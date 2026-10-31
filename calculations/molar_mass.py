
from periodictable import formula


def _parse_formula(formula_text):
    """
    Validate and parse a chemical formula.

    Returns:
        tuple: Cleaned formula and its element composition.
    """

    if not isinstance(formula_text, str):
        raise ValueError("Chemical formula must be text.")

    cleaned_formula = formula_text.strip()

    if not cleaned_formula:
        raise ValueError("Please enter a chemical formula.")

    try:
        compound = formula(cleaned_formula)
    except Exception as error:
        raise ValueError(
            f"'{cleaned_formula}' is not a valid chemical formula."
        ) from error

    atoms = compound.atoms

    if not atoms:
        raise ValueError("No elements were found in the formula.")

    for element, count in atoms.items():
        if element.mass is None or count <= 0:
            raise ValueError(
                "The formula contains an invalid element or atom count."
            )

    return cleaned_formula, atoms


def calculate_molar_mass(formula_text):
    """
    Calculate molar mass in grams per mole (g/mol).
    """

    _, atoms = _parse_formula(formula_text)

    molar_mass = sum(
        element.mass * count
        for element, count in atoms.items()
    )

    if molar_mass <= 0:
        raise ValueError("Could not calculate a valid molar mass.")

    return float(molar_mass)


def calculate_percentage_composition(formula_text):
    """
    Calculate the percentage by mass of each element.

    Returns:
        list: Element composition records.
    """

    cleaned_formula, atoms = _parse_formula(formula_text)

    total_molar_mass = calculate_molar_mass(cleaned_formula)

    composition = []

    for element, count in atoms.items():

        mass_contribution = element.mass * count

        percentage = (
            mass_contribution / total_molar_mass
        ) * 100

        composition.append({
            "element": element.name.title(),
            "symbol": element.symbol,
            "atom_count": float(count),
            "atomic_mass": float(element.mass),
            "mass_contribution": float(mass_contribution),
            "percentage": float(percentage),
        })

    return composition
