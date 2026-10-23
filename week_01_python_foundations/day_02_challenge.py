##GOAL: teaching Python how to interpret chemical formulas.

print("Welcome to the chemical formula interpreter!")

"""
COMPUTATIONAL CHEMISTRY: WEEK 1 — DAY 2
TASK 1: READING CHEMICAL FORMULAS
CHALLENGE 1 OF 4: THE CHEMICAL FORMULA INSPECTOR

CHALLENGE
A chemistry laboratory receives chemical formulas as text.
Write a Python program that inspects a chemical formula and
reports basic information about its characters.

Starting formula: C12H22O11

REQUIREMENTS
1. Store the chemical formula in a variable.
2. Print the original formula.
3. Print the total number of characters.
4. Display each character alongside its position.
5. Identify whether each character is a digit.
6. Count and print the total number of digit characters.

CONSTRAINTS
- Use meaningful variable names.
- Use a loop to inspect the characters.
- Do not hardcode individual character positions.
- Your program should also work with H2O, NaCl and Ca(OH)2.
- Do not calculate molecular mass in this challenge.

CONCEPTS TO PRACTISE
Strings, indexing, len(), loops, conditionals and isdigit().

THINK BEFORE YOU CODE
1. Why is a chemical formula stored as a string?
2. How can you access an individual character?
3. How can you check whether a character is a digit?
4. How can you count digits without hardcoding the answer?

EXPECTED OUTCOME
Display the formula, character count, each character and its
position, whether each character is a digit, and the total
number of digit characters.
"""

# MY SOLUTION
# Write your code below.

formular =  "Ca(OH)2"  #"H2O"  #"C12H22O11"
print(len(formular))
counter = 0
for index,char in enumerate(formular):
    print(f"POSITION: {index},{char}, {char.isdigit()}")
    if char.isdigit():

        counter = counter + 1

print(counter)


# formula = "H2O"
# digit_counter = 0

# for char in formular:
#    if char.isdigit() :
#       digit_counter = digit_counter + 1
# #    print(digit_counter)
# print(digit_counter)

# for char,ind in enumerate(formula):
#    print(ind, char)

# for i in range(len(formula)):
#    print(formula[i], i, formula[i].isdigit())


"""
# CHALLENGE 2: THE ELEMENT AND SUBSCRIPT EXTRACTOR

# PROBLEM
# Write a Python program that reads a simple chemical formula
# and identifies each element symbol and its numerical subscript.

# Examples:
# H2O  -> H: 2, O: 1
# NaCl -> Na: 1, Cl: 1
# C12H22O11 -> C: 12, H: 22, O: 11

# REQUIREMENTS
# 1. Store a chemical formula as a string.
# 2. Identify element symbols.
# 3. Recognise that an uppercase letter starts an element symbol.
# 4. Recognise that a lowercase letter may follow an uppercase
#    letter to complete a two-character symbol.
# 5. Read one-digit and multi-digit subscripts.
# 6. If an element has no subscript, assign it a count of 1.
# 7. Display each element and its atom count.

# CONSTRAINTS
# - Use loops, conditionals and string operations.
# - Do not hardcode the element symbols for each formula.
# - Do not calculate molecular mass yet.
# - For this challenge, formulas will contain element symbols
#   and subscripts only. Parentheses are not required yet.

# CONCEPTS TO PRACTISE
# - Uppercase and lowercase character recognition
# - String indexing
# - Building strings character by character
# - Converting digit strings to integers
# - Tracking information while processing a string

# THINK BEFORE YOU CODE
# 1. How can you recognise an uppercase letter?
# 2. How can you tell whether the next character belongs
#    to the current element symbol?
# 3. How can you collect the digits in a subscript such as 12?
# 4. What should happen when an element has no subscript?

# EXPECTED OUTCOME
# For C12H22O11, your program should identify:
# C: 12
# H: 22
# O: 11
# """

# MY SOLUTION
# Write your code below.
formula = "C12H22O11"

elements = {}
symbol = ""
number = ""

for char in formula:

    if char.isupper():
        # Save the previous element before starting another
        if symbol:
            count = int(number) if number else 1
            elements[symbol] = count

        symbol = char
        number = ""

    elif char.islower():
        # Add lowercase letter to complete the symbol
        symbol += char

    elif char.isdigit():
        # Collect consecutive digits into one number
        number += char

# Save the final element
if symbol:
    count = int(number) if number else 1
    elements[symbol] = count

# Display the results
print(f"Chemical formula: {formula}")
print("\nElement | Atom count")
print("--------------------")

for element, count in elements.items():
    print(f"{element:^7} | {count:^10}")



"""
TASK 3: CHEMICAL FORMULA MASS CALCULATOR

Objective:
Parse a chemical formula, count its atoms, look up atomic
masses, and calculate the total molar mass.

Requirements:
1. Identify element symbols and numerical subscripts.
2. Assign a count of 1 when no subscript is written.
3. Look up atomic masses in a dictionary.
4. Calculate each element's contribution.
5. Display the total molar mass.
6. Handle unsupported elements.

Scope: Formulas without parentheses.
"""

# 1. Store atomic masses in a dictionary
atomic_masses = {
    "H": 1.008,
    "C": 12.011,
    "O": 15.999,
    "Na": 22.990,
    "Cl": 35.450,
    "Ca": 40.078
}


# 2. Create a function to parse the chemical formula
def parse_formula(formula):
    elements = {}
    symbol = ""
    number = ""

    for char in formula:

        if char.isupper():
            # Save the previous element
            if symbol:
                count = int(number) if number else 1
                elements[symbol] = count

            # Start a new element
            symbol = char
            number = ""

        elif char.islower():
            # Complete a two-character element symbol
            symbol += char

        elif char.isdigit():
            # Collect consecutive digits
            number += char

        else:
            raise ValueError(
                f"Unsupported character in formula: {char}"
            )

    # Save the final element
    if symbol:
        count = int(number) if number else 1
        elements[symbol] = count

    if not elements:
        raise ValueError("Please enter a chemical formula.")

    return elements


# 3. Create a function to calculate molar mass
def calculate_molar_mass(formula):
    elements = parse_formula(formula)
    total_mass = 0

    print(f"\nChemical formula: {formula}")
    print("\nElement | Atoms | Atomic mass | Contribution")
    print("-" * 51)

    for element, count in elements.items():

        # Check whether the element has a known atomic mass
        if element not in atomic_masses:
            raise ValueError(
                f"Atomic mass for '{element}' is not available."
            )

        atomic_mass = atomic_masses[element]
        contribution = count * atomic_mass
        total_mass += contribution

        print(
            f"{element:^7} | {count:^5} | "
            f"{atomic_mass:^11.3f} | {contribution:^12.3f}"
        )

    print("-" * 51)
    print(f"Total molar mass: {total_mass:.3f} g/mol")

    return total_mass


# 4. Ask the user for a formula and calculate its molar mass
formula = input("Enter a chemical formula: ").strip()

try:
    calculate_molar_mass(formula)

except ValueError as error:
    print(f"Error: {error}")
