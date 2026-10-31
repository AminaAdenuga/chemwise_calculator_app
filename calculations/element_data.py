
import periodictable


def get_element_information(symbol):
    """
    Retrieve basic periodic-table information
    using an element symbol.
    """

    if not isinstance(symbol, str):
        raise ValueError("Element symbol must be text.")

    cleaned_symbol = symbol.strip()

    if not cleaned_symbol:
        raise ValueError("Please enter an element symbol.")

    # Element symbols are case-sensitive.
    # Examples: Fe, O, Na, Cl
    element = getattr(periodictable, cleaned_symbol, None)

    if element is None or not hasattr(element, "number"):
        raise ValueError(
            f"'{cleaned_symbol}' is not a recognised element symbol."
        )

    return {
        "name": element.name.title(),
        "symbol": element.symbol,
        "atomic_number": element.number,
        "atomic_mass": (
            float(element.mass)
            if element.mass is not None
            else None
        ),
        "density": getattr(element, "density", None),
    }
