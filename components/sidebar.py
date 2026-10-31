
import streamlit as st


TOOLS = [
    "Dashboard",
    "Molar Mass",
    "Percentage Composition",
    "Mass to Moles",
    "Moles to Mass",
    "Moles to Particles",
    "Particles to Moles",
    "Element Information",
]


def navigate_to(tool_name):
    """Update navigation before the radio widget is rendered."""
    st.session_state["navigation"] = tool_name


def render_sidebar():
    """Render ChemWise navigation and theme controls."""

    if "navigation" not in st.session_state:
        st.session_state["navigation"] = "Dashboard"

    with st.sidebar:

        st.markdown(
            """
            <div style="padding: 0.8rem 0 1.2rem;">
                <div style="
                    font-size: 1.7rem;
                    font-weight: 800;
                    color: var(--cw-primary);
                    letter-spacing: -1px;
                ">
                    ChemWise<span style="color: var(--cw-text);">.</span>
                </div>
                <div style="
                    color: var(--cw-muted);
                    font-size: 0.78rem;
                ">
                    Chemistry made clearer.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        st.markdown("**WORKSPACE**")

        selected_tool = st.radio(
            "Navigation",
            options=TOOLS,
            label_visibility="collapsed",
            key="navigation",
        )

        st.divider()

        st.markdown("**APPEARANCE**")

        dark_mode = st.toggle(
            "Dark mode",
            value=False,
            key="dark_mode",
        )

        st.divider()

        st.caption("ChemWise v2.0")
        st.caption("Built for chemistry learners.")

    return selected_tool, dark_mode
