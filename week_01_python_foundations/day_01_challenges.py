print("Computational Chemistry: Week 1")
print("My problem-solving journey begins.")

#challenge one
##Challenge 1: The chemical sample register
##A laboratory receives a sample with the following information:
##- Sample ID: HCL-001
##- Chemical: Hydrochloric acid
##- Concentration: 0.50 mol/L
##- Volume: 250 mL
##- Temperature: 27 °C
##Your task: Write a Python program that stores each piece of information in an appropriate variable and prints a readable sample report.

##Constraints:
##- Use at least five variables.
##- Use meaningful variable names.
##- Store numerical quantities as numbers, not as text.
##- Print all the information in a readable format.
##Think before you code: Which values should be strings, and which should be integers or floating-point numbers? Why?


sample_ID = "HCL-001"
chemical_name = "Hydrochloric Acid"
concentration_value = 0.50
concentration_molL = "mol/L"
volume_value = 250
volume_ml ="ml"
temperature_value = 27
temperature_unit = "°C"

##to write a sample report

print(f"A {chemical_name} sample identified as {sample_ID} was recorded with a reported concentration of {concentration_value} {concentration_molL}, a volume of {volume_value} {volume_ml}, and a temperature of {temperature_value} {temperature_unit}.")

# convert ml to l and reassign 

volume_value_l = volume_value/1000
volume_l = "L"

print(f"The volume of the sample in ml is {volume_value}{volume_ml} and in L is {volume_value_l} {volume_l}.")

##challenge two
##Challenge 2: The dilution calculation
##Easy
##A chemist has 100 mL of a 2.0 mol/L stock solution and wants to prepare a solution with a concentration of 0.50 mol/L.

##Use the dilution relationship: C1VI=C2V2, where C1 is the initial concentration, V1 is the initial volume, C2 is the final concentration, and V2 is the final volume.

##Your task: Write a program that calculates the final volume required and the volume of water to add, assuming volumes are additive for this calculation.

##Before coding, identify:
##- The known quantities.
##- The unknown quantity.
##- The equation you need to rearrange.
##- The units you will use.
##Then test your answer for physical and mathematical reasonableness. Should the final volume be larger or smaller than the initial volume?

initial_concentration_values = {
    "value": 2.0,
    "unit": "mol/L"
}
final_concentration_values = {
    "value": 0.50,
    "unit": "mol/L"
}
initial_volume_values = {
    "value": 100,
    "unit": "mL"
}

final_volume_values = {
    "value": initial_concentration_values["value"] * initial_volume_values["value"] / final_concentration_values["value"],
    "unit": initial_volume_values["unit"]
}
print(final_volume_values["value"], final_volume_values["unit"])

volume_water = final_volume_values["value"] - initial_volume_values["value"]
print(f"The volume of water needed to dilute the solution is {volume_water} {final_volume_values['unit']}.")

## challenge 03
##Challenge 3: The Laboratory Report
##A chemist has measured the pH of three aqueous samples in the laboratory.
##Sample ID	Sample name	pH
##PH-001	Distilled Water	7.0
##PH-002	Acidic Solution	3.5
##PH-003	Alkaline Solution	9.2

##Your task is to write a Python program that stores these measurements and prints a clear laboratory report.
##Your tasks
##Task 1 — Store the data

##Create variables for each sample's ID, name and pH. You can decide how to organise them based on what you learned in Challenges 1 and 2.

##Task 2 — Print the report
##Task 3 — Add a calculation

##Calculate the difference between the highest and lowest pH measurements.

##Print the result with a clear description.

sample_A = {
    "sample_ID": "PH-001",
    "sample_name": "Distilled Water",
    "PH_value": 7.0,
}
sample_B = {
    "sample_ID": "PH-002",
    "sample_name": "Acidic solution",
    "PH_value": 3.5,
}
sample_c = {
    "sample_ID": "PH-003",
    "sample_name": "Alkaline Solution",
    "PH_value": 9.2,
}

print(f"\nLaboratory pH Report \nSample: {sample_A['sample_ID']}  \nName: {sample_A['sample_name']}  \npH Value: {sample_A['PH_value']}.\nSample: {sample_B['sample_ID']}  \nName: {sample_B['sample_name']}  \npH Value: {sample_B['PH_value']}.\nSample: {sample_c['sample_ID']}  \nName: {sample_c['sample_name']}  \npH Value: {sample_c['PH_value']}.")

ph_difference_B = sample_c["PH_value"] - sample_B["PH_value"]
ph_difference_BC = round(ph_difference_B, 2)
print(f"\nThe difference in pH between the highest pH of {sample_c['sample_name']} and lowest ph of {sample_B['sample_name']} is {ph_difference_BC}.")

##challenge 4
##Challenge 4: The molar mass calculator
##Moderate
##A student needs to calculate the molar mass of calcium hydroxide, {Ca(OH)_2}

##Use these atomic masses:
##Element	Atomic mass (g/mol)
##Ca	40.078
##O	15.999
##H	1.008

##Your program must calculate the molar mass using variables and arithmetic operators.

##The reasoning trap: The formula contains two hydroxide groups. You must account for the number of atoms of each element.

##Your tasks:
##1. Represent the atomic masses in variables.
##2. Express the chemical formula mathematically.
##3. Calculate the molar mass.
##4. Print the result with its unit.]

element_1 = {
    "name": "Calcium",
    "symbol": "Ca",
    "atomic_number": 20,
    "atomic_mass": 40.078
}
element_2 = {
    "name": "Oxygen",
    "symbol": "O",
    "atomic_number": 8,
    "atomic_mass": 15.999
}
element_3 = {
    "name": "Hydrogen",
    "symbol": "H",
    "atomic_number": 1,
    "atomic_mass": 1.008
}

molar_mass_caOH2 = round(element_1["atomic_mass"] + 2*(element_2["atomic_mass"] + element_3["atomic_mass"]), 3)
print(f"\nThe molar mass of {element_1['name']} hydroxide (Ca(OH)2) is {molar_mass_caOH2} g/mol.")

##KEY TAKEAWAYS   
#Store structured data, perform calculations, apply chemical equations, format reports, and combine arithmetic with chemical reasoning.