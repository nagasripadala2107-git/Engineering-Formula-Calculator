import math

class EngineeringDisciplineEngine:
    """
    Computational engine covering Electrical & Electronics Engineering (BEEE)
    and Mechanical Engineering fundamentals.
    """

    # --- BASIC ELECTRICAL & ELECTRONICS (BEEE) ---

    @staticmethod
    def resistor_combination(r_list, connection_type="series"):
        """Calculates equivalent resistance for Series or Parallel combinations."""
        if not r_list or any(r <= 0 for r in r_list):
            raise ValueError("All resistance values must be positive non-zero numbers.")
        
        if connection_type.lower() == "series":
            req = sum(r_list)
            steps = " + ".join([f"{r}Ω" for r in r_list])
            explanation = f"R_eq = {steps} = {req:.4f} Ω"
            return round(req, 4), explanation
        else:
            reciprocal_sum = sum(1.0 / r for r in r_list)
            req = 1.0 / reciprocal_sum
            steps = " + ".join([f"(1/{r})" for r in r_list])
            explanation = f"1/R_eq = {steps} = {reciprocal_sum:.4f} S  ==>  R_eq = {req:.4f} Ω"
            return round(req, 4), explanation

    @staticmethod
    def capacitor_combination(c_list, connection_type="series"):
        """Calculates equivalent capacitance for Series or Parallel combinations."""
        if not c_list or any(c <= 0 for c in c_list):
            raise ValueError("All capacitance values must be positive non-zero numbers.")
        
        if connection_type.lower() == "parallel":
            ceq = sum(c_list)
            steps = " + ".join([f"{c}µF" for c in c_list])
            explanation = f"C_eq = {steps} = {ceq:.4f} µF"
            return round(ceq, 4), explanation
        else:
            reciprocal_sum = sum(1.0 / c for c in c_list)
            ceq = 1.0 / reciprocal_sum
            steps = " + ".join([f"(1/{c})" for c in c_list])
            explanation = f"1/C_eq = {steps} ==> C_eq = {ceq:.4f} µF"
            return round(ceq, 4), explanation

    @staticmethod
    def voltage_divider(v_in, r1, r2):
        """Calculates output voltage across R2 in a 2-resistor voltage divider."""
        if r1 <= 0 or r2 <= 0:
            raise ValueError("Resistor values must be greater than zero.")
        v_out = v_in * (r2 / (r1 + r2))
        derivation = f"V_out = V_in × [ R₂ / (R₁ + R₂) ] = {v_in} × [ {r2} / ({r1} + {r2}) ] = {v_out:.4f} V"
        return round(v_out, 4), derivation

    @staticmethod
    def current_divider(i_total, r1, r2):
        """Calculates current through R1 and R2 in parallel."""
        if r1 <= 0 or r2 <= 0:
            raise ValueError("Resistor values must be greater than zero.")
        i1 = i_total * (r2 / (r1 + r2))
        i2 = i_total * (r1 / (r1 + r2))
        derivation = (
            f"I₁ = I_total × [ R₂ / (R₁ + R₂) ] = {i_total} × [{r2}/({r1}+{r2})] = {i1:.4f} A\n"
            f"I₂ = I_total × [ R₁ / (R₁ + R₂) ] = {i_total} × [{r1}/({r1}+{r2})] = {i2:.4f} A"
        )
        return round(i1, 4), round(i2, 4), derivation

    @staticmethod
    def rlc_resonance_parameters(r_ohm, l_henry, c_farad):
        """Computes resonant frequency f0, angular frequency omega0, and quality factor Q."""
        if l_henry <= 0 or c_farad <= 0 or r_ohm <= 0:
            raise ValueError("L, C, and R must all be strictly positive.")
        omega0 = 1.0 / math.sqrt(l_henry * c_farad)
        f0 = omega0 / (2.0 * math.pi)
        q = (omega0 * l_henry) / r_ohm
        bandwidth = f0 / q if q > 0 else 0
        derivation = (
            f"ω₀ = 1 / √(LC) = {omega0:.2f} rad/s\n"
            f"f₀ = ω₀ / (2π) = {f0:.2f} Hz\n"
            f"Quality Factor Q = (ω₀ × L) / R = {q:.2f}\n"
            f"Bandwidth Δf = f₀ / Q = {bandwidth:.2f} Hz"
        )
        return round(f0, 2), round(q, 2), round(bandwidth, 2), derivation

    @staticmethod
    def star_to_delta(ra, rb, rc):
        """Converts Star (Y) network resistances (Ra, Rb, Rc connected to neutral) to Delta (Rab, Rbc, Rca)."""
        if any(r <= 0 for r in [ra, rb, rc]):
            raise ValueError("All Star resistor values must be positive.")
        sum_products = (ra * rb) + (rb * rc) + (rc * ra)
        rab = sum_products / rc
        rbc = sum_products / ra
        rca = sum_products / rb
        derivation = (
            f"Numerator = (Ra·Rb + Rb·Rc + Rc·Ra) = {sum_products:.2f}\n"
            f"R_ab = Numerator / Rc = {rab:.4f} Ω\n"
            f"R_bc = Numerator / Ra = {rbc:.4f} Ω\n"
            f"R_ca = Numerator / Rb = {rca:.4f} Ω"
        )
        return round(rab, 4), round(rbc, 4), round(rca, 4), derivation

    # --- MECHANICAL ENGINEERING FUNDAMENTALS ---

    @staticmethod
    def stress_strain_modulus(force_n, area_m2, delta_l_m, original_l_m):
        """Computes Stress σ, Strain ε, and Young's Modulus E."""
        if area_m2 <= 0 or original_l_m <= 0:
            raise ValueError("Cross-sectional area and original length must be positive non-zero.")
        stress = force_n / area_m2
        strain = delta_l_m / original_l_m
        if strain == 0:
            raise ValueError("Deformation (ΔL) cannot be zero for Young's Modulus calculation.")
        youngs_modulus = stress / strain
        derivation = (
            f"Stress σ = Force / Area = {force_n} / {area_m2} = {stress:.4e} Pa ({stress/1e6:.2f} MPa)\n"
            f"Strain ε = ΔL / L₀ = {delta_l_m} / {original_l_m} = {strain:.6f} (dimensionless)\n"
            f"Young's Modulus E = σ / ε = {youngs_modulus:.4e} Pa ({youngs_modulus/1e9:.2f} GPa)"
        )
        return round(stress, 2), round(strain, 6), round(youngs_modulus, 2), derivation

    @staticmethod
    def carnot_efficiency(temp_hot_k, temp_cold_k):
        """Calculates theoretical Carnot thermal engine efficiency."""
        if temp_hot_k <= 0 or temp_cold_k <= 0:
            raise ValueError("Temperatures must be specified in Kelvin and > 0.")
        if temp_cold_k >= temp_hot_k:
            raise ValueError("Cold reservoir temperature must be less than hot reservoir temperature.")
        eta = 1.0 - (temp_cold_k / temp_hot_k)
        eta_pct = eta * 100.0
        derivation = f"η = 1 - (T_cold / T_hot) = 1 - ({temp_cold_k} / {temp_hot_k}) = {eta:.4f} ({eta_pct:.2f}%)"
        return round(eta_pct, 2), derivation
