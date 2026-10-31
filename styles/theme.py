
import streamlit as st
from pathlib import Path


THEMES = {
    "light": {
        "background": "#F8F7FC",
        "surface": "#FFFFFF",
        "surface_alt": "#F0ECF7",
        "text": "#302444",
        "muted": "#766D83",
        "primary": "#7652B5",
        "primary_hover": "#63409F",
        "button_bg": "#7652B5",
        "button_text": "#FFFFFF",
        "button_hover": "#63409F",
        "border": "#E5DDED",
        "card_bg": "linear-gradient(145deg, #FFFFFF, #F7F3FC)",
        "card_border": "#E5DDED",
        "card_shadow": "0 5px 18px rgba(48, 36, 68, 0.06)",
        "result_bg": "#F0EAF8",
        "input_background": "#FFFFFF",
        "success": "#287A57",
        "error": "#B4233D",
        "warning": "#96630B",
        "focus": "#A88BD2",
    },

    "dark": {
        "background": "#15111D",
        "surface": "#211A2C",
        "surface_alt": "#2C233A",
        "text": "#F3EDF9",
        "muted": "#B9AFC8",
        "primary": "#C4A5F5",
        "primary_hover": "#D5BEFF",
        "button_bg": "#C4A5F5",
        "button_text": "#21172E",
        "button_hover": "#D5BEFF",
        "border": "#493A5E",
        "card_bg": "linear-gradient(145deg, #2A2138, #211A2C)",
        "card_border": "#493A5E",
        "card_shadow": "0 8px 24px rgba(0, 0, 0, 0.24)",
        "result_bg": "#332744",
        "input_background": "#2B2238",
        "success": "#83D6AD",
        "error": "#FF9BAA",
        "warning": "#F3CC7A",
        "focus": "#C4A5F5",
    },
}


def load_css():
    """Load the shared application stylesheet."""

    css_path = Path(__file__).parent / "main.css"

    if not css_path.exists():
        raise FileNotFoundError(
            f"Stylesheet not found: {css_path}"
        )

    return css_path.read_text(encoding="utf-8")


def apply_theme(dark_mode=False):
    """Apply the selected visual theme."""

    theme_name = "dark" if dark_mode else "light"
    colors = THEMES[theme_name]

    css_variables = "\n".join(
        f"--cw-{key.replace('_', '-')}: {value};"
        for key, value in colors.items()
    )

    css = load_css()

    st.markdown(
        f"""
        <style>
        :root {{
            {css_variables}
            color-scheme: {theme_name};
        }}

        {css}
        </style>
        """,
        unsafe_allow_html=True,
    )
