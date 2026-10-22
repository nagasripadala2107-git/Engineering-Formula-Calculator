import numpy as np

class AdvancedLabEngine:
    """
    Lab-grade computational engine for Experimental Curve Fitting,
    Structural SFD/BMD Beam analysis, and 2nd Order Vibration ODEs.
    """

    # --- 1. EXPERIMENTAL CURVE FITTING & REGRESSION ---

    @staticmethod
    def linear_regression(x_vals, y_vals):
        """
        Computes least-squares linear fit y = mx + c, Pearson r, and R^2.
        """
        if len(x_vals) != len(y_vals):
            raise ValueError("X and Y arrays must have identical number of data points.")
        if len(x_vals) < 2:
            raise ValueError("At least 2 data points are required for linear regression.")

        x = np.array(x_vals, dtype=float)
        y = np.array(y_vals, dtype=float)
        n = len(x)

        # Standard linear regression formulas
        sum_x = np.sum(x)
        sum_y = np.sum(y)
        sum_xy = np.sum(x * y)
        sum_x2 = np.sum(x ** 2)
        sum_y2 = np.sum(y ** 2)

        denom = (n * sum_x2 - sum_x ** 2)
        if denom == 0:
            raise ValueError("All X coordinates are identical; vertical line slope undefined.")

        slope = (n * sum_xy - sum_x * sum_y) / denom
        intercept = (sum_y - slope * sum_x) / n

        # Correlation coefficient r and R^2
        r_num = (n * sum_xy - sum_x * sum_y)
        r_denom = np.sqrt(abs((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)))
        r = r_num / r_denom if r_denom != 0 else 0.0
        r_squared = r ** 2

        derivation = [
            f"Number of Data Points (N): {n}",
            f"Sum of X: {sum_x:.4f}, Sum of Y: {sum_y:.4f}",
            f"Slope m = (N·Σxy - Σx·Σy) / (N·Σx² - (Σx)²) = {slope:.4f}",
            f"Intercept c = (Σy - m·Σx) / N = {intercept:.4f}",
            f"Regression Model: y = {slope:.4f}x + {intercept:.4f}",
            f"Coefficient of Determination R²: {r_squared:.4f} (Fit accuracy: {r_squared*100:.2f}%)"
        ]

        return slope, intercept, r_squared, derivation

    # --- 2. STRUCTURAL BEAM ANALYSIS (SFD & BMD) ---

    @staticmethod
    def calculate_sfd_bmd(length_m, load_type="Point Load", load_val=10.0, load_pos=2.5):
        """
        Calculates reactions, Shear Force Diagram (SFD), and Bending Moment Diagram (BMD)
        for a simply supported beam of span L.
        """
        L = float(length_m)
        if L <= 0:
            raise ValueError("Beam span length must be strictly positive.")

        x = np.linspace(0, L, 500)
        sfd = np.zeros_like(x)
        bmd = np.zeros_like(x)

        if load_type == "Point Load":
            P = float(load_val)
            a = float(load_pos)
            if a < 0 or a > L:
                raise ValueError(f"Load position must be within beam span [0, {L}] m.")
            b = L - a
            # Support reactions
            ra = P * b / L
            rb = P * a / L

            # SFD and BMD
            for i, pos in enumerate(x):
                if pos < a:
                    sfd[i] = ra
                    bmd[i] = ra * pos
                else:
                    sfd[i] = ra - P
                    bmd[i] = ra * pos - P * (pos - a)

            max_moment = (P * a * b) / L
            details = [
                f"Support Reaction at Left (R_A): {ra:.2f} kN",
                f"Support Reaction at Right (R_B): {rb:.2f} kN",
                f"Maximum Bending Moment: {max_moment:.2f} kN·m at x = {a:.2f} m",
                f"Point of zero shear force occurs at load position x = {a:.2f} m"
            ]

        else: # Uniformly Distributed Load (UDL)
            w = float(load_val) # in kN/m
            ra = w * L / 2.0
            rb = w * L / 2.0

            sfd = ra - w * x
            bmd = ra * x - 0.5 * w * x**2
            max_moment = (w * L**2) / 8.0

            details = [
                f"Support Reaction at Left (R_A): {ra:.2f} kN",
                f"Support Reaction at Right (R_B): {rb:.2f} kN",
                f"Maximum Bending Moment: {max_moment:.2f} kN·m at center x = {L/2:.2f} m",
                f"Shear force varies linearly: V(x) = {ra:.2f} - {w:.2f}x",
                f"Bending moment varies parabolically: M(x) = {ra:.2f}x - 0.5({w:.2f})x²"
            ]

        return x, sfd, bmd, ra, rb, max_moment, details

    # --- 3. VIBRATION & 2ND ORDER ODE (SPRING-MASS-DAMPER) ---

    @staticmethod
    def solve_spring_mass_damper(mass_kg, damping_c, stiffness_k, x0=1.0, v0=0.0, t_max=10.0):
        """
        Solves m x''(t) + c x'(t) + k x(t) = 0.
        Computes omega_n, zeta, damping category, and time-response x(t).
        """
        m = float(mass_kg)
        c = float(damping_c)
        k = float(stiffness_k)

        if m <= 0 or k <= 0 or c < 0:
            raise ValueError("Mass and stiffness must be positive; damping coefficient must be >= 0.")

        # Natural angular frequency omega_n
        omega_n = np.sqrt(k / m)
        # Critical damping coefficient c_c
        c_crit = 2.0 * np.sqrt(m * k)
        # Damping ratio zeta
        zeta = c / c_crit

        t = np.linspace(0, float(t_max), 600)

        if abs(zeta - 1.0) < 1e-4:
            regime = "Critically Damped (ζ = 1.0)"
            # x(t) = (A + B*t) * exp(-omega_n * t)
            A = x0
            B = v0 + omega_n * x0
            x = (A + B * t) * np.exp(-omega_n * t)
            omega_d = 0.0

        elif zeta < 1.0:
            regime = "Underdamped (Oscillatory, ζ < 1.0)"
            omega_d = omega_n * np.sqrt(1.0 - zeta**2)
            # x(t) = exp(-zeta * omega_n * t) * (C1 * cos(omega_d * t) + C2 * sin(omega_d * t))
            C1 = x0
            C2 = (v0 + zeta * omega_n * x0) / omega_d if omega_d > 0 else 0.0
            x = np.exp(-zeta * omega_n * t) * (C1 * np.cos(omega_d * t) + C2 * np.sin(omega_d * t))

        else: # zeta > 1.0
            regime = "Overdamped (Non-oscillatory slow decay, ζ > 1.0)"
            r1 = -omega_n * (zeta - np.sqrt(zeta**2 - 1.0))
            r2 = -omega_n * (zeta + np.sqrt(zeta**2 - 1.0))
            # x(t) = C1 * exp(r1 * t) + C2 * exp(r2 * t)
            C2 = (v0 - r1 * x0) / (r2 - r1)
            C1 = x0 - C2
            x = C1 * np.exp(r1 * t) + C2 * np.exp(r2 * t)
            omega_d = 0.0

        details = [
            f"Natural Frequency ωₙ: {omega_n:.4f} rad/s ({omega_n / (2*np.pi):.4f} Hz)",
            f"Critical Damping Coefficient c_c: {c_crit:.4f} N·s/m",
            f"Damping Ratio ζ: {zeta:.4f}",
            f"Vibration Regime: {regime}",
            f"Damped Angular Frequency ω_d: {omega_d:.4f} rad/s"
        ]

        return t, x, omega_n, zeta, omega_d, regime, details
