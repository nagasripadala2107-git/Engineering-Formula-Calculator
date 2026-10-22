import sys
import os
import math
from datetime import datetime
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.math_engine import MathEngine
from modules.physics_engine import PhysicsEngine
from modules.ee_engine import EngineeringDisciplineEngine
from modules.advanced_lab import AdvancedLabEngine
from modules.visualizer import EngineeringVisualizer
from modules.converter import EngineeringConverter
from modules.quiz_engine import QuizEngine
from modules.report_generator import ReportGenerator
from modules.ai_engine import RuleBasedAIEngine

# Page Configuration
st.set_page_config(
    page_title="Engineering Formula Platform & Advanced Lab Suite",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Glassmorphism & Modern Dark Aesthetics)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    .stApp {
        background: radial-gradient(circle at top right, #0F172A, #020617);
        color: #F8FAFC;
    }
    
    .metric-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        border-radius: 14px;
        padding: 16px 20px;
        margin-bottom: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }
    
    .badge-pill {
        background: linear-gradient(135deg, #3B82F6, #8B5CF6);
        color: white;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 8px;
    }
    
    .formula-box {
        background: rgba(15, 23, 42, 0.85);
        border-left: 4px solid #38BDF8;
        padding: 14px 18px;
        border-radius: 8px;
        margin: 12px 0px;
        font-family: monospace;
    }
</style>
""", unsafe_allow_html=True)

# Session State for History Notebook
if "calc_history" not in st.session_state:
    st.session_state["calc_history"] = []

def log_calculation(category, solver, inputs_str, result_str):
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state["calc_history"].append({
        "Time": timestamp,
        "Category": category,
        "Solver": solver,
        "Inputs": str(inputs_str),
        "Result": str(result_str)
    })

ai_engine = RuleBasedAIEngine()

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<span class='badge-pill'>JNTUK R23 B.Tech Suite</span>", unsafe_allow_html=True)
    st.title("🎓 Engineering Hub")
    st.caption("Computational Solvers, Lab Curve Fitting, Structural SFD/BMD & 3D Simulations")
    st.markdown("---")
    
    selected_section = st.radio(
        "Navigation Menu:",
        [
            "🏠 Home & Syllabus",
            "⚡ Live Calculators",
            "🔬 Experimental Curve Fitting",
            "🌊 Fourier Harmonic Synthesizer",
            "🏗️ Beam SFD & BMD Analyzer",
            "🌀 Vibrations & ODE Dynamics",
            "🏔️ 3D Multivariable Surfaces",
            "📈 3D & 2D Physics Visuals",
            "🤖 AI Assistant & Search",
            "🎯 Practice Quiz & Self-Test",
            "🔄 Unit Converter & Constants",
            "🕒 Session History & Notebook",
            "📄 Export Lab Report",
            "ℹ️ About & Curriculum"
        ]
    )
    st.markdown("---")
    st.info(f"💾 **History Logged:** {len(st.session_state['calc_history'])} calculations")

# ==========================================================
# 1. HOME & SYLLABUS
# ==========================================================
if selected_section == "🏠 Home & Syllabus":
    st.markdown("<span class='badge-pill'>Academic Engineering Platform</span>", unsafe_allow_html=True)
    st.title("🎓 Engineering Formula Calculator & Lab Suite")
    st.caption("Interactive Mathematical, Physical, Structural & Computational Science Platform")
    st.markdown("---")
    
    # KPI Metrics
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown("<div class='metric-card'><div style='color:#94A3B8; font-size:0.85rem;'>DISCIPLINES</div><div style='font-size:1.8rem; font-weight:700; color:#38BDF8;'>5 Branches</div><div style='font-size:0.8rem; color:#10B981;'>Math, Physics, EE, Mech, Civil</div></div>", unsafe_allow_html=True)
    with k2:
        st.markdown("<div class='metric-card'><div style='color:#94A3B8; font-size:0.85rem;'>SOLVERS</div><div style='font-size:1.8rem; font-weight:700; color:#A78BFA;'>40+ Tools</div><div style='font-size:0.8rem; color:#10B981;'>With Analytical Proofs</div></div>", unsafe_allow_html=True)
    with k3:
        st.markdown("<div class='metric-card'><div style='color:#94A3B8; font-size:0.85rem;'>LAB SIMULATORS</div><div style='font-size:1.8rem; font-weight:700; color:#34D399;'>8 Simulators</div><div style='font-size:0.8rem; color:#10B981;'>3D, SFD/BMD, Fourier, ODEs</div></div>", unsafe_allow_html=True)
    with k4:
        st.markdown("<div class='metric-card'><div style='color:#94A3B8; font-size:0.85rem;'>CURRICULUM</div><div style='font-size:1.8rem; font-weight:700; color:#F472B6;'>JNTUK R23</div><div style='font-size:0.8rem; color:#10B981;'>B.Tech Engineering</div></div>", unsafe_allow_html=True)
        
    st.markdown("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📐 Mathematics & Numerical Methods")
        st.write("""
        - **Linear Algebra:** Echelon Rank, Gauss-Jordan Inversion, Determinants, SymPy Eigenvalues & Linear Systems.
        - **Multivariable Calculus:** Gradient, Directional Derivatives, 3D Surface Topographies.
        - **Signal Processing:** Fourier Series decomposition & Gibbs Phenomenon animation.
        """)
    with c2:
        st.subheader("⚙️ Applied Engineering & Physics")
        st.write("""
        - **Experimental Data Analysis:** Least-squares linear regression & trendlines for lab experiments.
        - **Structural Mechanics:** Simply supported beam Shear Force & Bending Moment Diagrams (SFD & BMD).
        - **Mechanical Dynamics:** Spring-Mass-Damper 2nd order ODE vibration curves.
        - **Physics & Circuits:** Newton's Rings, Bragg's Law, Quantum Wells, Series RLC resonance & Star-Delta networks.
        """)

# ==========================================================
# 2. LIVE CALCULATORS
# ==========================================================
elif selected_section == "⚡ Live Calculators":
    st.title("⚡ Interactive Solvers & Derivations")
    st.caption("Step-by-step mathematical computations with formula substitutions and validation")
    st.markdown("---")
    
    tabs = st.tabs(["📐 Mathematics & Linear Algebra", "🔬 Engineering Physics", "⚡ Electrical & Mechanical"])
    
    # --- TAB 1: MATHEMATICS ---
    with tabs[0]:
        math_choice = st.selectbox(
            "Select Mathematics Solver:",
            [
                "Matrix Addition & Multiplication",
                "Matrix Inverse & Determinant (2x2 / 3x3)",
                "Matrix Rank (Row Echelon Form)",
                "Exact Eigenvalues & Eigenvectors (SymPy)",
                "System of Linear Equations (A X = B)",
                "3D Vectors: Magnitude, Dot & Cross Product",
                "Symbolic Gradient & Directional Derivative"
            ]
        )
        
        if math_choice == "Matrix Addition & Multiplication":
            op = st.radio("Operation:", ["Matrix Addition", "Matrix Multiplication"], horizontal=True)
            dim = st.radio("Matrix Dimension:", ["2x2", "3x3"], horizontal=True, key="mat_add_dim")
            n = 2 if dim == "2x2" else 3
            
            c1, c2 = st.columns(2)
            with c1:
                st.write(f"**Matrix A ({dim})**")
                mA = [[st.number_input(f"A[{r+1},{c+1}]", value=1.0 if r==c else 0.0, key=f"ma_{r}_{c}") for c in range(n)] for r in range(n)]
            with c2:
                st.write(f"**Matrix B ({dim})**")
                mB = [[st.number_input(f"B[{r+1},{c+1}]", value=2.0 if r==c else 1.0, key=f"mb_{r}_{c}") for c in range(n)] for r in range(n)]
                
            if st.button("Compute Result & Steps", type="primary"):
                res, steps = MathEngine.matrix_add(mA, mB) if op == "Matrix Addition" else MathEngine.matrix_multiply(mA, mB)
                st.success("### ✅ Output Matrix:")
                cols = st.columns(n)
                for r in range(n):
                    for c in range(n):
                        cols[c].info(f"**{res[r][c]}**")
                        
                with st.expander("🔍 View Step-by-Step Calculation", expanded=True):
                    for s in steps:
                        st.write(f"- {s}")
                log_calculation("Mathematics", op, f"Dim: {dim}", f"Result Matrix: {res}")

        elif math_choice == "Matrix Inverse & Determinant (2x2 / 3x3)":
            dim = st.radio("Dimension:", ["2x2", "3x3"], horizontal=True, key="inv_dim_sel")
            n = 2 if dim == "2x2" else 3
            mA = [[st.number_input(f"A[{r+1},{c+1}]", value=float(r*n + c + 1), key=f"inv_{r}_{c}") for c in range(n)] for r in range(n)]
            
            if st.button("Compute Inverse & Determinant", type="primary"):
                try:
                    inv, det, steps = MathEngine.matrix_inverse(mA)
                    st.success(f"**Determinant det(A):** {det}")
                    st.write("**Inverse Matrix A⁻¹:**")
                    cols = st.columns(n)
                    for r in range(n):
                        for c in range(n):
                            cols[c].info(f"**{inv[r][c]}**")
                    with st.expander("🔍 Derivation Steps", expanded=True):
                        for s in steps:
                            st.write(s)
                    log_calculation("Mathematics", "Inverse & Det", f"A: {mA}", f"det={det}, inv={inv}")
                except ValueError as e:
                    st.error(str(e))

        elif math_choice == "Matrix Rank (Row Echelon Form)":
            dim = st.radio("Dimension:", ["2x2", "3x3"], horizontal=True, key="rk_dim_sel")
            n = 2 if dim == "2x2" else 3
            mA = [[st.number_input(f"A[{r+1},{c+1}]", value=float((r+1)*(c+1)), key=f"rk_{r}_{c}") for c in range(n)] for r in range(n)]
            if st.button("Calculate Rank", type="primary"):
                rank, steps = MathEngine.matrix_rank_echelon(mA)
                st.success(f"**Rank of Matrix:** {rank}")
                with st.expander("🔍 Row Reduction Steps", expanded=True):
                    for s in steps:
                        st.write(f"- {s}")
                log_calculation("Mathematics", "Matrix Rank", f"A: {mA}", f"Rank={rank}")

        elif math_choice == "Exact Eigenvalues & Eigenvectors (SymPy)":
            st.info("Uses SymPy exact symbolic solver to derive Characteristic Equation, Eigenvalues, and Eigenvectors.")
            dim = st.radio("Dimension:", ["2x2", "3x3"], horizontal=True, key="eig_dim")
            n = 2 if dim == "2x2" else 3
            mA = [[st.number_input(f"A[{r+1},{c+1}]", value=2.0 if r==c else 1.0, key=f"eig_{r}_{c}") for c in range(n)] for r in range(n)]
            if st.button("Solve Eigenvalues & Eigenvectors", type="primary"):
                try:
                    poly_latex, vals, vects = MathEngine.eigenvalues_and_vectors(mA)
                    st.subheader("Characteristic Polynomial:")
                    st.latex(f"P(\\lambda) = {poly_latex} = 0")
                    st.subheader("Eigenvalues:")
                    for v in vals:
                        st.markdown(f"- **{v}**")
                    st.subheader("Eigenvectors:")
                    for vec in vects:
                        st.markdown(f"- {vec}")
                    log_calculation("Mathematics", "Eigenvalues", f"A: {mA}", f"Vals: {vals}")
                except Exception as e:
                    st.error(f"Error computing eigenvalues: {str(e)}")

        elif math_choice == "System of Linear Equations (A X = B)":
            st.info("Solves system $A X = B$ for $[x, y]$ or $[x, y, z]$.")
            dim = st.radio("Number of Variables:", ["2 Variables (x, y)", "3 Variables (x, y, z)"], horizontal=True)
            n = 2 if "2" in dim else 3
            
            c1, c2 = st.columns([3, 1])
            with c1:
                st.write("**Coefficient Matrix A:**")
                mA = [[st.number_input(f"A[{r+1},{c+1}]", value=3.0 if r==c else 1.0, key=f"sys_a_{r}_{c}") for c in range(n)] for r in range(n)]
            with c2:
                st.write("**Constant Vector B:**")
                mB = [st.number_input(f"B[{r+1}]", value=float(r+4), key=f"sys_b_{r}") for r in range(n)]
                
            if st.button("Solve Linear System", type="primary"):
                try:
                    sol, steps = MathEngine.solve_linear_system(mA, mB)
                    st.success("### Solution Vector X:")
                    var_names = ["x", "y", "z"]
                    for idx, val in enumerate(sol):
                        st.markdown(f"**{var_names[idx]} = {val}**")
                    with st.expander("🔍 Solution Steps", expanded=True):
                        for s in steps:
                            st.write(f"- {s}")
                    log_calculation("Mathematics", "Linear System", f"A: {mA}, B: {mB}", f"X: {sol}")
                except Exception as e:
                    st.error(str(e))

        elif math_choice == "3D Vectors: Magnitude, Dot & Cross Product":
            c1, c2, c3 = st.columns(3)
            ax = c1.number_input("Vector A: ax", value=2.0)
            ay = c2.number_input("Vector A: ay", value=3.0)
            az = c3.number_input("Vector A: az", value=-1.0)
            
            d1, d2, d3 = st.columns(3)
            bx = d1.number_input("Vector B: bx", value=1.0)
            by = d2.number_input("Vector B: by", value=-2.0)
            bz = d3.number_input("Vector B: bz", value=4.0)
            
            if st.button("Calculate Vector Operations", type="primary"):
                magA, stepA = MathEngine.vector_magnitude(ax, ay, az)
                magB, stepB = MathEngine.vector_magnitude(bx, by, bz)
                dot, stepDot = MathEngine.vector_dot_product(ax, ay, az, bx, by, bz)
                cross, stepCross = MathEngine.vector_cross_product(ax, ay, az, bx, by, bz)
                
                st.success(f"**||A||:** {magA}  |  **||B||:** {magB}  |  **A · B:** {dot}")
                st.info(f"**Cross Product A × B:** `[{cross[0]}, {cross[1]}, {cross[2]}]`")
                with st.expander("🔍 Step-by-Step Derivation", expanded=True):
                    st.write(f"**Magnitude A:** {stepA}")
                    st.write(f"**Magnitude B:** {stepB}")
                    st.write(f"**Dot Product:** {stepDot}")
                    for s in stepCross:
                        st.write(f"- {s}")
                log_calculation("Mathematics", "Vector Operations", f"A=[{ax},{ay},{az}], B=[{bx},{by},{bz}]", f"Dot={dot}, Cross={cross}")

        elif math_choice == "Symbolic Gradient & Directional Derivative":
            st.info("Enter any multi-variable expression $f(x, y, z)$, coordinates, and direction vector.")
            func_str = st.text_input("Scalar Field f(x, y, z):", value="x**2 * y + y * z**2")
            c1, c2, c3 = st.columns(3)
            x0 = c1.number_input("Point x₀:", value=1.0)
            y0 = c2.number_input("Point y₀:", value=2.0)
            z0 = c3.number_input("Point z₀:", value=-1.0)
            
            d1, d2, d3 = st.columns(3)
            vx = d1.number_input("Direction vx:", value=1.0)
            vy = d2.number_input("Direction vy:", value=2.0)
            vz = d3.number_input("Direction vz:", value=2.0)
            
            if st.button("Compute Gradient & Directional Derivative", type="primary"):
                try:
                    grad_latex, val_dir, steps = MathEngine.symbolic_gradient_and_directional(
                        func_str, {'x': x0, 'y': y0, 'z': z0}, [vx, vy, vz]
                    )
                    st.subheader("Gradient Expression:")
                    st.latex(grad_latex)
                    st.success(f"**Directional Derivative (D_u f):** {val_dir}")
                    with st.expander("🔍 Analytical Steps", expanded=True):
                        for s in steps:
                            st.write(s)
                    log_calculation("Mathematics", "Directional Derivative", f"f={func_str}, pt=({x0},{y0},{z0})", f"D_u f = {val_dir}")
                except Exception as e:
                    st.error(f"Computation error: {str(e)}")

    # --- TAB 2: PHYSICS ---
    with tabs[1]:
        phys_choice = st.selectbox(
            "Select Physics Solver:",
            [
                "Newton's Rings (Radius of Curvature)",
                "Bragg's Law of X-Ray Diffraction",
                "Interplanar Spacing (d_hkl)",
                "Quantum 1D Box Energy Levels",
                "Thin Film Refractive Index",
                "Hall Effect & Carrier Concentration",
                "Classical Kinematics & Mechanics (Force, Work, Power, KE)"
            ]
        )
        
        if phys_choice == "Newton's Rings (Radius of Curvature)":
            c1, c2 = st.columns(2)
            dn_m = c1.number_input("Diameter D_(n+m) (cm):", value=0.65)
            dn = c2.number_input("Diameter D_n (cm):", value=0.35)
            d3, d4 = st.columns(2)
            m_rings = d3.number_input("Ring difference m:", value=10, min_value=1)
            lam_nm = d4.number_input("Wavelength λ (nm):", value=589.0)
            
            if st.button("Calculate Curvature R", type="primary"):
                try:
                    R, derivation = PhysicsEngine.newtons_rings_radius_curvature(dn_m, dn, m_rings, lam_nm)
                    st.success(f"**Radius of Curvature R:** {R} m ({R*100:.2f} cm)")
                    st.code(derivation, language="text")
                    log_calculation("Physics", "Newton's Rings", f"D_n+m={dn_m}, D_n={dn}, m={m_rings}, λ={lam_nm}", f"R={R} m")
                except ValueError as e:
                    st.error(str(e))

        elif phys_choice == "Bragg's Law of X-Ray Diffraction":
            c1, c2, c3 = st.columns(3)
            d_ang = c1.number_input("Interplanar Spacing d (Å):", value=2.82)
            theta = c2.number_input("Glancing Angle θ (degrees):", value=15.0)
            n_ord = c3.number_input("Diffraction Order n:", value=1, min_value=1)
            if st.button("Calculate Wavelength λ", type="primary"):
                lam, der = PhysicsEngine.bragg_law_wavelength(d_ang, theta, n_ord)
                st.success(f"**Wavelength λ:** {lam} Å")
                st.code(der, language="text")
                log_calculation("Physics", "Bragg's Law", f"d={d_ang}, θ={theta}, n={n_ord}", f"λ={lam} Å")

        elif phys_choice == "Interplanar Spacing (d_hkl)":
            c1, c2, c3, c4 = st.columns(4)
            a_val = c1.number_input("Lattice Constant a (Å):", value=4.12)
            h = c2.number_input("Miller index h:", value=1)
            k = c3.number_input("Miller index k:", value=1)
            l = c4.number_input("Miller index l:", value=0)
            if st.button("Calculate Spacing d_hkl", type="primary"):
                try:
                    d, der = PhysicsEngine.interplanar_spacing(a_val, h, k, l)
                    st.success(f"**Interplanar Spacing d:** {d} Å")
                    st.code(der, language="text")
                    log_calculation("Physics", "Interplanar Spacing", f"a={a_val}, (h,k,l)=({h},{k},{l})", f"d={d} Å")
                except ValueError as e:
                    st.error(str(e))

        elif phys_choice == "Quantum 1D Box Energy Levels":
            c1, c2 = st.columns(2)
            n_lvl = c1.number_input("Quantum State n:", value=1, min_value=1)
            L_nm = c2.number_input("Box Width L (nm):", value=1.0)
            if st.button("Calculate Energy State", type="primary"):
                try:
                    e_ev, der = PhysicsEngine.quantum_particle_box_energy(n_lvl, L_nm)
                    st.success(f"**Energy E_{n_lvl}:** {e_ev} eV")
                    st.code(der, language="text")
                    log_calculation("Physics", "Quantum Box", f"n={n_lvl}, L={L_nm}nm", f"E={e_ev} eV")
                except ValueError as e:
                    st.error(str(e))

        elif phys_choice == "Thin Film Refractive Index":
            c1, c2, c3 = st.columns(3)
            lam = c1.number_input("Wavelength λ (nm):", value=600.0)
            t = c2.number_input("Film Thickness t (nm):", value=300.0)
            n_order = c3.number_input("Order n:", value=1)
            if st.button("Calculate Refractive Index μ", type="primary"):
                try:
                    mu, der = PhysicsEngine.thin_film_refractive_index(lam, t, n_order)
                    st.success(f"**Refractive Index μ:** {mu}")
                    st.code(der, language="text")
                    log_calculation("Physics", "Thin Film", f"λ={lam}, t={t}, n={n_order}", f"μ={mu}")
                except ValueError as e:
                    st.error(str(e))

        elif phys_choice == "Hall Effect & Carrier Concentration":
            n_dens = st.number_input("Charge Carrier Density n (m⁻³):", value=1e22, format="%.2e")
            if st.button("Calculate Hall Coefficient R_H", type="primary"):
                try:
                    rh, der = PhysicsEngine.hall_coefficient(n_dens)
                    st.success(f"**Hall Coefficient R_H:** {rh:.4e} m³/C")
                    st.code(der, language="text")
                    log_calculation("Physics", "Hall Effect", f"n={n_dens}", f"R_H={rh:.4e} m³/C")
                except ValueError as e:
                    st.error(str(e))

        elif phys_choice == "Classical Kinematics & Mechanics (Force, Work, Power, KE)":
            calc_type = st.radio("Sub-Calculator:", ["Force (F = ma)", "Work & Power", "Kinetic Energy (½mv²)"], horizontal=True)
            if calc_type == "Force (F = ma)":
                c1, c2 = st.columns(2)
                m = c1.number_input("Mass (kg):", value=10.0)
                a = c2.number_input("Acceleration (m/s²):", value=2.5)
                if st.button("Calculate Force", type="primary"):
                    f, der = PhysicsEngine.calculate_force(m, a)
                    st.success(f"**Force:** {f} N")
                    st.code(der, language="text")
                    log_calculation("Physics", "Force", f"m={m}, a={a}", f"F={f} N")
            elif calc_type == "Work & Power":
                c1, c2, c3 = st.columns(3)
                f = c1.number_input("Force (N):", value=50.0)
                d = c2.number_input("Distance (m):", value=5.0)
                t = c3.number_input("Time (s):", value=2.0)
                if st.button("Calculate Work & Power", type="primary"):
                    try:
                        w, der_w = PhysicsEngine.calculate_work(f, d)
                        p, der_p = PhysicsEngine.calculate_power(w, t)
                        st.success(f"**Work:** {w} J  |  **Power:** {p} W")
                        st.code(f"{der_w}\n{der_p}", language="text")
                        log_calculation("Physics", "Work/Power", f"F={f}, d={d}, t={t}", f"W={w} J, P={p} W")
                    except ValueError as e:
                        st.error(str(e))
            elif calc_type == "Kinetic Energy (½mv²)":
                c1, c2 = st.columns(2)
                m = c1.number_input("Mass (kg):", value=8.0)
                v = c2.number_input("Velocity (m/s):", value=12.0)
                if st.button("Calculate Kinetic Energy", type="primary"):
                    ke, der = PhysicsEngine.calculate_kinetic_energy(m, v)
                    st.success(f"**Kinetic Energy:** {ke} J")
                    st.code(der, language="text")
                    log_calculation("Physics", "Kinetic Energy", f"m={m}, v={v}", f"KE={ke} J")

    # --- TAB 3: ELECTRICAL & MECHANICAL ---
    with tabs[2]:
        ee_choice = st.selectbox(
            "Select Discipline Solver:",
            [
                "Resistor Series & Parallel Combinations",
                "Voltage & Current Divider Rules",
                "Series RLC Circuit Resonance & Q-Factor",
                "Star-Delta (Y-Δ) Transformation",
                "Stress, Strain & Young's Modulus",
                "Carnot Heat Engine Efficiency"
            ]
        )
        
        if ee_choice == "Resistor Series & Parallel Combinations":
            st.info("Enter comma-separated resistance values in Ohms (e.g. 10, 20, 30):")
            r_input = st.text_input("Resistor Values (Ω):", value="10, 20, 30")
            c_type = st.radio("Connection:", ["Series", "Parallel"], horizontal=True)
            if st.button("Calculate Equivalent Resistance", type="primary"):
                try:
                    r_vals = [float(x.strip()) for x in r_input.split(",") if x.strip()]
                    req, exp = EngineeringDisciplineEngine.resistor_combination(r_vals, c_type)
                    st.success(f"**Equivalent Resistance (R_eq):** {req} Ω")
                    st.code(exp, language="text")
                    log_calculation("Electrical", f"Resistors ({c_type})", r_input, f"R_eq={req} Ω")
                except Exception as e:
                    st.error(f"Input error: {str(e)}")

        elif ee_choice == "Voltage & Current Divider Rules":
            rule_mode = st.radio("Divider Mode:", ["Voltage Divider", "Current Divider"], horizontal=True)
            if rule_mode == "Voltage Divider":
                c1, c2, c3 = st.columns(3)
                vin = c1.number_input("Input Voltage V_in (V):", value=12.0)
                r1 = c2.number_input("Resistor R1 (Ω):", value=100.0)
                r2 = c3.number_input("Resistor R2 (Ω):", value=200.0)
                if st.button("Calculate Output Voltage", type="primary"):
                    try:
                        vout, der = EngineeringDisciplineEngine.voltage_divider(vin, r1, r2)
                        st.success(f"**Output Voltage V_out across R2:** {vout} V")
                        st.code(der, language="text")
                        log_calculation("Electrical", "Voltage Divider", f"Vin={vin}, R1={r1}, R2={r2}", f"Vout={vout} V")
                    except ValueError as e:
                        st.error(str(e))
            else:
                c1, c2, c3 = st.columns(3)
                itot = c1.number_input("Total Current I_total (A):", value=6.0)
                r1 = c2.number_input("Branch Resistor R1 (Ω):", value=30.0)
                r2 = c3.number_input("Branch Resistor R2 (Ω):", value=60.0)
                if st.button("Calculate Branch Currents", type="primary"):
                    try:
                        i1, i2, der = EngineeringDisciplineEngine.current_divider(itot, r1, r2)
                        st.success(f"**Current I1:** {i1} A  |  **Current I2:** {i2} A")
                        st.code(der, language="text")
                        log_calculation("Electrical", "Current Divider", f"Itot={itot}, R1={r1}, R2={r2}", f"I1={i1} A, I2={i2} A")
                    except ValueError as e:
                        st.error(str(e))

        elif ee_choice == "Series RLC Circuit Resonance & Q-Factor":
            c1, c2, c3 = st.columns(3)
            r_val = c1.number_input("Resistance R (Ω):", value=10.0)
            l_val = c2.number_input("Inductance L (H):", value=0.05)
            c_val = c3.number_input("Capacitance C (F):", value=1e-5, format="%.2e")
            if st.button("Calculate Resonance Parameters", type="primary"):
                try:
                    f0, q, bw, der = EngineeringDisciplineEngine.rlc_resonance_parameters(r_val, l_val, c_val)
                    st.success(f"**Resonant Frequency f₀:** {f0} Hz  |  **Quality Factor Q:** {q}  |  **Bandwidth:** {bw} Hz")
                    st.code(der, language="text")
                    log_calculation("Electrical", "RLC Resonance", f"R={r_val}, L={l_val}, C={c_val}", f"f0={f0} Hz, Q={q}")
                except ValueError as e:
                    st.error(str(e))

        elif ee_choice == "Star-Delta (Y-Δ) Transformation":
            c1, c2, c3 = st.columns(3)
            ra = c1.number_input("Star Ra (Ω):", value=10.0)
            rb = c2.number_input("Star Rb (Ω):", value=20.0)
            rc = c3.number_input("Star Rc (Ω):", value=30.0)
            if st.button("Convert to Delta Network", type="primary"):
                try:
                    rab, rbc, rca, der = EngineeringDisciplineEngine.star_to_delta(ra, rb, rc)
                    st.success(f"**Delta Resistors:** Rab = {rab} Ω, Rbc = {rbc} Ω, Rca = {rca} Ω")
                    st.code(der, language="text")
                    log_calculation("Electrical", "Star-Delta", f"Ra={ra}, Rb={rb}, Rc={rc}", f"Rab={rab}, Rbc={rbc}, Rca={rca}")
                except ValueError as e:
                    st.error(str(e))

        elif ee_choice == "Stress, Strain & Young's Modulus":
            c1, c2 = st.columns(2)
            force = c1.number_input("Applied Force F (N):", value=5000.0)
            area = c2.number_input("Cross-sectional Area A (m²):", value=0.002)
            d1, d2 = st.columns(2)
            delta_l = d1.number_input("Elongation ΔL (m):", value=0.0005)
            orig_l = d2.number_input("Original Length L₀ (m):", value=1.0)
            if st.button("Calculate Elasticity Parameters", type="primary"):
                try:
                    stress, strain, E, der = EngineeringDisciplineEngine.stress_strain_modulus(force, area, delta_l, orig_l)
                    st.success(f"**Stress σ:** {stress} Pa  |  **Strain ε:** {strain}  |  **Young's Modulus E:** {E:.2e} Pa")
                    st.code(der, language="text")
                    log_calculation("Mechanical", "Young's Modulus", f"F={force}, A={area}, ΔL={delta_l}, L0={orig_l}", f"E={E:.2e} Pa")
                except ValueError as e:
                    st.error(str(e))

        elif ee_choice == "Carnot Heat Engine Efficiency":
            c1, c2 = st.columns(2)
            thot = c1.number_input("Source Temperature T_hot (K):", value=600.0)
            tcold = c2.number_input("Sink Temperature T_cold (K):", value=300.0)
            if st.button("Calculate Efficiency", type="primary"):
                try:
                    eta, der = EngineeringDisciplineEngine.carnot_efficiency(thot, tcold)
                    st.success(f"**Carnot Efficiency η:** {eta}%")
                    st.code(der, language="text")
                    log_calculation("Mechanical", "Carnot Efficiency", f"Thot={thot}K, Tcold={tcold}K", f"η={eta}%")
                except ValueError as e:
                    st.error(str(e))

# ==========================================================
# 3. EXPERIMENTAL CURVE FITTING & REGRESSION
# ==========================================================
elif selected_section == "🔬 Experimental Curve Fitting":
    st.title("🔬 Experimental Data Curve Fitting & Linear Regression")
    st.caption("Perform least-squares linear regression (y = mx + c), find R², and plot scatter trendlines for physics/engineering lab data")
    st.markdown("---")
    
    preset = st.selectbox(
        "Load Sample Lab Experiment Preset:",
        [
            "Custom Data",
            "Ohm's Law Experiment (Voltage vs Current)",
            "Hooke's Law (Spring Force vs Extension)",
            "Newton's Rings (Fringe Order n vs Ring Diameter² D²)"
        ]
    )
    
    if preset == "Ohm's Law Experiment (Voltage vs Current)":
        default_x = "0.1, 0.2, 0.3, 0.4, 0.5, 0.6"
        default_y = "1.2, 2.3, 3.6, 4.9, 6.1, 7.3"
        x_label, y_label = "Current I (A)", "Voltage V (V)"
    elif preset == "Hooke's Law (Spring Force vs Extension)":
        default_x = "0.01, 0.02, 0.03, 0.04, 0.05"
        default_y = "0.49, 0.98, 1.48, 1.95, 2.45"
        x_label, y_label = "Extension Δx (m)", "Spring Force F (N)"
    elif preset == "Newton's Rings (Fringe Order n vs Ring Diameter² D²)":
        default_x = "1, 2, 3, 4, 5, 6"
        default_y = "0.12, 0.25, 0.38, 0.50, 0.62, 0.76"
        x_label, y_label = "Fringe Order n", "Diameter² D² (cm²)"
    else:
        default_x = "1.0, 2.0, 3.0, 4.0, 5.0"
        default_y = "2.1, 3.9, 6.2, 7.9, 10.1"
        x_label, y_label = "Independent X", "Dependent Y"
        
    c1, c2 = st.columns(2)
    x_input = c1.text_area("X Values (comma-separated):", value=default_x)
    y_input = c2.text_area("Y Values (comma-separated):", value=default_y)
    
    if st.button("Fit Trendline & Analyze Data", type="primary"):
        try:
            x_vals = [float(val.strip()) for val in x_input.split(",") if val.strip()]
            y_vals = [float(val.strip()) for val in y_input.split(",") if val.strip()]
            
            slope, intercept, r2, derivation = AdvancedLabEngine.linear_regression(x_vals, y_vals)
            
            st.success(f"### Fitted Line Equation: **y = {slope:.4f}x {'+' if intercept >= 0 else '-'} {abs(intercept):.4f}**")
            
            m1, m2, m3 = st.columns(3)
            m1.metric("Slope (m)", f"{slope:.4f}")
            m2.metric("Y-Intercept (c)", f"{intercept:.4f}")
            m3.metric("R² Determination", f"{r2:.4f}")
            
            # Interactive Trendline Plot
            fig = EngineeringVisualizer.plot_curve_fit(x_vals, y_vals, slope, intercept, r2)
            st.plotly_chart(fig, use_container_width=True)
            
            with st.expander("🔍 Derivation & Regression Formulas", expanded=True):
                for s in derivation:
                    st.write(f"- {s}")
                    
            log_calculation("Experimental Lab", "Linear Regression", f"N={len(x_vals)} pts", f"y={slope:.4f}x+{intercept:.4f}, R²={r2:.4f}")
        except Exception as e:
            st.error(f"Fitting error: {str(e)}")

# ==========================================================
# 4. FOURIER HARMONIC SYNTHESIZER
# ==========================================================
elif selected_section == "🌊 Fourier Harmonic Synthesizer":
    st.title("🌊 Fourier Series & Waveform Harmonic Synthesizer")
    st.caption("Synthesize periodic signals from sinusoidal harmonics and observe Gibbs phenomenon in real-time (JNTUK LA&C Unit V)")
    st.markdown("---")
    
    c1, c2 = st.columns([1, 2])
    with c1:
        wave_type = st.radio("Target Waveform:", ["Square Wave", "Sawtooth Wave", "Triangular Wave"])
        n_harmonics = st.slider("Number of Harmonics (N):", min_value=1, max_value=40, value=7, step=1)
        
        st.markdown(r"""
        **Fourier Analysis Notes:**
        - **Square Wave:** Contains only odd harmonics $\sum \frac{1}{n}\sin(nt)$.
        - **Sawtooth Wave:** Contains both even and odd harmonics.
        - **Gibbs Phenomenon:** ~9% overshoot at discontinuities that does not vanish even as $N \to \infty$.
        """)
        
    with c2:
        fig = EngineeringVisualizer.plot_fourier_series(wave_type, n_harmonics)
        st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# 5. BEAM SFD & BMD ANALYZER
# ==========================================================
elif selected_section == "🏗️ Beam SFD & BMD Analyzer":
    st.title("🏗️ Beam Shear Force & Bending Moment Diagrams (SFD & BMD)")
    st.caption("Calculate support reactions and plot interactive SFD and BMD curves for simply supported structural beams")
    st.markdown("---")
    
    c1, c2 = st.columns(2)
    span_l = c1.number_input("Beam Span Length L (m):", value=6.0, min_value=1.0)
    l_type = c2.selectbox("Loading Condition:", ["Point Load", "Uniformly Distributed Load (UDL)"])
    
    d1, d2 = st.columns(2)
    if l_type == "Point Load":
        p_val = d1.number_input("Load Magnitude P (kN):", value=15.0)
        p_pos = d2.number_input("Load Position from Left Support (m):", value=2.0, min_value=0.1, max_value=span_l)
    else:
        p_val = d1.number_input("UDL Intensity w (kN/m):", value=5.0)
        p_pos = span_l / 2.0
        d2.info(f"UDL acting across full span [0 to {span_l} m]")
        
    if st.button("Generate SFD & BMD Diagrams", type="primary"):
        try:
            x_pts, sfd_pts, bmd_pts, ra, rb, max_m, details = AdvancedLabEngine.calculate_sfd_bmd(
                span_l, l_type, p_val, p_pos
            )
            
            r1, r2, r3 = st.columns(3)
            r1.metric("Reaction R_A (Left)", f"{ra:.2f} kN")
            r2.metric("Reaction R_B (Right)", f"{rb:.2f} kN")
            r3.metric("Maximum Moment M_max", f"{max_m:.2f} kN·m")
            
            fig = EngineeringVisualizer.plot_sfd_bmd(x_pts, sfd_pts, bmd_pts, span_l, max_m)
            st.plotly_chart(fig, use_container_width=True)
            
            with st.expander("🔍 Structural Equilibrium Analysis", expanded=True):
                for d in details:
                    st.write(f"- {d}")
                    
            log_calculation("Structural Mechanics", f"SFD/BMD ({l_type})", f"L={span_l}m, Load={p_val}", f"Ra={ra:.2f}kN, Rb={rb:.2f}kN, Mmax={max_m:.2f}kN·m")
        except Exception as e:
            st.error(str(e))

# ==========================================================
# 6. VIBRATIONS & ODE DYNAMICS
# ==========================================================
elif selected_section == "🌀 Vibrations & ODE Dynamics":
    st.title("🌀 Mechanical Vibrations & 2nd Order ODEs")
    st.caption("Solves m·x''(t) + c·x'(t) + k·x(t) = 0 and classifies dynamic response (Underdamped, Critically Damped, Overdamped)")
    st.markdown("---")
    
    c1, c2, c3 = st.columns(3)
    m_kg = c1.number_input("Mass m (kg):", value=2.0, min_value=0.1)
    c_damp = c2.number_input("Damping Coefficient c (N·s/m):", value=1.5, min_value=0.0)
    k_stiff = c3.number_input("Spring Stiffness k (N/m):", value=50.0, min_value=0.1)
    
    d1, d2, d3 = st.columns(3)
    x0_val = d1.number_input("Initial Displacement x₀ (m):", value=1.0)
    v0_val = d2.number_input("Initial Velocity v₀ (m/s):", value=0.0)
    t_span = d3.slider("Simulation Time (s):", 2.0, 30.0, 10.0)
    
    if st.button("Solve Vibration Dynamics", type="primary"):
        try:
            t_arr, x_arr, w_n, z_ratio, w_d, regime, details = AdvancedLabEngine.solve_spring_mass_damper(
                m_kg, c_damp, k_stiff, x0_val, v0_val, t_span
            )
            
            st.subheader(f"System State: **{regime}**")
            k1, k2, k3 = st.columns(3)
            k1.metric("Natural Frequency ωₙ", f"{w_n:.3f} rad/s")
            k2.metric("Damping Ratio ζ", f"{z_ratio:.3f}")
            k3.metric("Damped Frequency ω_d", f"{w_d:.3f} rad/s" if z_ratio < 1.0 else "N/A")
            
            fig = EngineeringVisualizer.plot_vibration_response(t_arr, x_arr, w_n, z_ratio, regime)
            st.plotly_chart(fig, use_container_width=True)
            
            with st.expander("🔍 ODE Characteristic Roots & Parameters", expanded=True):
                for item in details:
                    st.write(f"- {item}")
                    
            log_calculation("Dynamics & ODE", "Vibrations", f"m={m_kg}, c={c_damp}, k={k_stiff}", f"ζ={z_ratio:.3f}, Regime={regime}")
        except Exception as e:
            st.error(str(e))

# ==========================================================
# 7. 3D MULTIVARIABLE SURFACES
# ==========================================================
elif selected_section == "🏔️ 3D Multivariable Surfaces":
    st.title("🏔️ 3D Multivariable Calculus Topography Plotter")
    st.caption("Interactive 3D surfaces and projected contour level curves (LA&C Unit III & IV)")
    st.markdown("---")
    
    c1, c2 = st.columns([1, 2])
    with c1:
        surface_sel = st.selectbox(
            "Select Multivariable Surface:",
            [
                "Saddle Surface (z = x² - y²)",
                "Elliptic Paraboloid (z = x² + y²)",
                "Damped Bessel Ripple Wave (z = sin(r)/r)",
                "Monkey Saddle Surface (z = x³ - 3xy²)"
            ]
        )
        range_val = st.slider("Coordinate Domain Range [-L, L]:", 1.0, 8.0, 3.0, step=0.5)
        
        st.info("""
        **Calculus Insights:**
        - **Saddle Point:** Stationarity where $\\nabla f = 0$ but eigenvalues of the Hessian matrix have opposite signs.
        - **Contour Projections:** Orthogonal 2D level curves where $f(x, y) = c$.
        """)
        
    with c2:
        fig_surf = EngineeringVisualizer.plot_3d_surface(surface_sel, range_val)
        st.plotly_chart(fig_surf, use_container_width=True)

# ==========================================================
# 8. 3D & 2D PHYSICS VISUALS
# ==========================================================
elif selected_section == "📈 3D & 2D Physics Visuals":
    st.title("📈 Interactive Engineering Visualizations")
    st.caption("3D Vector spaces, Quantum box wavefunctions, Newton's Rings interferogram, and RLC resonance")
    st.markdown("---")
    
    vis_type = st.selectbox(
        "Choose Visual Simulator:",
        [
            "3D Vector Space & Cross Product",
            "Quantum Particle in a Box (Wavefunction & Probability)",
            "Newton's Rings 2D Fringe Simulator",
            "Kinematics Motion (s-t and v-t curves)",
            "Series RLC Circuit Resonance Frequency Response"
        ]
    )
    
    if vis_type == "3D Vector Space & Cross Product":
        c1, c2, c3 = st.columns(3)
        ax = c1.slider("Vector A - X", -10.0, 10.0, 3.0)
        ay = c2.slider("Vector A - Y", -10.0, 10.0, 4.0)
        az = c3.slider("Vector A - Z", -10.0, 10.0, 2.0)
        
        d1, d2, d3 = st.columns(3)
        bx = d1.slider("Vector B - X", -10.0, 10.0, 1.0)
        by = d2.slider("Vector B - Y", -10.0, 10.0, -3.0)
        bz = d3.slider("Vector B - Z", -10.0, 10.0, 4.0)
        
        show_cross = st.checkbox("Display Cross Product Vector (A × B)", value=True)
        fig, cross_val = EngineeringVisualizer.plot_3d_vectors(ax, ay, az, bx, by, bz, show_cross)
        st.plotly_chart(fig, use_container_width=True)
        if show_cross:
            st.info(f"**Computed Cross Product Vector:** `{cross_val}`")

    elif vis_type == "Quantum Particle in a Box (Wavefunction & Probability)":
        c1, c2 = st.columns(2)
        n_quant = c1.slider("Principal Quantum Number (n)", min_value=1, max_value=6, value=2)
        L_width = c2.slider("Potential Well Width L (nm)", min_value=0.5, max_value=5.0, value=1.0, step=0.1)
        fig = EngineeringVisualizer.plot_particle_in_box(n_quant, L_width)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Notice: Number of antinodes in ψ equals n. Probability density |ψ|² represents likelihood of detecting the electron.")

    elif vis_type == "Newton's Rings 2D Fringe Simulator":
        c1, c2 = st.columns(2)
        w_nm = c1.slider("Light Wavelength λ (nm)", 400.0, 750.0, 589.0)
        r_m = c2.slider("Lens Radius of Curvature R (m)", 0.2, 3.0, 1.0, step=0.1)
        fig = EngineeringVisualizer.plot_newtons_rings(w_nm, r_m)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Interference fringes between reflected waves. The center spot is dark due to π phase reversal upon reflection.")

    elif vis_type == "Kinematics Motion (s-t and v-t curves)":
        c1, c2, c3 = st.columns(3)
        u_init = c1.number_input("Initial Velocity u (m/s):", value=5.0)
        a_acc = c2.number_input("Acceleration a (m/s²):", value=2.0)
        t_duration = c3.slider("Time Duration (s):", 1.0, 30.0, 10.0)
        fig = EngineeringVisualizer.plot_kinematics(u_init, a_acc, t_duration)
        st.plotly_chart(fig, use_container_width=True)

    elif vis_type == "Series RLC Circuit Resonance Frequency Response":
        c1, c2, c3 = st.columns(3)
        r_ohm = c1.slider("Resistance R (Ω)", 1.0, 50.0, 10.0)
        l_mh = c2.slider("Inductance L (mH)", 1.0, 200.0, 20.0)
        c_uf = c3.slider("Capacitance C (µF)", 0.1, 50.0, 5.0)
        fig, f0_val, q_val = EngineeringVisualizer.plot_rlc_resonance(r_ohm, l_mh, c_uf)
        st.plotly_chart(fig, use_container_width=True)
        st.success(f"**Resonant Frequency f₀:** {f0_val} Hz  |  **Quality Factor Q:** {q_val}")

# ==========================================================
# 9. AI ASSISTANT & FORMULA SEARCH
# ==========================================================
elif selected_section == "🤖 AI Assistant & Search":
    st.title("🤖 Rule-Based & Generative AI Assistant")
    st.caption("Natural language query processor and syllabus guidance for engineering students")
    st.markdown("---")
    
    st.subheader("🔍 Ask Any Formula or Scientific Concept")
    user_q = st.text_input(
        "Type your question (e.g. 'Linear regression formula', 'Fourier harmonics', 'Beam SFD BMD', 'RLC resonance frequency'):"
    )
    
    col_search, col_gemini = st.columns([1, 1])
    with col_search:
        search_clicked = st.button("Search Knowledge Engine", type="primary")
    with col_gemini:
        enable_gemini = st.checkbox("Enable Generative AI Explanations (Requires Gemini API Key)")
        
    api_key = ""
    if enable_gemini:
        api_key = st.text_input("Enter Gemini API Key (Optional):", type="password")
        
    if search_clicked:
        matched, msg = ai_engine.process_query(user_q)
        if matched:
            st.success(f"**Identified Subject & Topic:** {matched['category']} — **{matched['name']}**")
            st.markdown(f"<div class='formula-box'><b>Formula:</b> {matched['formula']}</div>", unsafe_allow_html=True)
            st.info(f"**Engineering Logic:**\n\n{matched['explanation']}\n\n*{msg}*")
        else:
            st.warning(msg)
            
        if enable_gemini and api_key and user_q:
            try:
                import google.generativeai as genai
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                with st.spinner("Consulting Gemini AI tutor..."):
                    resp = model.generate_content(f"You are an engineering tutor for B.Tech students. Answer this engineering question concisely with relevant formulas: {user_q}")
                    st.subheader("💡 Generative AI Detailed Solution:")
                    st.write(resp.text)
            except Exception as e:
                st.error(f"Gemini API Error: {str(e)}")

# ==========================================================
# 10. PRACTICE QUIZ & SELF-TEST
# ==========================================================
elif selected_section == "🎯 Practice Quiz & Self-Test":
    st.title("🎯 Formula Practice & Self-Assessment")
    st.caption("Test your conceptual mastery across Engineering Mathematics, Physics, and Electrical Circuits")
    st.markdown("---")
    
    questions = QuizEngine.get_all_questions()
    
    if "quiz_answers" not in st.session_state:
        st.session_state["quiz_answers"] = {}
        
    total_q = len(questions)
    for q in questions:
        qid = q["id"]
        st.markdown(f"#### Q{qid}. [{q['subject']}] {q['question']}")
        st.session_state["quiz_answers"][qid] = st.radio(
            "Choose option:",
            q["options"],
            key=f"quiz_opt_{qid}"
        )
        st.markdown("---")
        
    if st.button("Submit & Evaluate Answers", type="primary"):
        score = 0
        st.subheader("📊 Quiz Evaluation Report")
        for q in questions:
            qid = q["id"]
            user_ans = st.session_state["quiz_answers"].get(qid)
            corr_ans = q["options"][q["correct_idx"]]
            
            if user_ans == corr_ans:
                score += 1
                st.success(f"✅ **Q{qid}: Correct!**\n\n*{q['explanation']}*")
            else:
                st.error(f"❌ **Q{qid}: Incorrect.** Your answer: `{user_ans}` | Correct: `{corr_ans}`\n\n*{q['explanation']}*")
                
        pct = (score / total_q) * 100
        st.markdown(f"### 🏆 Total Score: **{score} / {total_q} ({pct:.1f}%)**")

# ==========================================================
# 11. UNIT CONVERTER & CONSTANTS
# ==========================================================
elif selected_section == "🔄 Unit Converter & Constants":
    st.title("🔄 Engineering Unit Converter & Physical Constants")
    st.caption("Standard factor-label unit conversions and fundamental universal constants")
    st.markdown("---")
    
    subtab1, subtab2 = st.tabs(["🔄 Multi-Unit Converter", "📚 Universal Physical Constants"])
    
    with subtab1:
        cat = st.selectbox("Select Dimension Category:", list(EngineeringConverter.UNIT_CATEGORIES.keys()))
        units = list(EngineeringConverter.UNIT_CATEGORIES[cat].keys())
        
        c1, c2, c3 = st.columns(3)
        val_in = c1.number_input("Value to Convert:", value=1.0)
        from_u = c2.selectbox("From Unit:", units, index=0)
        to_u = c3.selectbox("To Unit:", units, index=1 if len(units) > 1 else 0)
        
        if st.button("Convert Unit", type="primary"):
            converted = EngineeringConverter.convert(cat, val_in, from_u, to_u)
            st.success(f"**Result:** {val_in} {from_u} = **{converted:.6e}** {to_u} ({converted:.6f})")
            
    with subtab2:
        st.subheader("Fundamental Scientific & Engineering Constants")
        const_data = EngineeringConverter.CONSTANTS
        st.table(const_data)

# ==========================================================
# 12. LIVE SESSION HISTORY & NOTEBOOK
# ==========================================================
elif selected_section == "🕒 Session History & Notebook":
    st.title("🕒 Live Session History & Notebook")
    st.caption("Persistent log of all mathematical, physical, and engineering computations conducted in your session")
    st.markdown("---")
    
    history_list = st.session_state["calc_history"]
    if not history_list:
        st.info("No calculations performed yet in this session. Run any calculator, regression, or structural solver to see it recorded here!")
    else:
        df_hist = pd.DataFrame(history_list)
        st.dataframe(df_hist, use_container_width=True)
        
        csv_data = df_hist.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Export Session History (CSV)",
            data=csv_data,
            file_name=f"calculation_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
        
        if st.button("Clear Session History"):
            st.session_state["calc_history"] = []
            st.experimental_rerun()

# ==========================================================
# 13. EXPORT LAB REPORT
# ==========================================================
elif selected_section == "📄 Export Lab Report":
    st.title("📄 Export Lab / Assignment Report")
    st.caption("Generate formatted academic lab computation sheets ready for printing or submission")
    st.markdown("---")
    
    c1, c2, c3 = st.columns(3)
    s_name = c1.text_input("Student Name:", value="Prasanna")
    r_no = c2.text_input("Roll Number / Registration ID:", value="23A91A0501")
    s_subj = c3.selectbox("Subject:", ["Linear Algebra & Calculus", "Engineering Physics", "Basic Electrical Engineering", "Structural Mechanics"])
    
    prob_title = st.text_input("Experiment / Problem Title:", value="Linear Regression & Trendline Analysis")
    
    st.subheader("Input Values (JSON or Key-Value text):")
    inputs_raw = st.text_area("Given Inputs:", value="X Data: [0.1, 0.2, 0.3, 0.4, 0.5]\nY Data: [1.2, 2.3, 3.6, 4.9, 6.1]")
    
    st.subheader("Step-by-Step Mathematical Derivation:")
    steps_raw = st.text_area(
        "Steps (one per line):",
        value="Compute Sum(X) = 1.5, Sum(Y) = 18.1\nSlope m = (N*Sum(XY) - Sum(X)*Sum(Y)) / (N*Sum(X^2) - Sum(X)^2) = 12.30\nIntercept c = (Sum(Y) - m*Sum(X)) / N = -0.07\nModel: y = 12.30x - 0.07\nR^2 Determination = 0.998"
    )
    
    st.subheader("Final Output Summary:")
    res_raw = st.text_area("Final Result:", value="Slope m = 12.30, Intercept c = -0.07, R^2 = 0.998 (99.8% Accuracy)")
    
    if st.button("Generate Formatted Academic Report", type="primary"):
        in_dict = {f"Param {i+1}": line.strip() for i, line in enumerate(inputs_raw.split("\n")) if line.strip()}
        st_list = [line.strip() for line in steps_raw.split("\n") if line.strip()]
        
        report_md = ReportGenerator.generate_markdown_report(
            s_name, r_no, s_subj, prob_title, in_dict, st_list, res_raw
        )
        
        st.markdown("---")
        st.subheader("Preview Report:")
        st.markdown(report_md)
        
        st.download_button(
            label="📥 Download Academic Report (.md)",
            data=report_md,
            file_name=f"lab_report_{r_no}.md",
            mime="text/markdown"
        )

# ==========================================================
# 14. ABOUT & CURRICULUM
# ==========================================================
elif selected_section == "ℹ️ About & Curriculum":
    st.title("ℹ️ About the Engineering Platform")
    st.markdown("---")
    st.write("""
    ### 🎓 Project Motivation & Scope
    This project bridges theoretical B.Tech engineering coursework with laboratory computations and real-time interactive simulations.
    Aligned with the **JNTUK R23 B.Tech** curriculum across Mathematics, Physics, Electrical, Mechanical, and Civil branches.
    
    ### 🛠️ Architecture & Technologies
    - **UI Engine:** Streamlit with customized glassmorphic design system
    - **Symbolic Mathematics:** SymPy (exact characteristic polynomials, symbolic gradients, LU solver)
    - **Interactive Visualizations:** Plotly 3D & 2D (WebGL-accelerated vector fields, surfaces, waveforms, SFD/BMD)
    - **Data Lab:** NumPy numerical least-squares curve fitting and ODE damping solvers
    - **NLP Pipeline:** Custom Rule-Based Natural Language Processing with weighted keyword scoring
    - **Session Notebook:** Persistent session calculation notebook with CSV export
    """)
    st.success("Project version 3.0 with Advanced Engineering Lab & Simulation Suite Live!")
