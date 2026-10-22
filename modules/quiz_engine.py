class QuizEngine:
    """
    Self-Assessment and Formula Practice Quiz for B.Tech Engineering Students.
    """

    QUESTIONS = [
        {
            "id": 1,
            "subject": "Engineering Mathematics",
            "question": "What is the condition for a square matrix A to possess a unique inverse A⁻¹?",
            "options": [
                "det(A) = 0 (Singular Matrix)",
                "det(A) ≠ 0 (Non-singular Matrix)",
                "Trace(A) = 0",
                "All diagonal elements must be 1"
            ],
            "correct_idx": 1,
            "explanation": "A matrix is invertible if and only if its determinant is non-zero (det(A) ≠ 0). If det(A) = 0, division by zero occurs in A⁻¹ = adj(A)/det(A)."
        },
        {
            "id": 2,
            "subject": "Engineering Mathematics",
            "question": "According to the Cayley-Hamilton Theorem, every square matrix A satisfies:",
            "options": [
                "Its own characteristic equation: P(A) = 0",
                "det(A) = Trace(A)",
                "A² = Identity Matrix",
                "Aᵀ = -A"
            ],
            "correct_idx": 0,
            "explanation": "The Cayley-Hamilton Theorem states that every square matrix satisfies its own characteristic polynomial equation |A - λI| = 0."
        },
        {
            "id": 3,
            "subject": "Engineering Physics",
            "question": "In Newton's Rings reflected light experiment, why is the central spot dark?",
            "options": [
                "Destructive interference occurs due to an extra π (180°) phase change upon reflection at the denser medium",
                "Constructive interference cancels the light",
                "The lens absorbs all incident wavelengths",
                "Light travels faster in the glass plate"
            ],
            "correct_idx": 0,
            "explanation": "At the point of contact, film thickness t = 0. An additional path difference of λ/2 (phase change of π) is introduced upon reflection at the top surface of the lower glass plate, causing destructive interference."
        },
        {
            "id": 4,
            "subject": "Engineering Physics",
            "question": "Bragg's Law of X-ray diffraction in crystal lattices is expressed as:",
            "options": [
                "2d sin(θ) = nλ",
                "d sin(θ) = 2nλ",
                "λ = 2d cos(θ)",
                "E = mc²"
            ],
            "correct_idx": 0,
            "explanation": "Bragg's Law states that constructive interference from crystal planes with interplanar spacing d occurs when the path difference 2d sin(θ) equals an integer multiple of the wavelength nλ."
        },
        {
            "id": 5,
            "subject": "Basic Electrical Engineering",
            "question": "In a series RLC circuit at resonance (f = f₀), what is the net circuit impedance Z?",
            "options": [
                "Z = R (Purely resistive, minimum impedance)",
                "Z = ∞ (Open circuit)",
                "Z = ωL + 1/(ωC)",
                "Z = 0"
            ],
            "correct_idx": 0,
            "explanation": "At resonance, inductive reactance equals capacitive reactance (X_L = X_C). They cancel each other out, leaving only the resistance: Z = R. Thus, current is at its maximum."
        },
        {
            "id": 6,
            "subject": "Classical Mechanics",
            "question": "If the velocity of an object is doubled, what happens to its kinetic energy?",
            "options": [
                "It quadruples (increases by 4x)",
                "It doubles (increases by 2x)",
                "It remains unchanged",
                "It decreases by half"
            ],
            "correct_idx": 0,
            "explanation": "Kinetic Energy is proportional to the square of velocity: KE = 0.5 × m × v². Doubling v results in (2v)² = 4v², so KE increases by 4 times."
        },
        {
            "id": 7,
            "subject": "Engineering Mathematics",
            "question": "The directional derivative of a scalar field f(x, y, z) in the direction of unit vector û is computed as:",
            "options": [
                "∇f · û (Dot product of Gradient and Unit Direction Vector)",
                "∇f × û (Cross product)",
                "|∇f| / |û|",
                "∂f/∂x + ∂f/∂y + ∂f/∂z"
            ],
            "correct_idx": 0,
            "explanation": "The directional derivative Duf = ∇f · û, which projects the maximum rate of change (the gradient) along the direction of interest."
        },
        {
            "id": 8,
            "subject": "Engineering Physics",
            "question": "The Hall coefficient R_H for an n-type semiconductor with electron concentration n is given by:",
            "options": [
                "R_H = -1 / (n · e)",
                "R_H = +1 / (n · e)",
                "R_H = n · e",
                "R_H = 0"
            ],
            "correct_idx": 0,
            "explanation": "For electrons as the majority carrier, the Hall coefficient is negative: R_H = -1 / (n · e)."
        }
    ]

    @staticmethod
    def get_all_questions():
        return QuizEngine.QUESTIONS
