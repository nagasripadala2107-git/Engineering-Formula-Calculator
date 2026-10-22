# 🎓 Engineering Formula Platform & Advanced Virtual Lab Suite

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-WebGL%203D-3F4F75.svg?logo=plotly&logoColor=white)](https://plotly.com/)
[![SymPy](https://img.shields.io/badge/SymPy-Symbolic%20Math-3B5526.svg?logo=python&logoColor=white)](https://www.sympy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **An all-in-one computational engineering workbench and interactive simulation lab designed for undergraduate engineering students (B.Tech / STEM).**
>
> Bridge the gap between theoretical textbook formulas and hands-on numerical & visual understanding. Solve step-by-step problems, run real-time simulations, fit experimental lab data, and generate academic lab reports with a single click.

---

## 📌 At a Glance: What is this Project?

Undergraduate engineering students frequently struggle with dry mathematical formulas, complex matrix steps, beam load distributions, and abstract wave phenomena.

**Engineering Formula Platform & Lab Suite** transforms static formulas into **interactive, dynamic simulations**:
- 🧮 **Solve Complex Math Symbolically & Numerically**: Eigenvalues, Echelon form row operations, and multivariable gradients.
- 🏗️ **Analyze Structural Mechanics**: Real-time Shear Force (SFD) & Bending Moment (BMD) diagrams with reaction calculations.
- 🌊 **Synthesize Waveforms & Fourier Series**: Tune harmonic sliders to observe convergence and the Gibbs phenomenon live.
- 🔬 **Analyze Lab Experiments**: Automated least-squares curve fitting for Ohm's Law, Hooke's Law, and Newton's Rings.
- 🏔️ **3D Calculus Visualizer**: WebGL-powered 3D rotatable surfaces (saddles, paraboloids, ripple waves).
- 📄 **Export Coursework & Reports**: Download computation histories (CSV) and auto-formatted Academic Markdown Lab Reports.

---

## 🚀 Quick Start Guide

### 1. Prerequisites
Ensure you have **Python 3.9+** installed:
```bash
python --version
```

### 2. Clone the Repository
```bash
git clone https://github.com/nagasripadala2107-git/Engineering-Formula-Calculator.git
cd Engineering-Formula-Calculator
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the Web Application
```bash
streamlit run app.py
```
*The application will automatically launch in your browser at `http://localhost:8501`.*

---

## 🌟 Modules & Features Overview

| Module | Topic | Key Capabilities |
| :--- | :--- | :--- |
| **🔬 Advanced Lab** | Curve Fitting & Regression | Least-squares fitting ($m, c, r, R^2$), Ohm's Law, Hooke's Law, Newton's Rings with interactive scatter + trendlines |
| **🌊 Advanced Lab** | Fourier Series Synthesizer | Square, Sawtooth, & Triangular waves with dynamic harmonic blending ($N=1$ to $40$) and Gibbs phenomenon demonstration |
| **🏗️ Advanced Lab** | Structural Beam Analysis | Simply supported beams under point/UDL loads, support reactions ($R_A, R_B$), $M_{\max}$, and dynamic dual SFD & BMD plots |
| **🌀 Advanced Lab** | Mechanical Vibrations | 2nd-order ODEs ($m\ddot{x} + c\dot{x} + kx = 0$), natural/damped frequencies, auto-classification (Under/Critical/Overdamped) |
| **🏔️ Advanced Lab** | 3D Topography Plotter | Rotatable 3D WebGL surfaces (Saddle, Paraboloids, Monkey Saddle, Bessel Ripple) with contour projections |
| **📐 Mathematics** | Linear Algebra & Calculus | Matrix inverse/det/rank with step-by-step Echelon form, exact SymPy eigenvalues/eigenvectors, $AX=B$ LU solver, 3D vector calculus |
| **⚡ Physics** | Optics & Crystallography | Newton's Rings radius $R$, thin film interference $\mu$, Bragg's Law, interplanar spacing $d_{hkl}$, 1D quantum well, Hall effect |
| **🔌 BEEE** | Electrical & Mechanical | Resistor/Capacitor networks, Star-Delta conversion, RLC resonance, stress/strain/Young's modulus, Carnot engine efficiency |
| **🎯 Academic Tools** | Quiz, Converter & Reports | Conceptual engineering practice quiz, multi-unit converter + 13 physical constants, and 1-click Lab Report generator |

---

## 🖥️ System Architecture & Codebase Layout

The project follows a clean, decoupled modular design where core calculation logic is separated from UI components and visual representations:

```
Engineering-Formula-Calculator/
├── app.py                      # Main Streamlit web application & UI navigation
├── main.py                     # CLI / entrypoint interface
├── requirements.txt            # Dependency specifications
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore rules
└── modules/                    # Computational & domain engines
    ├── advanced_lab.py         # Advanced lab algorithms (Fourier, Vibrations, SFD/BMD, Regression)
    ├── visualizer.py           # Plotly 2D/3D interactive charts & graphic rendering
    ├── math_engine.py          # SymPy & NumPy linear algebra, vector calculus, matrices
    ├── physics_engine.py       # Wave optics, quantum mechanics, crystallography
    ├── ee_engine.py            # Circuits, Star-Delta, RLC resonance, solid mechanics
    ├── converter.py            # Engineering unit converter & physical constants table
    ├── quiz_engine.py          # Interactive branch-wise engineering quiz questions
    ├── report_generator.py     # Academic Markdown report generation & export
    └── ai_engine.py            # Rule-based calculation suggestions & guidance
```

---

## 🛠️ Built With

- **[Python](https://www.python.org/)** — Core programming language
- **[Streamlit](https://streamlit.io/)** — Reactive web dashboard with custom glassmorphism styling
- **[Plotly](https://plotly.com/)** — WebGL-accelerated 2D/3D interactive scientific visualizations
- **[SymPy](https://www.sympy.org/)** — Symbolic computer algebra system for exact analytical expressions
- **[NumPy](https://numpy.org/)** & **[Pandas](https://pandas.pydata.org/)** — High-performance numerical arrays and table manipulation

---

## 🎯 Target Audience & Curriculum

Specially aligned with standard undergraduate engineering curricula (including **JNTUK R23 / AICTE model curriculum**):
- **First Year Engineering (Common)**: Linear Algebra & Calculus (LA&C), Engineering Physics, Basic Electrical & Electronics Engineering (BEEE).
- **Core Disciplines**: Mechanical Engineering (Vibrations, Solid Mechanics), Civil Engineering (Strength of Materials, SFD/BMD), Electronics (Signals & Fourier Series).

---

## 🤝 Contributing

Contributions, feature requests, and suggestions are welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

⭐ **If you find this project helpful for your engineering coursework or lab studies, consider giving it a star on GitHub!**
