
from periodictable import formula, elements
from periodictable.constants import avogadro_number


def get_formula(formula_text):
    """Parse and validate a chemical formula."""

    formula_text = formula_text.strip()

    if not formula_text:
        raise ValueError("Please enter a chemical formula.")

    compound = formula(formula_text)

    if not compound.atoms:
        raise ValueError("No elements were found.")

    return compound


def calculate_molar_mass(compound):
    """Return the formula mass in g/mol numerically."""

    return compound.mass


def show_composition(compound):
    """Display elemental composition and percentage by mass."""

    total_mass = calculate_molar_mass(compound)

    print("\nELEMENTAL COMPOSITION")
    print("-" * 68)
    print(
        f"{'Element':<10}{'Atoms':>10}{'Atomic mass':>16}"
        f"{'Contribution':>16}{'% by mass':>16}"
    )
    print("-" * 68)

    for atom, count in compound.atoms.items():
        element = atom.element if hasattr(atom, "element") else atom

        atomic_mass = element.mass
        contribution = count * atom.mass
        percentage = (contribution / total_mass) * 100

        print(
            f"{element.symbol:<10}{count:>10g}"
            f"{atomic_mass:>16.4f}"
            f"{contribution:>16.4f}"
            f"{percentage:>15.2f}%"
        )

    print("-" * 68)
    print(f"Total formula mass: {total_mass:.4f} g/mol")


def mass_to_moles(compound, mass):
    """Convert sample mass in grams to moles."""

    if mass < 0:
        raise ValueError("Mass cannot be negative.")

    return mass / calculate_molar_mass(compound)


def moles_to_mass(compound, moles):
    """Convert moles to sample mass in grams."""

    if moles < 0:
        raise ValueError("Amount in moles cannot be negative.")

    return moles * calculate_molar_mass(compound)


def moles_to_particles(moles):
    """Calculate number of particles using Avogadro's constant."""

    if moles < 0:
        raise ValueError("Amount in moles cannot be negative.")

    return moles * avogadro_number


def particles_to_moles(particles):
    """Convert number of particles to moles."""

    if particles < 0:
        raise ValueError("Number of particles cannot be negative.")

    return particles / avogadro_number


def show_element_information():
    """Look up an element by symbol or name."""

    query = input("Enter element symbol or name: ").strip()

    if not query:
        raise ValueError("Enter an element symbol or name.")

    try:
        element = elements.symbol(query)
    except (ValueError, KeyError):
        element = elements.name(query.lower())

    print("\nELEMENT INFORMATION")
    print("-" * 35)
    print(f"Name: {element.name}")
    print(f"Symbol: {element.symbol}")
    print(f"Atomic number: {element.number}")
    print(f"Atomic mass: {element.mass:.5f} u")
    print(f"Density: {element.density} g/cm³")


def run_formula_calculations():
    """Menu for calculations involving a chemical formula."""

    formula_text = input("Enter chemical formula: ")
    compound = get_formula(formula_text)
    molar_mass = calculate_molar_mass(compound)

    print(f"\nFormula: {formula_text}")
    print(f"Molar mass: {molar_mass:.4f} g/mol")

    while True:
        print("\nFORMULA CALCULATIONS")
        print("1. Show elemental composition")
        print("2. Convert mass to moles")
        print("3. Convert moles to mass")
        print("4. Convert moles to particles")
        print("5. Convert particles to moles")
        print("6. Calculate atoms in a sample")
        print("0. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_composition(compound)

        elif choice == "2":
            mass = float(input("Enter sample mass in grams: "))
            moles = mass_to_moles(compound, mass)
            print(f"Amount: {moles:.6g} mol")

        elif choice == "3":
            moles = float(input("Enter amount in moles: "))
            mass = moles_to_mass(compound, moles)
            print(f"Mass: {mass:.6g} g")

        elif choice == "4":
            moles = float(input("Enter amount in moles: "))
            particles = moles_to_particles(moles)
            print(f"Number of particles: {particles:.6g}")

        elif choice == "5":
            particles = float(input("Enter number of particles: "))
            moles = particles_to_moles(particles)
            print(f"Amount: {moles:.6g} mol")

        elif choice == "6":
            mass = float(input("Enter sample mass in grams: "))
            moles = mass_to_moles(compound, mass)
            particles = moles_to_particles(moles)

            print(f"\nAmount of compound: {moles:.6g} mol")
            print(f"Number of formula units: {particles:.6g}")

            print("\nNumber of atoms of each element:")
            for atom, count in compound.atoms.items():
                element = atom.element if hasattr(atom, "element") else atom
                print(
                    f"{element.symbol}: "
                    f"{particles * count:.6g} atoms"
                )

        elif choice == "0":
            break

        else:
            print("Invalid option. Choose from the menu.")


def main():
    print("=" * 45)
    print("       CHEMISTRY CALCULATION TOOL")
    print("=" * 45)

    while True:
        print("\nMAIN MENU")
        print("1. Formula and molar mass calculations")
        print("2. Look up an element")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                run_formula_calculations()

            elif choice == "2":
                show_element_information()

            elif choice == "0":
                print("Calculator closed.")
                break

            else:
                print("Invalid option. Choose 0, 1, or 2.")

        except (ValueError, KeyError, TypeError, AttributeError) as error:
            print(f"Could not complete calculation: {error}")


if __name__ == "__main__":
    main()
