
import streamlit as st
from periodictable import formula

# ============================================================
# CHEMWISE — A SMART CHEMISTRY TOOLKIT
# Developed by Adenuga Aminat Aderonke
# ============================================================

AVOGADRO = 6.02214076e23

# -------------------- PAGE CONFIGURATION --------------------

st.set_page_config(
    page_title="ChemWise | Smart Chemistry Toolkit",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- CUSTOM PURPLE THEME --------------------

st.markdown(
    """
    <style>
    /* Main application background */
    [data-testid="stAppViewContainer"] {
        background-color: #6D28D9;
    }

    [data-testid="stMain"] {
        background-color: #6D28D9;
    }

    /* White top header */
    [data-testid="stHeader"] {
        background-color: #FFFFFF;
    }

    /* Main content spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Main text */
    [data-testid="stAppViewContainer"] .stMarkdown,
    [data-testid="stAppViewContainer"] label,
    [data-testid="stAppViewContainer"] .stMetricLabel,
    [data-testid="stAppViewContainer"] .stMetricValue {
        color: #FFFFFF;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #4C1D95;
    }

    [data-testid="stSidebar"] * {
        color: #FFFFFF;
    }

    /* Input fields */
    .stTextInput input,
    .stNumberInput input {
        background-color: #FFFFFF;
        color: #241044;
        border: 1px solid #DDD6FE;
        border-radius: 8px;
    }

    /* Select boxes */
    [data-baseweb="select"] > div {
        background-color: #FFFFFF;
        color: #241044;
        border-radius: 8px;
    }

    /* Buttons */
    .stButton > button {
        background-color: #FFFFFF;
        color: #5B21B6;
        border: 2px solid #FFFFFF;
        border-radius: 10px;
        font-weight: 700;
        padding: 0.55rem 1.2rem;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background-color: #EDE9FE;
        color: #4C1D95;
        border-color: #DDD6FE;
    }

    /* White result panels */
    .result-card {
        background-color: #FFFFFF;
        color: #241044;
        padding: 22px;
        border-radius: 14px;
        margin: 14px 0;
        box-shadow: 0 4px 15px rgba(31, 10, 65, 0.12);
    }

    .result-card h3,
    .result-card p,
    .result-card strong {
        color: #4C1D95;
    }

    .result-number {
        color: #6D28D9;
        font-size: 1.8rem;
        font-weight: 750;
    }

    /* Tables */
    [data-testid="stTable"] {
        background-color: #FFFFFF;
        border-radius: 10px;
        overflow: hidden;
    }

    /* White footer */
    .chemwise-footer {
        background-color: #FFFFFF;
        color: #4C1D95;
        text-align: center;
        padding: 28px 15px;
        border-radius: 14px;
        margin-top: 45px;
        line-height: 1.8;
    }

    .chemwise-footer h3 {
        color: #6D28D9;
        margin-bottom: 4px;
    }

    .chemwise-footer p {
        color: #4C1D95;
        margin: 3px 0;
    }

    .chemwise-footer a {
        color: #6D28D9;
        font-weight: 600;
    }

    /* Divider */
    hr {
        border-color: #DDD6FE;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -------------------- CHEMISTRY FUNCTIONS --------------------

def get_compound(formula_text):
    """Return the parsed compound, atom counts, and molar mass."""

    text = formula_text.strip()

    if not text:
        raise ValueError("Please enter a chemical formula.")

    compound = formula(text)
    atoms = compound.atoms

    if not atoms:
        raise ValueError("No elements were found in the formula.")

    for element, count in atoms.items():
        if element.mass is None or count <= 0:
            raise ValueError("The formula contains invalid data.")

    molar_mass = sum(
        element.mass * count
        for element, count in atoms.items()
    )

    if molar_mass <= 0:
        raise ValueError("Could not calculate a valid molar mass.")

    return compound, molar_mass


def get_element_rows(compound, molar_mass):
    """Create a breakdown of each element's mass contribution."""

    rows = []

    for element, count in compound.atoms.items():
        contribution = element.mass * count
        percentage = contribution / molar_mass * 100

        rows.append({
            "Element": element.name.title(),
            "Symbol": element.symbol,
            "Atom count": count,
            "Atomic mass (u)": round(element.mass, 4),
            "Mass contribution (g/mol)": round(contribution, 4),
            "Percentage (%)": round(percentage, 2)
        })

    return rows


def show_molar_mass(compound, molar_mass):
    """Display the molar mass and element breakdown."""

    st.markdown(
        f"""
        <div class="result-card">
            <h3>Calculated molar mass</h3>
            <div class="result-number">{molar_mass:.4f} g/mol</div>
            <p>Molar mass is the mass of one mole of the compound.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Element breakdown")
    st.table(get_element_rows(compound, molar_mass))


def display_error(error):
    """Show understandable errors without crashing the app."""

    st.error(f"Unable to complete the calculation: {error}")


# -------------------- WHITE APPLICATION HEADER --------------------

st.markdown(
    """
    <div style="
        background-color: #FFFFFF;
        color: #4C1D95;
        padding: 24px;
        border-radius: 14px;
        margin-bottom: 25px;
    ">
        <div style="font-size: 2.5rem; font-weight: 800;">
            ⚗️ ChemWise
        </div>
        <div style="
            font-size: 1.05rem;
            color: #6D28D9;
            font-weight: 600;
        ">
            A Smart Chemistry Toolkit
        </div>
        <p style="color: #5B5567; margin-bottom: 0;">
            Calculate, explore, and understand the numbers behind chemistry.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# -------------------- SIDEBAR NAVIGATION --------------------

st.sidebar.markdown(
    """
    <div style="text-align: center; padding: 10px 0 20px;">
        <div style="font-size: 2.3rem;">⚗️</div>
        <h2 style="color: white; margin-bottom: 0;">ChemWise</h2>
        <p style="color: #DDD6FE;">Chemistry tools</p>
    </div>
    """,
    unsafe_allow_html=True
)

calculation = st.sidebar.selectbox(
    "SELECT A CALCULATION",
    [
        "Molar Mass",
        "Percentage Composition",
        "Mass to Moles",
        "Moles to Mass",
        "Moles to Particles",
        "Particles to Moles",
        "Element Information"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption(
    "Designed for chemistry learning, practice, and calculations."
)


# -------------------- 1. MOLAR MASS --------------------

if calculation == "Molar Mass":

    st.header("Molar Mass Calculator")

    st.write(
        "Calculate the molar mass of an element, ionic compound, "
        "or molecular compound."
    )

    formula_text = st.text_input(
        "Chemical formula",
        placeholder="Examples: H2O, NaCl, Ca(OH)2"
    )

    if st.button("Calculate molar mass", key="molar_mass"):

        try:
            compound, molar_mass = get_compound(formula_text)
            show_molar_mass(compound, molar_mass)

        except Exception as error:
            display_error(error)


# -------------------- 2. PERCENTAGE COMPOSITION --------------------

elif calculation == "Percentage Composition":

    st.header("Percentage Composition")

    st.write(
        "Determine the percentage by mass contributed by each "
        "element in a chemical compound."
    )

    formula_text = st.text_input(
        "Chemical formula",
        placeholder="Example: H2SO4"
    )

    if st.button("Calculate composition", key="composition"):

        try:
            compound, molar_mass = get_compound(formula_text)

            show_molar_mass(compound, molar_mass)

            st.subheader("Percentage by mass")

            rows = get_element_rows(compound, molar_mass)

            st.table([
                {
                    "Element": row["Element"],
                    "Symbol": row["Symbol"],
                    "Percentage by mass (%)": row["Percentage (%)"]
                }
                for row in rows
            ])

            st.info(
                "The elemental mass percentages should total "
                "approximately 100%, subject to rounding."
            )

        except Exception as error:
            display_error(error)


# -------------------- 3. MASS TO MOLES --------------------

elif calculation == "Mass to Moles":

    st.header("Convert Mass to Moles")

    st.write("Calculate the amount of substance from its mass.")

    formula_text = st.text_input(
        "Chemical formula",
        placeholder="Example: NaCl"
    )

    mass = st.number_input(
        "Sample mass (g)",
        min_value=0.0,
        value=10.0,
        step=1.0
    )

    if st.button("Calculate amount", key="mass_to_moles"):

        try:
            _, molar_mass = get_compound(formula_text)
            moles = mass / molar_mass

            st.markdown(
                f"""
                <div class="result-card">
                    <h3>Amount of substance</h3>
                    <div class="result-number">{moles:.6g} mol</div>
                    <p>Molar mass: {molar_mass:.4f} g/mol</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.subheader("Calculation")

            st.latex(r"n = \frac{m}{M}")

            st.write(
                f"n = {mass:g} g ÷ {molar_mass:.4f} g/mol"
            )

            st.write(f"**Answer: {moles:.6g} mol**")

        except Exception as error:
            display_error(error)


# -------------------- 4. MOLES TO MASS --------------------

elif calculation == "Moles to Mass":

    st.header("Convert Moles to Mass")

    st.write("Calculate the mass corresponding to a given amount.")

    formula_text = st.text_input(
        "Chemical formula",
        placeholder="Example: NaCl"
    )

    moles = st.number_input(
        "Amount of substance (mol)",
        min_value=0.0,
        value=1.0,
        step=0.1
    )

    if st.button("Calculate mass", key="moles_to_mass"):

        try:
            _, molar_mass = get_compound(formula_text)
            mass = moles * molar_mass

            st.markdown(
                f"""
                <div class="result-card">
                    <h3>Sample mass</h3>
                    <div class="result-number">{mass:.4f} g</div>
                    <p>Molar mass: {molar_mass:.4f} g/mol</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.subheader("Calculation")

            st.latex(r"m = n \times M")

            st.write(
                f"m = {moles:g} mol × {molar_mass:.4f} g/mol"
            )

            st.write(f"**Answer: {mass:.4f} g**")

        except Exception as error:
            display_error(error)


# -------------------- 5. MOLES TO PARTICLES --------------------

elif calculation == "Moles to Particles":

    st.header("Convert Moles to Particles")

    st.write(
        "Use Avogadro's constant to determine the number of "
        "entities represented by a quantity in moles."
    )

    moles = st.number_input(
        "Amount of substance (mol)",
        min_value=0.0,
        value=1.0,
        step=0.1,
        format="%.8f"
    )

    particle_type = st.selectbox(
        "Type of entity",
        ["Atoms", "Molecules", "Formula units", "Particles"]
    )

    if st.button("Calculate particles", key="moles_to_particles"):

        particles = moles * AVOGADRO

        st.markdown(
            f"""
            <div class="result-card">
                <h3>Number of {particle_type.lower()}</h3>
                <div class="result-number">{particles:.6e}</div>
                <p>Avogadro constant: {AVOGADRO:.8e} mol⁻¹</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader("Calculation")

        st.latex(r"N = n \times N_A")

        st.write(
            f"N = {moles:g} mol × {AVOGADRO:.8e} mol⁻¹"
        )

        st.write(f"**Answer: {particles:.6e} entities**")

        st.caption(
            "Choose the entity type appropriate to your substance. "
            "For example, NaCl is counted in formula units, while "
            "H2O is counted in molecules."
        )


# -------------------- 6. PARTICLES TO MOLES --------------------

elif calculation == "Particles to Moles":

    st.header("Convert Particles to Moles")

    st.write(
        "Calculate the amount of substance from the number of entities."
    )

    particles = st.number_input(
        "Number of entities",
        min_value=0.0,
        value=float(AVOGADRO),
        step=1.0,
        format="%.6e"
    )

    if st.button("Calculate moles", key="particles_to_moles"):

        moles = particles / AVOGADRO

        st.markdown(
            f"""
            <div class="result-card">
                <h3>Amount of substance</h3>
                <div class="result-number">{moles:.6g} mol</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.subheader("Calculation")

        st.latex(r"n = \frac{N}{N_A}")

        st.write(
            f"n = {particles:.6e} ÷ {AVOGADRO:.8e}"
        )

        st.write(f"**Answer: {moles:.6g} mol**")


# -------------------- 7. ELEMENT INFORMATION --------------------

elif calculation == "Element Information":

    st.header("Element Information")

    st.write(
        "Look up basic information about a chemical element "
        "using its chemical symbol."
    )

    symbol = st.text_input(
        "Element symbol",
        placeholder="Examples: Fe, Na, O, Au"
    ).strip()

    if st.button("Look up element", key="element_info"):

        try:
            if (
                not symbol.isalpha()
                or len(symbol) > 2
            ):
                raise ValueError(
                    "Enter a valid element symbol, such as Fe or Na."
                )

            element_formula, _ = get_compound(symbol.capitalize())
            atoms = element_formula.atoms

            if len(atoms) != 1:
                raise ValueError(
                    "Enter the symbol of one element, such as Fe."
                )

            element, count = next(iter(atoms.items()))

            if count != 1 or element.symbol != symbol.capitalize():
                raise ValueError(
                    "That is not a recognised element symbol."
                )

            st.markdown(
                f"""
                <div class="result-card">
                    <h3>{element.name.title()}</h3>
                    <div class="result-number">{element.symbol}</div>
                    <p>Basic periodic-table information</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Atomic number", element.number)

            with col2:
                st.metric("Atomic mass", f"{element.mass:.4f} u")

            st.write(
                f"**Element:** {element.name.title()}"
            )

            st.write(f"**Symbol:** {element.symbol}")

            st.write(f"**Atomic number:** {element.number}")

            st.write(f"**Atomic mass:** {element.mass:.4f} u")

            st.caption(
                "Atomic masses are based on the values supplied "
                "by the periodictable library."
            )

        except Exception as error:
            display_error(error)


# -------------------- WHITE FOOTER --------------------

st.markdown(
    """
    <div class="chemwise-footer">
        <h3>⚗️ ChemWise</h3>
        <p><strong>A Smart Chemistry Toolkit</strong></p>
        <p>Developed by Adenuga Aminat Aderonke</p>
        <p><em>Chemist | Educator | AI & Materials Researcher</em></p>
        <p>Creator of The Sassy Lecturer</p>
        <br>
        <p style="font-size: 0.85rem;">
            © 2026 Adenuga Aminat Aderonke. All rights reserved.
        </p>
        <p style="font-size: 0.78rem; color: #6B5B7B;">
            Built with Python and Streamlit.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
