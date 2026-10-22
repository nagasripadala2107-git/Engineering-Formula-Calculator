import re

class RuleBasedAIEngine:
    """
    Rule-Based Natural Language Query Processing & Engineering AI Assistant.
    Aligned with JNTUK B.Tech R23 Regulation Syllabus across Mathematics,
    Physics, and Electrical & Mechanical Engineering.
    """

    def __init__(self):
        self.rules = [
            # --- LA&C UNIT I: MATRICES ---
            {
                "id": "echelon_rank",
                "category": "LA&C (Unit I: Matrices)",
                "name": "Matrix Rank (Echelon Form)",
                "keywords": ["rank", "echelon", "echelon form", "row echelon", "non zero rows"],
                "formula": "Rank(A) = Number of non-zero rows in row-echelon form",
                "explanation": "Perform elementary row operations to reduce the matrix to upper triangular echelon form. Count the rows that contain at least one non-zero entry."
            },
            {
                "id": "matrix_inverse",
                "category": "LA&C (Unit I: Matrices)",
                "name": "Matrix Inverse & Adjugate",
                "keywords": ["inverse", "invertible", "adjugate", "cofactor", "determinant inverse"],
                "formula": "A⁻¹ = adj(A) / det(A),  where det(A) ≠ 0",
                "explanation": "Compute the determinant. If det(A) ≠ 0, compute the cofactor matrix, transpose it to obtain adj(A), and divide by det(A)."
            },
            {
                "id": "gauss_jordan",
                "category": "LA&C (Unit I: Matrices)",
                "name": "Gauss-Jordan Matrix Inversion",
                "keywords": ["gauss jordan", "augmented matrix", "identity matrix", "row operations"],
                "formula": "[A | I]  --> [I | A⁻¹]",
                "explanation": "Augment matrix A with Identity matrix I and apply elementary row operations until the left block becomes I."
            },
            {
                "id": "gauss_seidel",
                "category": "LA&C (Unit I: Matrices)",
                "name": "Gauss-Seidel Iteration Method",
                "keywords": ["gauss seidel", "seidel", "jacobi", "iteration", "linear equations"],
                "formula": "x_i^(k+1) = (1/a_ii) * [ b_i - sum_{j<i} a_ij*x_j^(k+1) - sum_{j>i} a_ij*x_j^(k) ]",
                "explanation": "Iterative numerical solver for strictly diagonally dominant linear systems where updated values are used immediately."
            },

            # --- LA&C UNIT II: EIGENVALUES ---
            {
                "id": "eigenvalues",
                "category": "LA&C (Unit II: Eigenvalues)",
                "name": "Eigenvalues & Characteristic Equation",
                "keywords": ["eigenvalue", "eigenvalues", "eigenvector", "characteristic equation", "characteristic polynomial"],
                "formula": "det(A - λ·I) = 0",
                "explanation": "The characteristic polynomial roots provide the eigenvalues λ. Solve (A - λ·I)X = 0 to obtain the corresponding eigenvectors X."
            },
            {
                "id": "cayley_hamilton",
                "category": "LA&C (Unit II: Eigenvalues)",
                "name": "Cayley-Hamilton Theorem",
                "keywords": ["cayley hamilton", "cayley", "power of matrix", "inverse using cayley"],
                "formula": "P(A) = Aⁿ + c_{n-1}·Aⁿ⁻¹ + ... + c₀·I = 0",
                "explanation": "Every square matrix satisfies its own characteristic equation. Multiplying by A⁻¹ provides a powerful method to compute matrix inverses and higher matrix powers."
            },

            # --- LA&C UNIT III & IV: CALCULUS & VECTOR CALCULUS ---
            {
                "id": "directional_derivative",
                "category": "LA&C (Unit IV: Vector Calculus)",
                "name": "Directional Derivative & Gradient",
                "keywords": ["directional derivative", "gradient", "grad f", "rate of change in direction"],
                "formula": "D_u f = ∇f · û,  where û = v / ||v||",
                "explanation": "Computes the projection of the gradient vector ∇f onto the unit direction vector û. Maximum rate of change occurs in the direction of ∇f."
            },
            {
                "id": "jacobian",
                "category": "LA&C (Unit III: Multivariable Calculus)",
                "name": "Jacobian Determinant",
                "keywords": ["jacobian", "variable transformation", "partial derivatives determinant"],
                "formula": "J = ∂(u,v)/∂(x,y) = (∂u/∂x)(∂v/∂y) - (∂u/∂y)(∂v/∂x)",
                "explanation": "Measures the local scale factor and coordinate deformation when changing variables in multiple integrals."
            },

            # --- PHYSICS: WAVE OPTICS & CRYSTALLOGRAPHY ---
            {
                "id": "newtons_rings",
                "category": "Engineering Physics (Wave Optics)",
                "name": "Newton's Rings (Radius of Curvature)",
                "keywords": ["newton's rings", "newton rings", "radius of curvature", "interference ring", "fringe diameter"],
                "formula": "R = (Dₙ₊ₘ² - Dₙ²) / (4·m·λ)",
                "explanation": "Formed by optical interference between reflected light rays from the spherical lens surface and the planar glass plate."
            },
            {
                "id": "bragg_law",
                "category": "Engineering Physics (Crystallography)",
                "name": "Bragg's Law of X-Ray Diffraction",
                "keywords": ["bragg", "bragg's law", "diffraction", "crystal lattice", "interplanar spacing"],
                "formula": "2·d·sin(θ) = n·λ",
                "explanation": "Condition for constructive interference of X-rays scattered from parallel atomic crystal planes separated by spacing d."
            },
            {
                "id": "interplanar_spacing",
                "category": "Engineering Physics (Crystallography)",
                "name": "Interplanar Spacing (d_hkl)",
                "keywords": ["interplanar", "miller indices", "hkl", "spacing", "lattice constant"],
                "formula": "d = a / √(h² + k² + l²)",
                "explanation": "Calculates the perpendicular distance between successive parallel lattice planes in a cubic crystal with lattice constant a."
            },
            {
                "id": "quantum_box",
                "category": "Engineering Physics (Quantum Mechanics)",
                "name": "Particle in a 1D Potential Box",
                "keywords": ["particle in box", "quantum well", "energy levels", "wavefunction", "planck"],
                "formula": "Eₙ = (n²·h²) / (8·m·L²)",
                "explanation": "Quantized energy eigenvalues of a trapped particle inside an infinite potential well of width L."
            },
            {
                "id": "hall_effect",
                "category": "Engineering Physics (Semiconductors)",
                "name": "Hall Effect & Hall Coefficient",
                "keywords": ["hall effect", "hall coefficient", "carrier concentration", "charge density"],
                "formula": "R_H = 1 / (n·e)",
                "explanation": "Generation of a transverse voltage across a current-carrying conductor placed in a magnetic field; used to determine charge carrier type and concentration."
            },

            # --- ELECTRICAL & ELECTRONICS (BEEE) ---
            {
                "id": "rlc_resonance",
                "category": "Basic Electrical Engineering (AC Circuits)",
                "name": "Series RLC Resonance & Quality Factor",
                "keywords": ["rlc", "resonance", "resonant frequency", "quality factor", "q factor", "impedance"],
                "formula": "f₀ = 1 / (2π√(LC)),   Q = (ω₀·L) / R",
                "explanation": "Condition where inductive reactance cancels capacitive reactance (X_L = X_C), causing minimum impedance Z = R and peak circuit current."
            },
            {
                "id": "voltage_divider",
                "category": "Basic Electrical Engineering (Circuits)",
                "name": "Voltage Divider Rule",
                "keywords": ["voltage divider", "potential divider", "v out", "series resistors"],
                "formula": "V_out = V_in × [ R₂ / (R₁ + R₂) ]",
                "explanation": "Calculates the distributed voltage dropped across a particular series resistor relative to the total circuit resistance."
            },
            {
                "id": "star_delta",
                "category": "Basic Electrical Engineering (Networks)",
                "name": "Star-Delta (Y-Δ) Transformation",
                "keywords": ["star delta", "wye delta", "y to delta", "three phase network"],
                "formula": "R_ab = (Ra·Rb + Rb·Rc + Rc·Ra) / Rc",
                "explanation": "Circuit equivalence transformation simplifying complex three-phase or bridge resistor topologies."
            },

            # --- MECHANICAL ENGINEERING ---
            {
                "id": "stress_strain",
                "category": "Mechanical Engineering (Mechanics of Solids)",
                "name": "Stress, Strain & Young's Modulus",
                "keywords": ["stress", "strain", "young's modulus", "elasticity", "hooke's law"],
                "formula": "σ = F / A,   ε = ΔL / L₀,   E = σ / ε",
                "explanation": "Hooke's Law relationship describing linear elastic deformation of materials under tensile or compressive mechanical loads."
            },
            {
                "id": "carnot_efficiency",
                "category": "Mechanical Engineering (Thermodynamics)",
                "name": "Carnot Heat Engine Efficiency",
                "keywords": ["carnot", "efficiency", "heat engine", "thermodynamics", "kelvin"],
                "formula": "η = 1 - (T_cold / T_hot)",
                "explanation": "The maximum theoretical thermodynamic efficiency achievable by any heat engine operating between two temperatures T_hot and T_cold."
            },
            {
                "id": "curve_fitting",
                "category": "Experimental Physics & Numerical Analysis",
                "name": "Linear Regression & Curve Fitting (Least Squares)",
                "keywords": ["linear regression", "curve fitting", "least squares", "trendline", "slope", "r squared", "r2"],
                "formula": "y = mx + c,   m = (N·Σxy - Σx·Σy)/(N·Σx² - (Σx)²),   c = (Σy - m·Σx)/N",
                "explanation": "Statistical technique minimizing the sum of squared vertical offsets from experimental data points to determine the optimal line of best fit and R²."
            },
            {
                "id": "fourier_series",
                "category": "LA&C (Unit V: Fourier Series)",
                "name": "Fourier Series Waveform Synthesis",
                "keywords": ["fourier", "fourier series", "harmonics", "gibbs phenomenon", "square wave", "sawtooth"],
                "formula": "f(t) = a₀/2 + Σ [aₙ cos(nωt) + bₙ sin(nωt)]",
                "explanation": "Decomposes any periodic signal into an infinite sum of sinusoidal harmonics with orthogonal basis frequencies."
            },
            {
                "id": "beam_sfd_bmd",
                "category": "Structural Mechanics (Civil & Mechanical)",
                "name": "Beam Shear Force & Bending Moment (SFD & BMD)",
                "keywords": ["sfd", "bmd", "shear force", "bending moment", "simply supported", "udl", "point load"],
                "formula": "V(x) = dM/dx,   M_max = (P·a·b)/L (Point Load) or (w·L²)/8 (UDL)",
                "explanation": "Diagrammatic determination of internal shear forces and bending moments along a structural beam under external loading."
            },
            {
                "id": "vibration_ode",
                "category": "Mechanical Vibrations & ODEs",
                "name": "Spring-Mass-Damper Vibration Dynamics",
                "keywords": ["vibration", "spring mass damper", "damping ratio", "natural frequency", "underdamped", "overdamped", "ode"],
                "formula": "m·x''(t) + c·x'(t) + k·x(t) = 0,   ωₙ = √(k/m),   ζ = c / (2√(mk))",
                "explanation": "Second-order linear differential equation governing damped free mechanical oscillations and critical damping limits."
            }
        ]

    def process_query(self, query):
        """Matches student natural language query against rules and scores keyword overlaps."""
        if not query or len(query.strip()) < 2:
            return None, "Please enter a question or engineering topic."

        clean_query = query.lower()
        best_match = None
        max_score = 0

        for rule in self.rules:
            score = 0
            # Check keywords
            for kw in rule["keywords"]:
                if kw in clean_query:
                    score += len(kw.split()) * 2

            # Check rule name
            for word in rule["name"].lower().split():
                if len(word) > 3 and word in clean_query:
                    score += 1

            if score > max_score:
                max_score = score
                best_match = rule

        if best_match and max_score >= 2:
            confidence = min(98, 40 + max_score * 15)
            msg = f"Match Confidence: {confidence}% (Matched via JNTUK R23 Rule Engine)"
            return best_match, msg

        return None, "No exact formula match found. Try typing keywords like 'Eigenvalues', 'Bragg', 'Newton Rings', 'RLC Resonance', 'Rank', or 'Carnot'."
