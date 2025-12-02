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
                <p style="font-weight: 400; font-family:'Inter', san-serif; font-size: 1.2rem; line-height: 1.7; text-align: justify;">Our research delivers rigorous analysis through working papers (preliminary findings), discussion papers (policy-focused insights), and comprehensive reports, 
                all essential reading for policymakers navigating Malaysia's strategic challenges. Through data visualisation, we advocate for the knowledge we acquire, making 
                insights accessible and encouraging informed public discourse.</p>
                <p style="font-weight: 400; font-family:'Inter', san-serif; font-size: 1.2rem; line-height: 1.7; text-align: justify;">Our commentary features expert opinions on current issues, offering timely perspectives (views expressed are individual, not institutional).</p>
                <p style="font-weight: 400; font-family:'Inter', san-serif; font-size: 1.2rem; line-height: 1.7; text-align: justify;">Together, these publications shape informed policy decisions and public discourse, translating complex data into actionable knowledge for Malaysia's progress.</p>
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
                For a comprehensive explanation of the data, please refer to this
                <a href="https://www.krinstitute.org/publication/working-paper" target="_blank" 
                style="color: ##e2e8f0; text-decoration: underline;">
                    paper
                </a> .This dashboard offers a visual representation of that information.
                </p>

                <p style="font-weight: 400; font-family:'Inter', san-serif; font-size: 1.2rem; line-height: 1.7; text-align: justify;">
                For an interactive experience, please also check out this
                <a href="https://www.krinstitute.org/publication/working-paper" target="_blank" 
                style="color: ##e2e8f0; text-decoration: underline;">
                     scorllytelling
                </a> .
                </p>
            </div>
            """
        )
