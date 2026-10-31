
import math


# Exact SI-defined Avogadro constant
AVOGADRO_CONSTANT = 6.02214076e23


def _validate_number(value, label):
    """
    Check that a numerical input is valid and non-negative.
    """

    try:
        number = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{label} must be a number.")

    if not math.isfinite(number):
        raise ValueError(f"{label} must be a finite number.")

    if number < 0:
        raise ValueError(f"{label} cannot be negative.")

    return number


def _validate_positive(value, label):
    """Validate values that must be greater than zero."""

    number = _validate_number(value, label)

    if number == 0:
        raise ValueError(f"{label} must be greater than zero.")

    return number


def mass_to_moles(mass_g, molar_mass_g_mol):
    """
    Convert mass to moles.

    Formula:
        n = m / M
    """

    mass = _validate_number(mass_g, "Mass")

    molar_mass = _validate_positive(
        molar_mass_g_mol,
        "Molar mass"
    )

    return mass / molar_mass


def moles_to_mass(moles, molar_mass_g_mol):
    """
    Convert moles to mass.

    Formula:
        m = n × M
    """

    amount = _validate_number(moles, "Amount")

    molar_mass = _validate_positive(
        molar_mass_g_mol,
        "Molar mass"
    )

    return amount * molar_mass


def moles_to_particles(moles):
    """
    Convert moles to representative particles.

    Formula:
        N = n × NA
    """

    amount = _validate_number(moles, "Amount")

    return amount * AVOGADRO_CONSTANT


def particles_to_moles(particles):
    """
    Convert representative particles to moles.

    Formula:
        n = N / NA
    """

    number_of_particles = _validate_number(
        particles,
        "Number of particles"
    )

    return number_of_particles / AVOGADRO_CONSTANT
