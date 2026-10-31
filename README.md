# ⚗️ ChemWise — A Smart Chemistry Toolkit

**ChemWise** is a Python-powered chemistry toolkit built with [Streamlit](https://streamlit.io/) to make essential chemistry calculations easier, faster, and more accessible.

Designed for chemistry students, educators, and science enthusiasts, ChemWise provides an interactive platform for solving common chemistry problems, understanding calculation procedures, and retrieving basic chemical element information.

## ✨ Features

ChemWise currently includes seven functional chemistry tools:

| Tool | Description |
|---|---|
| **Molar Mass Calculator** | Calculates the molar mass of chemical compounds from their molecular formulas. |
| **Percentage Composition Calculator** | Determines the percentage by mass of each element in a compound. |
| **Mass to Moles Converter** | Converts a given mass into the corresponding number of moles. |
| **Moles to Mass Converter** | Calculates the mass corresponding to a specified number of moles. |
| **Moles to Particles Converter** | Converts moles into the number of representative particles using Avogadro's constant. |
| **Particles to Moles Converter** | Converts the number of representative particles into moles. |
| **Element Information Lookup** | Retrieves basic information about chemical elements, including atomic number, atomic mass, and density where available. |

### 🎨 User Interface

- Clean, modern and responsive interface.
- Light and dark themes.
- Interactive calculation forms.
- Structured calculation results.
- Modular and reusable application components.

## 🛠️ Technology Stack

- **Python** — Core programming language.
- **Streamlit** — Interactive web application framework.
- **periodictable** — Chemical element and atomic mass data.
- **Pytest** — Automated testing framework.
- **CSS** — Custom interface styling.

## 📁 Project Structure

```text
chemwise_calculator_app/
│
├── app.py
│
├── calculations/
│   ├── __init__.py
│   ├── element_data.py
│   ├── molar_mass.py
│   └── stoichiometry.py
│
├── components/
│   ├── __init__.py
│   ├── header.py
│   ├── result_cards.py
│   └── sidebar.py
│
├── styles/
│   ├── __init__.py
│   ├── main.css
│   └── theme.py
│
├── tests/
│   ├── __init__.py
│   └── test_calculations.py
│
├── week_01_python_foundations/
│
├── requirements.txt
├── README.md
└── .gitignore
```

The application follows a modular structure, separating calculation logic, interface components, styling, and automated tests.

## 🚀 Installation and Setup

Follow these steps to run ChemWise locally.

### 1. Clone the repository

```bash
git clone https://github.com/AminaAdenuga/chemwise_calculator_app.git
```

### 2. Navigate into the project directory

```bash
cd chemwise_calculator_app
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application
