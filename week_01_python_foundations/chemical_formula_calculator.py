
from periodictable import formula


def calculate_molar_mass(formula_text):
    """Calculate molar mass and display the elemental contributions."""

    formula_text = formula_text.strip()

    if not formula_text:
        raise ValueError("Please enter a chemical formula.")

    compound = formula(formula_text)
    atoms = compound.atoms

    if not atoms:
        raise ValueError("No elements were found in the formula.")

    total_mass = 0.0

    print(f"\nChemical formula: {formula_text}")
    print("\nElement | Atom count | Atomic mass | Contribution")
    print("-" * 59)

    for element, count in atoms.items():
        atomic_mass = element.mass
        contribution = count * atomic_mass
        total_mass += contribution

        print(
            f"{element.symbol:^7} | {count:^10} | "
            f"{atomic_mass:^12.4f} | {contribution:^12.4f}"
        )

    print("-" * 59)
    print(f"Total molar mass: {total_mass:.4f} g/mol")

    return total_mass


def main():
    print("CHEMICAL MOLAR MASS CALCULATOR")
    print("Examples: H2O, NaCl, Ca(OH)2, Al2(SO4)3")
    print("Type 'quit' to exit.")

    while True:
        formula_text = input("\nEnter a chemical formula: ").strip()

        if formula_text.lower() == "quit":
            print("Calculator closed.")
            break

        try:
            calculate_molar_mass(formula_text)
        except (ValueError, KeyError, TypeError, AttributeError) as error:
            print(f"Could not process formula: {error}")


if __name__ == "__main__":
    main()
