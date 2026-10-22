class EngineeringConverter:
    """
    Unit Conversion and Fundamental Physical Constants Cheatsheet.
    """

    CONSTANTS = [
        {"symbol": "c", "name": "Speed of Light in Vacuum", "value": "2.99792 × 10⁸", "unit": "m/s", "category": "Electrodynamics"},
        {"symbol": "h", "name": "Planck Constant", "value": "6.62607 × 10⁻³⁴", "unit": "J·s", "category": "Quantum Physics"},
        {"symbol": "ħ", "name": "Reduced Planck Constant (h/2π)", "value": "1.05457 × 10⁻³⁴", "unit": "J·s", "category": "Quantum Physics"},
        {"symbol": "e", "name": "Elementary Charge", "value": "1.60218 × 10⁻¹⁹", "unit": "C", "category": "Electromagnetism"},
        {"symbol": "mₑ", "name": "Electron Rest Mass", "value": "9.10938 × 10⁻³¹", "unit": "kg", "category": "Atomic Physics"},
        {"symbol": "mₚ", "name": "Proton Rest Mass", "value": "1.67262 × 10⁻²⁷", "unit": "kg", "category": "Nuclear Physics"},
        {"symbol": "ε₀", "name": "Vacuum Permittivity", "value": "8.85419 × 10⁻¹²", "unit": "F/m", "category": "Electromagnetism"},
        {"symbol": "μ₀", "name": "Vacuum Permeability", "value": "1.25664 × 10⁻⁶", "unit": "H/m", "category": "Electromagnetism"},
        {"symbol": "k_B", "name": "Boltzmann Constant", "value": "1.38065 × 10⁻²³", "unit": "J/K", "category": "Thermodynamics"},
        {"symbol": "N_A", "name": "Avogadro Constant", "value": "6.02214 × 10²³", "unit": "mol⁻¹", "category": "Physical Chemistry"},
        {"symbol": "G", "name": "Gravitational Constant", "value": "6.67430 × 10⁻¹¹", "unit": "N·m²/kg²", "category": "Classical Mechanics"},
        {"symbol": "g", "name": "Standard Acceleration of Gravity", "value": "9.80665", "unit": "m/s²", "category": "Classical Mechanics"},
        {"symbol": "R", "name": "Universal Gas Constant", "value": "8.31446", "unit": "J/(mol·K)", "category": "Thermodynamics"},
    ]

    UNIT_CATEGORIES = {
        "Force": {
            "Newton (N)": 1.0,
            "Kilonewton (kN)": 1000.0,
            "Dyne (dyn)": 1e-5,
            "Pound-force (lbf)": 4.44822,
            "Kilogram-force (kgf)": 9.80665
        },
        "Energy": {
            "Joule (J)": 1.0,
            "Kilojoule (kJ)": 1000.0,
            "Electronvolt (eV)": 1.60218e-19,
            "Calorie (cal)": 4.184,
            "Kilocalorie (kcal)": 4184.0,
            "Kilowatt-hour (kWh)": 3.6e6,
            "British Thermal Unit (BTU)": 1055.06
        },
        "Pressure": {
            "Pascal (Pa)": 1.0,
            "Kilopascal (kPa)": 1000.0,
            "Megapascal (MPa)": 1e6,
            "Bar (bar)": 1e5,
            "Atmosphere (atm)": 101325.0,
            "Pound per sq inch (psi)": 6894.76,
            "Torr / mmHg": 133.322
        },
        "Length & Wavelength": {
            "Meter (m)": 1.0,
            "Centimeter (cm)": 0.01,
            "Millimeter (mm)": 1e-3,
            "Micrometer (µm)": 1e-6,
            "Nanometer (nm)": 1e-9,
            "Angstrom (Å)": 1e-10,
            "Picometer (pm)": 1e-12,
            "Inch (in)": 0.0254,
            "Foot (ft)": 0.3048
        },
        "Angle": {
            "Degrees (deg)": 1.0,
            "Radians (rad)": 57.2957795,
            "Gradians (grad)": 0.9
        }
    }

    @staticmethod
    def convert(category, val, from_unit, to_unit):
        """Converts value from one unit to another within standard factor base."""
        factors = EngineeringConverter.UNIT_CATEGORIES.get(category, {})
        if from_unit not in factors or to_unit not in factors:
            raise ValueError("Unsupported unit specified.")
        
        # Convert to base unit
        base_val = val * factors[from_unit]
        # Convert to target unit
        converted_val = base_val / factors[to_unit]
        return converted_val
