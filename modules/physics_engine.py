import math

class PhysicsEngine:
    """
    Physics Computation Engine supporting Classical Mechanics, Circuits,
    and JNTUK R23 Engineering Physics with step-by-step formula substitutions.
    """

    # --- CLASSICAL MECHANICS & BASIC PHYSICS ---

    @staticmethod
    def calculate_force(mass, acceleration):
        val = mass * acceleration
        derivation = f"F = m × a = {mass} kg × {acceleration} m/s² = {val:.4f} N"
        return round(val, 4), derivation

    @staticmethod
    def calculate_velocity(displacement, time):
        if time == 0:
            raise ValueError("Time cannot be zero!")
        val = displacement / time
        derivation = f"v = s / t = {displacement} m / {time} s = {val:.4f} m/s"
        return round(val, 4), derivation

    @staticmethod
    def calculate_acceleration(v_final, v_initial, time):
        if time == 0:
            raise ValueError("Time cannot be zero!")
        val = (v_final - v_initial) / time
        derivation = f"a = (v - u) / t = ({v_final} - {v_initial}) / {time} = {val:.4f} m/s²"
        return round(val, 4), derivation

    @staticmethod
    def calculate_momentum(mass, velocity):
        val = mass * velocity
        derivation = f"p = m × v = {mass} kg × {velocity} m/s = {val:.4f} kg·m/s"
        return round(val, 4), derivation

    @staticmethod
    def calculate_work(force, distance):
        val = force * distance
        derivation = f"W = F × d = {force} N × {distance} m = {val:.4f} J"
        return round(val, 4), derivation

    @staticmethod
    def calculate_power(work, time):
        if time == 0:
            raise ValueError("Time cannot be zero!")
        val = work / time
        derivation = f"P = W / t = {work} J / {time} s = {val:.4f} W"
        return round(val, 4), derivation

    @staticmethod
    def calculate_kinetic_energy(mass, velocity):
        val = 0.5 * mass * (velocity ** 2)
        derivation = f"KE = ½ m v² = 0.5 × {mass} × ({velocity})² = {val:.4f} J"
        return round(val, 4), derivation

    @staticmethod
    def calculate_pressure(force, area):
        if area == 0:
            raise ValueError("Area cannot be zero!")
        val = force / area
        derivation = f"P = F / A = {force} N / {area} m² = {val:.4f} Pa"
        return round(val, 4), derivation

    @staticmethod
    def calculate_density(mass, volume):
        if volume == 0:
            raise ValueError("Volume cannot be zero!")
        val = mass / volume
        derivation = f"ρ = m / V = {mass} kg / {volume} m³ = {val:.4f} kg/m³"
        return round(val, 4), derivation

    @staticmethod
    def calculate_ohms_law(current, resistance):
        val = current * resistance
        derivation = f"V = I × R = {current} A × {resistance} Ω = {val:.4f} V"
        return round(val, 4), derivation

    # --- JNTUK R23 ENGINEERING PHYSICS METHODS ---

    @staticmethod
    def thin_film_refractive_index(lambda_nm, t_nm, n_order):
        if t_nm <= 0:
            raise ValueError("Film thickness must be positive.")
        mu = (n_order * lambda_nm) / (2 * t_nm)
        derivation = f"μ = (n × λ) / (2t) = ({n_order} × {lambda_nm} nm) / (2 × {t_nm} nm) = {mu:.4f}"
        return round(mu, 4), derivation

    @staticmethod
    def newtons_rings_radius_curvature(D_n_plus_m, D_n, m_rings, lambda_nm):
        if m_rings <= 0 or lambda_nm <= 0:
            raise ValueError("Rings count m and wavelength must be greater than zero.")
        lam_m = lambda_nm * 1e-9
        D2 = (D_n_plus_m * 1e-2)**2
        D1 = (D_n * 1e-2)**2
        R = (D2 - D1) / (4 * m_rings * lam_m)
        derivation = (
            f"R = (Dₙ₊ₘ² - Dₙ²) / (4 · m · λ)\n"
            f"  = ({D_n_plus_m} cm² - {D_n} cm²) / (4 × {m_rings} × {lambda_nm} nm)\n"
            f"  = {R:.4f} m ({R*100:.2f} cm)"
        )
        return round(R, 4), derivation

    @staticmethod
    def interplanar_spacing(a_angstrom, h, k, l):
        denom = math.sqrt(h**2 + k**2 + l**2)
        if denom == 0:
            raise ValueError("Miller indices (h,k,l) cannot all be zero.")
        d = a_angstrom / denom
        derivation = f"d = a / √(h² + k² + l²) = {a_angstrom} / √({h}² + {k}² + {l}²) = {a_angstrom} / {denom:.4f} = {d:.4f} Å"
        return round(d, 4), derivation

    @staticmethod
    def bragg_law_wavelength(d_angstrom, theta_deg, n_order=1):
        theta_rad = math.radians(theta_deg)
        lam = (2 * d_angstrom * math.sin(theta_rad)) / n_order
        derivation = f"λ = (2d sin θ) / n = (2 × {d_angstrom} × sin({theta_deg}°)) / {n_order} = {lam:.4f} Å"
        return round(lam, 4), derivation

    @staticmethod
    def quantum_particle_box_energy(n_quantum, L_nm):
        if L_nm <= 0:
            raise ValueError("Box width L must be greater than 0.")
        h, m_e = 6.626e-34, 9.109e-31
        L_m = L_nm * 1e-9
        E_joules = (n_quantum**2 * h**2) / (8 * m_e * L_m**2)
        E_ev = E_joules / 1.602e-19
        derivation = (
            f"Eₙ = (n² h²) / (8 m L²)\n"
            f"   = ({n_quantum}² × (6.626×10⁻³⁴)²) / (8 × 9.109×10⁻³¹ × ({L_nm}×10⁻⁹)²)\n"
            f"   = {E_joules:.4e} J = {E_ev:.4f} eV"
        )
        return round(E_ev, 4), derivation

    @staticmethod
    def hall_coefficient(carrier_density_m3):
        if carrier_density_m3 <= 0:
            raise ValueError("Carrier density must be positive.")
        rh = 1.0 / (carrier_density_m3 * 1.602e-19)
        derivation = f"R_H = 1 / (n × e) = 1 / ({carrier_density_m3:.2e} × 1.602×10⁻¹⁹) = {rh:.4e} m³/C"
        return rh, derivation
