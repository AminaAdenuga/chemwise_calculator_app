
import streamlit as st


def render_header(title, description=None):
    """Display a consistent ChemWise page header."""

    st.markdown(
        f"""
        <div style="margin-bottom: 1.5rem;">
            <h1 style="
                font-size: 2rem;
                font-weight: 750;
                margin-bottom: 0.35rem;
                color: var(--cw-text);
            ">
                {title}
            </h1>
            <p style="
                color: var(--cw-muted);
                font-size: 0.95rem;
                margin-top: 0;
            ">
                {description or ""}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
