
import streamlit as st
from periodictable import formula

st.set_page_config(
    page_title="Chemical Calculator",
    page_icon="⚗️",
    layout="centered"
)

st.title("⚗️ Chemical Calculator")
st.write("Calculate molar mass and explore chemical composition.")

chemical_formula = st.text_input(
    "Enter a chemical formula",
    placeholder="Examples: H2O, NaCl, Ca(OH)2"
)

if st.button("Calculate molar mass"):
    if not chemical_formula.strip():
        st.warning("Please enter a chemical formula.")
    else:
        try:
            compound = formula(chemical_formula.strip())
            total_mass = sum(
                element.mass * count
                for element, count in compound.atoms.items()
            )

            st.subheader("Calculation result")
            st.metric("Molar mass", f"{total_mass:.4f} g/mol")

            st.write("### Element breakdown")

            for element, count in compound.atoms.items():
                contribution = element.mass * count
                st.write(
                    f"**{element.symbol}**: {count} atom(s) × "
                    f"{element.mass:.4f} g/mol = "
                    f"{contribution:.4f} g/mol"
                )

        except Exception as error:
            st.error(f"Could not process that formula: {error}")
