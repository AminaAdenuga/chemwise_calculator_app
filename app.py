
import math
import streamlit as st

from calculations.molar_mass import (
    calculate_molar_mass,
    calculate_percentage_composition,
)

from calculations.stoichiometry import (
    mass_to_moles,
    moles_to_mass,
    moles_to_particles,
    particles_to_moles,
    AVOGADRO_CONSTANT,
)

from calculations.element_data import get_element_information

from styles.theme import apply_theme
from components.sidebar import render_sidebar, navigate_to
from components.header import render_header
from components.result_cards import (
    render_result_card,
    render_result_table,
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ChemWise | Chemistry Calculator",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# APPLICATION INITIALIZATION
# ============================================================

selected_tool, dark_mode = render_sidebar()

apply_theme(dark_mode)


# ============================================================
# SHARED FUNCTIONS
# ============================================================

def show_error(error):
    """Display a user-friendly calculation error."""
    st.error(str(error))


def show_formula(formula_text):
    """Display the mathematical relationship."""
    st.markdown(
        f"""
        <div class="cw-card">
            <div style="color:var(--cw-muted);font-size:0.8rem;">
                WORKING FORMULA
            </div>
            <div style="
                font-size:1.25rem;
                font-weight:700;
                margin-top:0.5rem;
                color:var(--cw-primary);
            ">
                {formula_text}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def format_scientific(number):
    """Format large or very small values."""
    return f"{number:.6e}"


def render_tool_intro(title, description, formula_text=None):
    render_header(title, description)

    if formula_text:
        show_formula(formula_text)

    st.write("")


# ============================================================
# DASHBOARD
# ============================================================

def render_dashboard():

    render_header(
        "Welcome to ChemWise",
        "Your chemistry calculation and learning workspace."
    )

    st.markdown(
        """
        Explore chemistry calculations, convert quantities
        and retrieve periodic-table information in one workspace.
        """
    )

    st.write("")

    # Overview metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        render_result_card("Available tools", "7", "calculators")

    with col2:
        render_result_card("Avogadro constant", "6.022 × 10²³", "mol⁻¹")

    with col3:
        render_result_card("Calculation engine", "Active", "Python")

    st.write("")
    st.divider()

    st.subheader("Explore your chemistry tools")

    st.caption("Select a tool to get started.")

    tools = [
        {
            "name": "Molar Mass",
            "description": "Calculate the molar mass of chemical compounds.",
            "symbol": "⚖️",
        },
        {
            "name": "Percentage Composition",
            "description": "Find the percentage by mass of each element.",
            "symbol": "🧪",
        },
        {
            "name": "Mass to Moles",
            "description": "Convert a substance's mass into moles.",
            "symbol": "→",
        },
        {
            "name": "Moles to Mass",
            "description": "Calculate mass from a given amount in moles.",
            "symbol": "→",
        },
        {
            "name": "Moles to Particles",
            "description": "Convert moles into representative particles.",
            "symbol": "🔬",
        },
        {
            "name": "Particles to Moles",
            "description": "Convert representative particles into moles.",
            "symbol": "🔬",
        },
        {
            "name": "Element Information",
            "description": "Explore basic periodic-table information.",
            "symbol": "⚛️",
        },
    ]

    columns = st.columns(3)

    for index, tool in enumerate(tools):

        with columns[index % 3]:

            st.markdown(
                f"""
                <div class="cw-card">
                    <div style="font-size:1.5rem;">
                        {tool["symbol"]}
                    </div>
                    <h3>{tool["name"]}</h3>
                    <p>{tool["description"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.button(
                f"Open {tool['name']}",
                key=f"dashboard_tool_{index}",
                use_container_width=True,
                on_click=navigate_to,
                args=(tool["name"],),
            )


# ============================================================
# 1. MOLAR MASS CALCULATOR
# ============================================================

def render_molar_mass():

    render_tool_intro(
        "Molar Mass Calculator",
        "Calculate the molar mass of a chemical compound.",
        "M = Σ (number of atoms × atomic mass)",
    )

    with st.form("molar_mass_form"):

        chemical_formula = st.text_input(
            "Chemical formula",
            placeholder="Examples: H2O, NaCl, H2SO4, Ca(OH)2",
            help="Enter a valid chemical formula using element symbols.",
        )

        submitted = st.form_submit_button(
            "Calculate molar mass",
            use_container_width=True,
        )

    if submitted:

        try:

            result = calculate_molar_mass(chemical_formula)

            st.success("Calculation completed successfully.")

            render_result_card(
                "Molar mass",
                f"{result:.4f}",
                "g/mol",
            )

            st.markdown("### Calculation details")

            st.write(
                f"The molar mass of **{chemical_formula.strip()}** "
                f"is **{result:.4f} g/mol**."
            )

            st.caption(
                "The result is calculated using the atomic masses "
                "provided by the periodic-table library."
            )

        except (ValueError, TypeError) as error:
            show_error(error)


# ============================================================
# 2. PERCENTAGE COMPOSITION CALCULATOR
# ============================================================

def render_percentage_composition():

    render_tool_intro(
        "Percentage Composition",
        "Determine the percentage by mass contributed by each element.",
        "% composition = (element mass contribution / molar mass) × 100",
    )

    with st.form("percentage_form"):

        chemical_formula = st.text_input(
            "Chemical formula",
            placeholder="Example: H2O",
        )

        submitted = st.form_submit_button(
            "Calculate composition",
            use_container_width=True,
        )

    if submitted:

        try:

            composition = calculate_percentage_composition(
                chemical_formula
            )

            total_mass = calculate_molar_mass(chemical_formula)

            st.success("Composition calculated successfully.")

            render_result_card(
                "Total molar mass",
                f"{total_mass:.4f}",
                "g/mol",
            )

            rows = []

            for item in composition:

                rows.append({
                    "Element": item["element"],
                    "Symbol": item["symbol"],
                    "Atom count": f"{item['atom_count']:g}",
                    "Atomic mass": f"{item['atomic_mass']:.4f}",
                    "Mass contribution": (
                        f"{item['mass_contribution']:.4f}"
                    ),
                    "Percentage": f"{item['percentage']:.2f}%",
                })

            st.markdown("### Elemental composition")

            render_result_table(rows)

            total_percentage = sum(
                item["percentage"] for item in composition
            )

            render_result_card(
                "Total percentage",
                f"{total_percentage:.2f}",
                "%",
            )

            st.caption(
                "Small differences from 100% may occur due to rounding."
            )

        except (ValueError, TypeError) as error:
            show_error(error)


# ============================================================
# 3. MASS TO MOLES
# ============================================================

def render_mass_to_moles():

    render_tool_intro(
        "Mass to Moles Converter",
        "Convert the mass of a substance into the amount in moles.",
        "n = m / M",
    )

    with st.form("mass_to_moles_form"):

        mass = st.number_input(
            "Mass (g)",
            min_value=0.0,
            value=18.015,
            step=0.1,
            format="%.6f",
        )

        molar_mass = st.number_input(
            "Molar mass (g/mol)",
            min_value=0.000001,
            value=18.015,
            step=0.1,
            format="%.6f",
        )

        submitted = st.form_submit_button(
            "Convert to moles",
            use_container_width=True,
        )

    if submitted:

        try:

            result = mass_to_moles(mass, molar_mass)

            st.success("Conversion completed.")

            render_result_card(
                "Amount of substance",
                f"{result:.6f}",
                "mol",
            )

            st.markdown("### Calculation working")

            st.write(f"Given mass, m = {mass:g} g")
            st.write(f"Molar mass, M = {molar_mass:g} g/mol")

            st.latex(
                r"n = \frac{m}{M}"
            )

            st.latex(
                rf"n = \frac{{{mass:g}}}{{{molar_mass:g}}}"
                rf" = {result:.6f}\ mol"
            )

        except (ValueError, TypeError) as error:
            show_error(error)


# ============================================================
# 4. MOLES TO MASS
# ============================================================

def render_moles_to_mass():

    render_tool_intro(
        "Moles to Mass Converter",
        "Calculate the mass corresponding to a given amount in moles.",
        "m = n × M",
    )

    with st.form("moles_to_mass_form"):

        moles = st.number_input(
            "Amount of substance (mol)",
            min_value=0.0,
            value=1.0,
            step=0.1,
            format="%.6f",
        )

        molar_mass = st.number_input(
            "Molar mass (g/mol)",
            min_value=0.000001,
            value=18.015,
            step=0.1,
            format="%.6f",
        )

        submitted = st.form_submit_button(
            "Calculate mass",
            use_container_width=True,
        )

    if submitted:

        try:

            result = moles_to_mass(moles, molar_mass)

            st.success("Calculation completed.")

            render_result_card(
                "Mass",
                f"{result:.6f}",
                "g",
            )

            st.markdown("### Calculation working")

            st.write(f"Amount, n = {moles:g} mol")
            st.write(f"Molar mass, M = {molar_mass:g} g/mol")

            st.latex(r"m = n \times M")

            st.latex(
                rf"m = {moles:g} \times {molar_mass:g}"
                rf" = {result:.6f}\ g"
            )

        except (ValueError, TypeError) as error:
            show_error(error)


# ============================================================
# 5. MOLES TO PARTICLES
# ============================================================

def render_moles_to_particles():

    render_tool_intro(
        "Moles to Particles Converter",
        "Calculate the number of representative particles in a sample.",
        "N = n × Nₐ",
    )

    with st.form("moles_to_particles_form"):

        moles = st.number_input(
            "Amount of substance (mol)",
            min_value=0.0,
            value=1.0,
            step=0.1,
            format="%.8f",
        )

        particle_type = st.selectbox(
            "Type of representative particle",
            [
                "Atoms",
                "Molecules",
                "Ions",
                "Formula units",
            ],
        )

        submitted = st.form_submit_button(
            "Calculate particles",
            use_container_width=True,
        )

    if submitted:

        try:

            result = moles_to_particles(moles)

            st.success("Conversion completed.")

            render_result_card(
                f"Number of {particle_type.lower()}",
                format_scientific(result),
                "particles",
            )

            st.markdown("### Calculation working")

            st.write(f"Amount, n = {moles:g} mol")

            st.write(
                "Avogadro constant = "
                f"{AVOGADRO_CONSTANT:.8e} mol⁻¹"
            )

            st.latex(r"N = n \times N_A")

            st.latex(
                rf"N = {moles:g} \times "
                rf"{AVOGADRO_CONSTANT:.8e}"
            )

            st.write(
                f"Therefore, the sample contains "
                f"**{result:.6e} {particle_type.lower()}**."
            )

        except (ValueError, TypeError) as error:
            show_error(error)


# ============================================================
# 6. PARTICLES TO MOLES
# ============================================================

def render_particles_to_moles():

    render_tool_intro(
        "Particles to Moles Converter",
        "Determine the amount of substance from its particle count.",
        "n = N / Nₐ",
    )

    with st.form("particles_to_moles_form"):

        particles = st.number_input(
            "Number of particles",
            min_value=0.0,
            value=6.02214076e23,
            step=1.0,
            format="%.6e",
        )

        particle_type = st.selectbox(
            "Type of representative particle",
            [
                "Atoms",
                "Molecules",
                "Ions",
                "Formula units",
            ],
        )

        submitted = st.form_submit_button(
            "Convert to moles",
            use_container_width=True,
        )

    if submitted:

        try:

            result = particles_to_moles(particles)

            st.success("Conversion completed.")

            render_result_card(
                "Amount of substance",
                f"{result:.8f}",
                "mol",
            )

            st.markdown("### Calculation working")

            st.write(
                f"Number of {particle_type.lower()} = "
                f"{particles:.6e}"
            )

            st.latex(r"n = \frac{N}{N_A}")

            st.latex(
                rf"n = \frac{{{particles:.6e}}}"
                rf"{{{AVOGADRO_CONSTANT:.8e}}}"
                rf" = {result:.8f}\ mol"
            )

        except (ValueError, TypeError) as error:
            show_error(error)


# ============================================================
# 7. ELEMENT INFORMATION
# ============================================================

def render_element_information():

    render_tool_intro(
        "Element Information",
        "Retrieve basic information about an element in the periodic table."
    )

    with st.form("element_information_form"):

        symbol = st.text_input(
            "Element symbol",
            placeholder="Examples: Fe, Na, O, Cl",
            help="Use standard chemical element symbols.",
        )

        submitted = st.form_submit_button(
            "Find element",
            use_container_width=True,
        )

    if submitted:

        try:

            element = get_element_information(symbol)

            st.success("Element found.")

            st.markdown(
                f"""
                <div class="cw-card">
                    <div style="
                        font-size:3rem;
                        font-weight:800;
                        color:var(--cw-primary);
                    ">
                        {element["symbol"]}
                    </div>
                    <h2>{element["name"]}</h2>
                    <p>Periodic table element</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.write("")

            col1, col2 = st.columns(2)

            with col1:
                render_result_card(
                    "Atomic number",
                    str(element["atomic_number"]),
                )

            with col2:
                mass = element["atomic_mass"]

                render_result_card(
                    "Atomic mass",
                    f"{mass:.4f}" if mass is not None else "N/A",
                    "u",
                )

            density = element["density"]

            if density is not None:
                render_result_card(
                    "Density",
                    f"{density:g}",
                    "g/cm³",
                )
            else:
                st.info("Density information is not available.")

        except (ValueError, TypeError) as error:
            show_error(error)


# ============================================================
# APPLICATION ROUTER
# ============================================================

PAGES = {
    "Molar Mass": render_molar_mass,
    "Percentage Composition": render_percentage_composition,
    "Mass to Moles": render_mass_to_moles,
    "Moles to Mass": render_moles_to_mass,
    "Moles to Particles": render_moles_to_particles,
    "Particles to Moles": render_particles_to_moles,
    "Element Information": render_element_information,
}


if selected_tool == "Dashboard":

    render_dashboard()

elif selected_tool in PAGES:

    PAGES[selected_tool]()

else:

    st.error("The selected page could not be found.")
