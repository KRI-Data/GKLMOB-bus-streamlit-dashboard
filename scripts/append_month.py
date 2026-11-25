"""Add one month of Analysis output to the 3 shared data files.

Usage, from the repo root:
    python -m scripts.append_month 202610 path/to/analysis/output

The folder must hold that month's 6 files, e.g. Rapid_kl_monthly_bpi_202610.csv.
Nothing is written unless all 6 files pass every check, and the 3 shared files
are either all updated or all left as they were.
"""
import os
import sys
import tempfile
from pathlib import Path
import pandas as pd
from scripts.shared_format import KEYS, SOURCES, to_shared, check_values

DATASET = Path(__file__).resolve().parent.parent / "dataset"


def new_rows_for(month, yyyymm, folder):
    """Read and check all 6 files; return {shared name: rows to add}. Exits on any problem."""
    new_rows = {}
    for name, networks in SOURCES.items():
        existing = pd.read_csv(DATASET / f"{name}.csv", usecols=["month"])
        if month in set(existing["month"]):
            sys.exit(f"{name}.csv already has {month}. Nothing written.")

        parts = []
        for network, prefix in networks.items():
            path = Path(folder) / f"{prefix}_{yyyymm}.csv"
            if not path.exists():
                sys.exit(f"Missing {path}. Nothing written.")
            try:
                df = to_shared(name, network, pd.read_csv(path, keep_default_na=False, na_values=[""]), path.name)
                df = check_values(name, df, path.name)
            except ValueError as e:
                sys.exit(f"{e}. Nothing written.")
            other_months = set(df["month"]) - {month}
            if other_months:
                sys.exit(f"{path.name} also has rows for {sorted(other_months)}. Nothing written.")
            parts.append(df)

        df = pd.concat(parts, ignore_index=True)
        dupes = int(df.duplicated(subset=KEYS[name]).sum())
        if dupes:
            sys.exit(f"{name}: {dupes} duplicate rows in the new files. Nothing written.")
        new_rows[name] = df.sort_values(KEYS[name])
    return new_rows


def write_all(new_rows):
    """Append rows to every shared file, or change none of them.

    Each file is rebuilt in a temp file next to it, then all temps replace the
    originals. If a replace fails (e.g. the file is open in Excel), the files
    already replaced are put back from their original bytes.
    """
    originals, temps = {}, {}
    try:
        for name, df in new_rows.items():
            target = DATASET / f"{name}.csv"
            originals[target] = old = target.read_bytes()
            fd, tmp = tempfile.mkstemp(dir=DATASET, prefix=f".{name}.", suffix=".tmp")
            temps[target] = Path(tmp)
            with os.fdopen(fd, "wb") as f:
                f.write(old)
                if old and not old.endswith(b"\n"):
                    f.write(b"\n")
                f.write(df.to_csv(header=False, index=False, lineterminator="\n").encode("utf-8"))
            os.chmod(tmp, target.stat().st_mode)

        replaced = []
        try:
            for target, tmp in temps.items():
                replaced.append(target)  # listed first: restoring an untouched file is harmless
                os.replace(tmp, target)
        except BaseException as e:  # includes Ctrl-C
            stuck = restore(replaced, originals)
            if stuck:
                sys.exit(f"Could not write the shared files ({e}) and could not put back "
                         f"{', '.join(p.name for p in stuck)}. The 3 files may be out of sync. "
                         f"Run: git checkout -- dataset/*.csv")
            if isinstance(e, OSError):
                sys.exit(f"Could not write {target.name} ({e}). All shared files left unchanged.")
            raise
    finally:
        for tmp in temps.values():
            tmp.unlink(missing_ok=True)


def restore(targets, originals):
    """Put each file back to its original bytes (via temp file + replace, so never half-written).

    Tries every file even if one fails; returns the files that could not be restored.
    """
    stuck = []
    for target in targets:
        tmp = None
        try:
            fd, tmp = tempfile.mkstemp(dir=DATASET, prefix=f".{target.stem}.", suffix=".tmp")
            with os.fdopen(fd, "wb") as f:
                f.write(originals[target])
            os.replace(tmp, target)
        except OSError:
            stuck.append(target)
        finally:
            if tmp:
                Path(tmp).unlink(missing_ok=True)
    return stuck


def main(yyyymm, folder):
    if len(yyyymm) != 6 or not yyyymm.isdigit():
        sys.exit(f"Month must look like 202610, got {yyyymm!r}")
    month = f"{yyyymm[:4]}-{yyyymm[4:]}"

    new_rows = new_rows_for(month, yyyymm, folder)
    write_all(new_rows)
    for name, df in new_rows.items():
        print(f"{name}.csv: added {len(df):,} rows for {month}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
