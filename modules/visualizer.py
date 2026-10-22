import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class EngineeringVisualizer:
    """
    Interactive Plotly-based visualizer for Engineering Physics, Mathematics,
    Structural Mechanics, Signal Processing, and Electrical circuits.
    """

    @staticmethod
    def plot_3d_vectors(ax, ay, az, bx, by, bz, show_cross=True):
        """Generates an interactive 3D vector diagram with Vector A, B, and optional Cross Product."""
        fig = go.Figure()

        # Origin
        fig.add_trace(go.Scatter3d(
            x=[0], y=[0], z=[0],
            mode='markers+text',
            marker=dict(size=5, color='black'),
            text=['Origin (0,0,0)'],
            name='Origin'
        ))

        # Vector A
        fig.add_trace(go.Scatter3d(
            x=[0, ax], y=[0, ay], z=[0, az],
            mode='lines+markers',
            line=dict(color='#2563EB', width=7),
            marker=dict(size=[3, 6], color='#2563EB'),
            name='Vector A'
        ))

        # Vector B
        fig.add_trace(go.Scatter3d(
            x=[0, bx], y=[0, by], z=[0, bz],
            mode='lines+markers',
            line=dict(color='#10B981', width=7),
            marker=dict(size=[3, 6], color='#10B981'),
            name='Vector B'
        ))

        # Cross Product (A x B)
        cx = ay * bz - az * by
        cy = az * bx - ax * bz
        cz = ax * by - ay * bx

        if show_cross and (cx != 0 or cy != 0 or cz != 0):
            fig.add_trace(go.Scatter3d(
                x=[0, cx], y=[0, cy], z=[0, cz],
                mode='lines+markers',
                line=dict(color='#EF4444', width=6, dash='dash'),
                marker=dict(size=[3, 7], color='#EF4444'),
                name='A × B (Cross Product)'
            ))

        max_range = max(abs(ax), abs(ay), abs(az), abs(bx), abs(by), abs(bz), 1.0)
        if show_cross:
            max_range = max(max_range, abs(cx), abs(cy), abs(cz))

        fig.update_layout(
            title="3D Vector Space Visualization",
            scene=dict(
                xaxis=dict(title='X Axis', range=[-max_range * 1.2, max_range * 1.2]),
                yaxis=dict(title='Y Axis', range=[-max_range * 1.2, max_range * 1.2]),
                zaxis=dict(title='Z Axis', range=[-max_range * 1.2, max_range * 1.2]),
                aspectmode='cube'
            ),
            margin=dict(l=0, r=0, b=0, t=40),
            legend=dict(x=0.02, y=0.98)
        )
        return fig, (round(cx, 4), round(cy, 4), round(cz, 4))

    @staticmethod
    def plot_particle_in_box(n_quantum, L_nm):
        """Visualizes wave function ψ_n(x) and probability density |ψ_n(x)|² for 1D Infinite Potential Well."""
        x = np.linspace(0, L_nm, 500)
        psi = np.sqrt(2 / L_nm) * np.sin(n_quantum * np.pi * x / L_nm)
        prob_density = psi ** 2

        fig = make_subplots(
            rows=2, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.15,
            subplot_titles=(f"Wavefunction ψ_{n_quantum}(x)", f"Probability Density |ψ_{n_quantum}(x)|²")
        )

        fig.add_trace(
            go.Scatter(x=x, y=psi, mode='lines', line=dict(color='#3B82F6', width=2.5), name=f"ψ_{n_quantum}(x)"),
            row=1, col=1
        )
        fig.add_hline(y=0, line_dash="dash", line_color="gray", row=1, col=1)

        fig.add_trace(
            go.Scatter(
                x=x, y=prob_density, mode='lines', fill='tozeroy',
                line=dict(color='#8B5CF6', width=2.5),
                fillcolor='rgba(139, 92, 246, 0.25)',
                name=f"|ψ_{n_quantum}(x)|²"
            ),
            row=2, col=1
        )

        fig.update_xaxes(title_text="Position x (nm)", row=2, col=1)
        fig.update_yaxes(title_text="Amplitude", row=1, col=1)
        fig.update_yaxes(title_text="Probability Density", row=2, col=1)

        fig.update_layout(
            title=f"Quantum Particle in a Box (Level n = {n_quantum}, Well Width L = {L_nm} nm)",
            height=500,
            showlegend=False,
            margin=dict(l=40, r=40, t=50, b=40)
        )
        return fig

    @staticmethod
    def plot_newtons_rings(wavelength_nm=589.0, radius_curvature_m=1.0):
        """Generates synthetic 2D optical interference fringe pattern of Newton's Rings."""
        lam = wavelength_nm * 1e-9
        R = radius_curvature_m

        grid_size = 400
        limit_mm = 2.5
        x = np.linspace(-limit_mm * 1e-3, limit_mm * 1e-3, grid_size)
        y = np.linspace(-limit_mm * 1e-3, limit_mm * 1e-3, grid_size)
        X, Y = np.meshgrid(x, y)
        r_sq = X**2 + Y**2

        phase = (2 * np.pi * r_sq) / (2 * R * lam)
        intensity = np.sin(phase)**2

        fig = go.Figure(data=go.Heatmap(
            z=intensity,
            x=np.linspace(-limit_mm, limit_mm, grid_size),
            y=np.linspace(-limit_mm, limit_mm, grid_size),
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title='Intensity')
        ))

        fig.update_layout(
            title=f"Newton's Rings Interference Pattern (λ = {wavelength_nm} nm, R = {radius_curvature_m} m)",
            xaxis_title="Radial distance x (mm)",
            yaxis_title="Radial distance y (mm)",
            width=500,
            height=500,
            yaxis=dict(scaleanchor="x", scaleratio=1),
            margin=dict(l=30, r=30, t=50, b=30)
        )
        return fig

    @staticmethod
    def plot_kinematics(u, a, t_total):
        """Generates Displacement-Time and Velocity-Time graphs."""
        t = np.linspace(0, max(t_total, 1.0), 300)
        v = u + a * t
        s = u * t + 0.5 * a * t**2

        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=("Velocity vs. Time (v = u + at)", "Displacement vs. Time (s = ut + ½at²)")
        )

        fig.add_trace(
            go.Scatter(x=t, y=v, mode='lines', line=dict(color='#0284C7', width=3), name="v(t)"),
            row=1, col=1
        )
        fig.add_trace(
            go.Scatter(x=t, y=s, mode='lines', line=dict(color='#059669', width=3), name="s(t)"),
            row=1, col=2
        )

        fig.update_xaxes(title_text="Time t (s)", row=1, col=1)
        fig.update_yaxes(title_text="Velocity (m/s)", row=1, col=1)
        fig.update_xaxes(title_text="Time t (s)", row=1, col=2)
        fig.update_yaxes(title_text="Displacement (m)", row=1, col=2)

        fig.update_layout(
            title=f"Kinematic Motion Analysis (Initial Velocity u = {u} m/s, Acceleration a = {a} m/s²)",
            height=400,
            showlegend=False,
            margin=dict(l=40, r=40, t=50, b=40)
        )
        return fig

    @staticmethod
    def plot_rlc_resonance(r_ohm, l_mh, c_uf, v_rms=10.0):
        """Plots frequency response and resonance peak for Series RLC Circuit."""
        L = l_mh * 1e-3
        C = c_uf * 1e-6
        f_0 = 1 / (2 * np.pi * np.sqrt(L * C)) if (L * C) > 0 else 1000

        f_min = max(1.0, f_0 * 0.1)
        f_max = f_0 * 2.5
        f = np.linspace(f_min, f_max, 600)
        omega = 2 * np.pi * f

        X_L = omega * L
        X_C = 1 / (omega * C)
        Z = np.sqrt(r_ohm**2 + (X_L - X_C)**2)
        current = v_rms / Z

        omega_0 = 2 * np.pi * f_0
        q_factor = (omega_0 * L) / r_ohm if r_ohm > 0 else 0

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=f, y=current,
            mode='lines',
            line=dict(color='#DC2626', width=3),
            name="Current I (A)"
        ))

        i_peak = v_rms / r_ohm if r_ohm > 0 else 0
        fig.add_trace(go.Scatter(
            x=[f_0], y=[i_peak],
            mode='markers+text',
            marker=dict(size=10, color='#991B1B'),
            text=[f"Resonance f₀ = {f_0:.1f} Hz"],
            textposition="top center",
            name="Resonance Peak"
        ))

        fig.update_layout(
            title=f"Series RLC Circuit Resonance Response (R = {r_ohm} Ω, L = {l_mh} mH, C = {c_uf} µF)",
            xaxis_title="Frequency f (Hz)",
            yaxis_title="Current I_rms (A)",
            height=420,
            margin=dict(l=40, r=40, t=50, b=40)
        )
        return fig, round(f_0, 2), round(q_factor, 2)

    # --- NEW FEATURE 1: EXPERIMENTAL CURVE FIT PLOTTER ---

    @staticmethod
    def plot_curve_fit(x_data, y_data, slope, intercept, r_squared):
        """Plots experimental data scatter and linear regression trendline."""
        x = np.array(x_data, dtype=float)
        y = np.array(y_data, dtype=float)

        x_line = np.linspace(min(x), max(x), 200)
        y_line = slope * x_line + intercept

        fig = go.Figure()
        # Scatter of raw data
        fig.add_trace(go.Scatter(
            x=x, y=y,
            mode='markers',
            marker=dict(size=9, color='#3B82F6', line=dict(width=1.5, color='white')),
            name='Experimental Data Points'
        ))
        # Best-fit trendline
        sign = "+" if intercept >= 0 else "-"
        fig.add_trace(go.Scatter(
            x=x_line, y=y_line,
            mode='lines',
            line=dict(color='#EF4444', width=3),
            name=f"Fit: y = {slope:.4f}x {sign} {abs(intercept):.4f} (R² = {r_squared:.4f})"
        ))

        fig.update_layout(
            title="Experimental Data & Linear Regression Trendline",
            xaxis_title="Independent Variable X",
            yaxis_title="Dependent Variable Y",
            height=450,
            legend=dict(x=0.02, y=0.98),
            margin=dict(l=40, r=40, t=50, b=40)
        )
        return fig

    # --- NEW FEATURE 2: FOURIER SERIES SYNTHESIZER ---

    @staticmethod
    def plot_fourier_series(waveform="Square Wave", num_harmonics=5):
        """Synthesizes Fourier series harmonics and plots Gibbs phenomenon."""
        t = np.linspace(-np.pi, np.pi, 800)
        y_fourier = np.zeros_like(t)

        if waveform == "Square Wave":
            # 4/pi * sum_{n=1,3,5,...} (1/n) * sin(n*t)
            for k in range(1, num_harmonics + 1):
                n = 2 * k - 1
                y_fourier += (4.0 / (np.pi * n)) * np.sin(n * t)
            y_ideal = np.sign(np.sin(t))

        elif waveform == "Sawtooth Wave":
            # 2/pi * sum_{n=1,2,3,...} ((-1)^(n+1) / n) * sin(n*t)
            for n in range(1, num_harmonics + 1):
                y_fourier += (2.0 / (np.pi * n)) * ((-1) ** (n + 1)) * np.sin(n * t)
            y_ideal = t / np.pi

        else: # Triangular Wave
            # 8/pi^2 * sum_{k=1...} ((-1)^(k-1) / (2k-1)^2) * sin((2k-1)*t)
            for k in range(1, num_harmonics + 1):
                n = 2 * k - 1
                y_fourier += (8.0 / (np.pi**2 * n**2)) * ((-1)**(k - 1)) * np.sin(n * t)
            y_ideal = 1 - 2 * np.abs(t) / np.pi

        fig = go.Figure()
        # Ideal Target Waveform
        fig.add_trace(go.Scatter(
            x=t, y=y_ideal,
            mode='lines',
            line=dict(color='rgba(255, 255, 255, 0.4)', dash='dash', width=2),
            name=f"Ideal {waveform}"
        ))
        # Fourier Synthesis
        fig.add_trace(go.Scatter(
            x=t, y=y_fourier,
            mode='lines',
            line=dict(color='#10B981', width=3),
            name=f"Fourier Approximation ({num_harmonics} Harmonics)"
        ))

        fig.update_layout(
            title=f"Fourier Series Waveform Synthesis: {waveform} (N = {num_harmonics} Harmonics)",
            xaxis_title="Angle θ / Time t (rad)",
            yaxis_title="Amplitude f(t)",
            height=450,
            margin=dict(l=40, r=40, t=50, b=40)
        )
        return fig

    # --- NEW FEATURE 3: STRUCTURAL BEAM SFD & BMD ---

    @staticmethod
    def plot_sfd_bmd(x, sfd, bmd, length_m, max_moment):
        """Generates Shear Force Diagram (SFD) and Bending Moment Diagram (BMD) plots."""
        fig = make_subplots(
            rows=2, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.15,
            subplot_titles=("Shear Force Diagram (SFD)", "Bending Moment Diagram (BMD)")
        )

        # SFD
        fig.add_trace(
            go.Scatter(
                x=x, y=sfd, mode='lines', fill='tozeroy',
                line=dict(color='#F59E0B', width=2.5),
                fillcolor='rgba(245, 158, 11, 0.25)',
                name="Shear Force V(x)"
            ),
            row=1, col=1
        )
        fig.add_hline(y=0, line_dash="solid", line_color="gray", row=1, col=1)

        # BMD
        fig.add_trace(
            go.Scatter(
                x=x, y=bmd, mode='lines', fill='tozeroy',
                line=dict(color='#8B5CF6', width=2.5),
                fillcolor='rgba(139, 92, 246, 0.25)',
                name="Bending Moment M(x)"
            ),
            row=2, col=1
        )
        fig.add_hline(y=0, line_dash="solid", line_color="gray", row=2, col=1)

        fig.update_xaxes(title_text="Beam Position x (m)", row=2, col=1)
        fig.update_yaxes(title_text="Shear Force (kN)", row=1, col=1)
        fig.update_yaxes(title_text="Moment (kN·m)", row=2, col=1)

        fig.update_layout(
            title=f"Structural Beam Analysis (Span L = {length_m} m, Max Moment = {max_moment:.2f} kN·m)",
            height=500,
            showlegend=False,
            margin=dict(l=40, r=40, t=50, b=40)
        )
        return fig

    # --- NEW FEATURE 4: SPRING-MASS-DAMPER VIBRATIONS ---

    @staticmethod
    def plot_vibration_response(t, x, omega_n, zeta, regime):
        """Plots dynamic displacement response x(t) for Spring-Mass-Damper ODE."""
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=t, y=x,
            mode='lines',
            line=dict(color='#06B6D4', width=3),
            name=f"x(t) [{regime}]"
        ))

        # Envelope if underdamped
        if zeta < 1.0:
            env = np.exp(-zeta * omega_n * t)
            fig.add_trace(go.Scatter(
                x=t, y=env, mode='lines',
                line=dict(color='rgba(239, 68, 68, 0.5)', dash='dot', width=1.5),
                name="Decay Envelope +e^(-ζωₙt)"
            ))
            fig.add_trace(go.Scatter(
                x=t, y=-env, mode='lines',
                line=dict(color='rgba(239, 68, 68, 0.5)', dash='dot', width=1.5),
                name="Decay Envelope -e^(-ζωₙt)"
            ))

        fig.add_hline(y=0, line_dash="dash", line_color="gray")

        fig.update_layout(
            title=f"Vibration Response x(t): {regime} (ωₙ = {omega_n:.2f} rad/s, ζ = {zeta:.3f})",
            xaxis_title="Time t (s)",
            yaxis_title="Displacement x (m)",
            height=430,
            margin=dict(l=40, r=40, t=50, b=40)
        )
        return fig

    # --- NEW FEATURE 5: 3D MULTIVARIABLE SURFACE PLOTTER ---

    @staticmethod
    def plot_3d_surface(surface_type="Saddle Surface (z = x² - y²)", grid_range=3.0):
        """Renders interactive 3D multivariable surface topography with contours."""
        r = float(grid_range)
        x = np.linspace(-r, r, 70)
        y = np.linspace(-r, r, 70)
        X, Y = np.meshgrid(x, y)

        if "Saddle" in surface_type:
            Z = X**2 - Y**2
            title = "Hyperbolic Paraboloid / Saddle Surface: z = x² - y²"
        elif "Paraboloid" in surface_type:
            Z = X**2 + Y**2
            title = "Elliptic Paraboloid: z = x² + y²"
        elif "Ripple" in surface_type:
            R = np.sqrt(X**2 + Y**2) + 1e-5
            Z = np.sin(R) / R
            title = "Damped Bessel Ripple Wave: z = sin(r)/r"
        else: # Monkey Saddle
            Z = X**3 - 3*X*Y**2
            title = "Monkey Saddle Surface: z = x³ - 3xy²"

        fig = go.Figure(data=[go.Surface(
            z=Z, x=X, y=Y,
            colorscale='Turbo',
            contours=dict(
                z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True)
            )
        )])

        fig.update_layout(
            title=title,
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z',
                camera=dict(eye=dict(x=1.4, y=1.4, z=1.2))
            ),
            height=550,
            margin=dict(l=0, r=0, b=0, t=40)
        )
        return fig
