
import pytest

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


# -----------------------------------------
# MOLAR MASS TESTS
# -----------------------------------------

@pytest.mark.parametrize(
    "chemical_formula, expected",
    [
        ("H2O", 18.015),
        ("NaCl", 58.44),
        ("H2SO4", 98.079),
        ("Ca(OH)2", 74.092),
    ],
)
def test_molar_mass(chemical_formula, expected):

    result = calculate_molar_mass(chemical_formula)

    assert result == pytest.approx(expected, abs=0.03)


@pytest.mark.parametrize(
    "invalid_input",
    ["", "   ", "XYZ123", None, 123],
)
def test_invalid_chemical_formula(invalid_input):

    with pytest.raises(ValueError):
        calculate_molar_mass(invalid_input)


# -----------------------------------------
# PERCENTAGE COMPOSITION TESTS
# -----------------------------------------

def test_percentage_composition_totals_100():

    result = calculate_percentage_composition("H2O")

    total_percentage = sum(
        item["percentage"] for item in result
    )

    assert total_percentage == pytest.approx(100.0)


# -----------------------------------------
# MASS TO MOLES TESTS
# -----------------------------------------

def test_mass_to_moles():

    result = mass_to_moles(18.015, 18.015)

    assert result == pytest.approx(1.0)


def test_mass_to_moles_with_zero_mass():

    result = mass_to_moles(0, 18.015)

    assert result == 0


# -----------------------------------------
# MOLES TO MASS TESTS
# -----------------------------------------

def test_moles_to_mass():

    result = moles_to_mass(2, 18.015)

    assert result == pytest.approx(36.03)


# -----------------------------------------
# PARTICLE CONVERSION TESTS
# -----------------------------------------

def test_moles_to_particles():

    result = moles_to_particles(1)

    assert result == pytest.approx(AVOGADRO_CONSTANT)


def test_particles_to_moles():

    result = particles_to_moles(AVOGADRO_CONSTANT)

    assert result == pytest.approx(1.0)


# -----------------------------------------
# ELEMENT INFORMATION TESTS
# -----------------------------------------

def test_iron_information():

    result = get_element_information("Fe")

    assert result["name"] == "Iron"
    assert result["symbol"] == "Fe"
    assert result["atomic_number"] == 26


def test_invalid_element_symbol():

    with pytest.raises(ValueError):
        get_element_information("Xx")


# -----------------------------------------
# INPUT VALIDATION TESTS
# -----------------------------------------

@pytest.mark.parametrize(
    "function, arguments",
    [
        (mass_to_moles, (-1, 18)),
        (mass_to_moles, (10, 0)),
        (moles_to_mass, (-1, 18)),
        (moles_to_particles, (-1,)),
        (particles_to_moles, (-5,)),
    ],
)
def test_invalid_stoichiometry_inputs(function, arguments):

    with pytest.raises(ValueError):
        function(*arguments)
