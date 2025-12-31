import streamlit as st
import base64
from pathlib import Path

# Convert local image to base64
img_path = Path("pictures/KRI_Weave.jpg")
img_base64 = base64.b64encode(img_path.read_bytes()).decode()

def render_about():
    """Renders the About page with a centered background image in the About box."""

    st.markdown(
        f"""
        <style>
        /* About box with background image */
        .about-box {{
            background-image: url("data:image/jpeg;base64,{img_base64}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            padding: 30px;
            border-radius: 10px;
            color: rgba(204, 68, 0);
        }}

        /* Content overlay */
        .about-box-content {{
            background-color: rgba(0, 0, 0, 0); 
            padding: 20px;
            border-radius: 10px;
            text-align: justify;
            color: black;
        }}

        a {{
            color: white !important;
            text-decoration: underline;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Main header box
    st.markdown(
        """
        <div class="about-box">
            <div class="about-box-content">
                <h1 style="font-weight: 700; font-family:'Crimson Pro', serif; font-size: 2.5rem; line-height: 1.1; text-align: left">KRI Data Visualisation</h1>
                <p style="font-weight: 500; font-family:'Inter', san-serif; font-size: 1.25rem; line-height: 1.7;">A research narrative combines data with context and human stories, making findings clearer, more relatable, and impactful.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Two columns
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(
            """
            <div>
                <h2 style="font-weight: 600; font-family:'Inter', san-serif; font-size: 1.25rem; line-height: 1.6;">About KRI Data Visualisation</h2>
                <p style="font-weight: 400; font-family:'Inter', san-serif; font-size: 1.2rem; line-height: 1.7; text-align: justify;">At Khazanah Research Institute (KRI), we believe that data comes alive when it is seen and understood. Through clear, compelling, and interactive data visualisations, we turn complex research findings into stories that are accessible, relatable, and actionable. </p>
                <p style="font-weight: 400; font-family:'Inter', san-serif; font-size: 1.2rem; line-height: 1.7; text-align: justify;">Our visualisations highlight the patterns, trends, and human dimensions behind Malaysia’s most pressing economic, social, and structural challenges, helping policymakers, communities, and the public make informed decisions that strengthen families, uplift communities, and drive inclusive national progress.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.html(
            f"""
            <div>

                <h2 style="font-weight: 600; font-family:'Inter', san-serif; font-size: 1.25rem; line-height: 1.6;">Further Reading</h2>
                <p style="font-weight: 400; font-family:'Inter', san-serif; font-size: 1.2rem; line-height: 1.7; text-align: justify;">
                For a comprehensive explanation of the data, please refer to our
                <a href="https://www.krinstitute.org/publications/assessing-bus-performance-in-greater-kuala-lumpur" target="_blank" 
                style="color: ##e2e8f0; text-decoration: underline;">
                    paper
                </a> .This dashboard offers a visual representation of that information.
                </p>

                <p style="font-weight: 400; font-family:'Inter', san-serif; font-size: 1.2rem; line-height: 1.7; text-align: justify;">
                For an interactive experience, please also check out our
                <a href="https://www.krinstitute.org/publications/data-bus-scrollytelling" target="_blank" 
                style="color: ##e2e8f0; text-decoration: underline;">
                     scrollytelling
                </a> .
                </p>
            </div>
            """
        )
