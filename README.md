# 🎓 Engineering Formula Platform & Advanced Lab Suite (v3.0)

A comprehensive, interactive web platform and computational engineering suite designed for B.Tech students (aligned with the JNTUK R23 curriculum). Built using **Python**, **Streamlit**, **SymPy**, **NumPy**, **Pandas**, and **Plotly**.

---

## 🌟 Complete Feature Index

### 1. 🔬 Experimental Data Curve Fitting & Linear Regression
* **Least-Squares Regression:** Calculates optimal slope $m$, y-intercept $c$, Pearson correlation $r$, and $R^2$ determination coefficient.
* **Presets Included:** Ohm's Law ($V$ vs $I$), Hooke's Law ($F$ vs $\Delta x$), and Newton's Rings ($D^2$ vs $n$).
* **Visual Output:** Interactive Plotly scatter plot with linear trendline and equation display.

### 2. 🌊 Fourier Series & Harmonic Waveform Synthesizer
* **Waveforms:** Square Wave, Sawtooth Wave, and Triangular Wave.
* **Harmonic Slider:** Dynamically blend $N = 1$ to $40$ sinusoidal harmonics.
* **Observation:** Real-time demonstration of harmonic convergence and the Gibbs phenomenon at jump discontinuities.

### 3. 🏗️ Structural Beam Analysis (SFD & BMD)
* **Beam Configurations:** Simply supported beams with customizable span length $L$.
* **Load Types:** Point load at arbitrary offset $a$ or Uniformly Distributed Load (UDL) across the span.
* **Analytical Solvers:** Left & right support reactions ($R_A, R_B$) and maximum bending moment $M_{\max}$.
* **Dual Diagrams:** Side-by-side Shear Force Diagram (SFD) and Bending Moment Diagram (BMD) with area fills.

### 4. 🌀 Mechanical Vibrations & 2nd Order ODEs
* **Governing Equation:** $m\ddot{x}(t) + c\dot{x}(t) + kx(t) = 0$.
* **Parameters Computed:** Natural frequency $\omega_n$, critical damping $c_c$, damping ratio $\zeta$, and damped frequency $\omega_d$.
* **Classification:** Auto-classifies as **Underdamped ($\zeta < 1$)**, **Critically Damped ($\zeta = 1$)**, or **Overdamped ($\zeta > 1$)**.
* **Dynamic Plot:** Time-displacement curve $x(t)$ with exponential decay envelope bounds.

### 5. 🏔️ 3D Multivariable Calculus Topography Plotter
* **Surfaces:** Hyperbolic Paraboloid (Saddle Surface $z = x^2 - y^2$), Elliptic Paraboloid ($z = x^2 + y^2$), Damped Bessel Ripple Wave ($z = \sin(r)/r$), and Monkey Saddle ($z = x^3 - 3xy^2$).
* **Interactive 3D Engine:** Rotatable 3D WebGL mesh with projected orthogonal contour lines.

### 6. 🕒 Live Session History & Notebook
* **Auto-Logging:** Every calculation from Mathematics, Physics, Electrical, and Structural modules is automatically recorded with timestamps and input/output parameters.
* **CSV Export:** Download full calculation history as a CSV file for coursework records.

### 7. 📐 Mathematics & Linear Algebra (LA&C)
* **Matrix Solvers:** Addition, Multiplication, Inverses, Determinants, and Step-by-Step Echelon Form Rank.
* **SymPy Symbolic Solvers:** Exact characteristic polynomial $\det(\mathbf{A} - \lambda\mathbf{I}) = 0$, exact eigenvalues, eigenvectors, and LU linear system solver ($A X = B$).
* **Vector Calculus:** 3D Vector Magnitude, Dot & Cross Product, Symbolic Gradient $\nabla f$ & Directional Derivative $D_{\hat{u}} f$.

### 8. ⚡ Engineering Physics & Crystallography
* **Wave Optics & Crystallography:** Newton's Rings radius of curvature $R$, Thin Film $\mu$, Interplanar Spacing $d_{hkl}$, and Bragg's Law.
* **Quantum & Solid State:** 1D Infinite Potential Box energy quantization and Hall Coefficient $R_H$.
* **Classical Mechanics:** Kinematics, Force ($F = ma$), Work, Power, and Kinetic Energy.

### 9. 🔌 Basic Electrical & Mechanical Engineering (BEEE)
* **Circuits:** Resistor/Capacitor Series & Parallel networks, Voltage & Current Dividers, Series RLC resonance & Star-to-Delta conversions.
* **Solid Mechanics:** Stress ($\sigma$), Strain ($\epsilon$), Young's Modulus ($E$), and Carnot Heat Engine efficiency ($\eta$).

### 10. 🎯 Practice Quiz, Converter & Lab Report Generator
* **Interactive Quiz:** Instant conceptual grading with explanations across all engineering branches.
* **Unit Converter:** Conversions for Force, Energy, Pressure, Length, and Angle + 13 Universal Constants table.
* **Lab Report Generator:** Academic Markdown report with 1-click download.

---

## 🚀 How to Run

Navigate to the project directory in PowerShell or Terminal:

```powershell
cd c:\Users\prasanna\Downloads\engineering-formula-calucator--main\engineering-formula-calucator--main
python -m streamlit run app.py
```

The app will start and open automatically at: `http://localhost:8501`
