import os
import tkinter as tk
from tkinter import ttk, messagebox

# Import modular engines
from modules.math_engine import MathEngine
from modules.physics_engine import PhysicsEngine
from modules.ai_engine import RuleBasedAIEngine


class EngineeringCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.ai_engine = RuleBasedAIEngine()

        self.root.title("Formula Calculator for Engineering Subjects - B.Tech Project")
        self.window_width = 1024
        self.window_height = 700
        self.center_window()
        self.root.minsize(900, 600)
        self.root.configure(bg="#F1F5F9")

        self.create_header()
        self.configure_styles()
        self.create_tabs()

        self.build_home_tab()
        self.build_subjects_tab()
        self.build_programming_tab()
        self.build_ai_tab()
        self.build_live_demo_tab()
        self.build_about_tab()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (self.window_width / 2))
        y_coordinate = int((screen_height / 2) - (self.window_height / 2))
        self.root.geometry(f"{self.window_width}x{self.window_height}+{x_coordinate}+{y_coordinate}")

    def create_header(self):
        header_frame = tk.Frame(self.root, bg="#1E293B", height=75)
        header_frame.pack(side="top", fill="x")
        header_frame.pack_propagate(False)

        title_label = tk.Label(
            header_frame,
            text="ENGINEERING FORMULA CALCULATOR",
            font=("Helvetica", 16, "bold"),
            fg="#F8FAFC",
            bg="#1E293B"
        )
        title_label.pack(pady=(12, 2))

        subtitle_label = tk.Label(
            header_frame,
            text="Smart Computational & AI Formula Suggestion System | B.Tech Project",
            font=("Helvetica", 9, "italic"),
            fg="#94A3B8",
            bg="#1E293B"
        )
        subtitle_label.pack()

    def configure_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure("TNotebook", background="#F1F5F9", borderwidth=0)
        self.style.configure(
            "TNotebook.Tab",
            font=("Helvetica", 10, "bold"),
            padding=[14, 8],
            background="#CBD5E1",
            foreground="#334155",
            borderwidth=0
        )
        self.style.map(
            "TNotebook.Tab",
            background=[("selected", "#0F172A")],
            foreground=[("selected", "#FFFFFF")]
        )

    def create_tabs(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=15, pady=15)

        self.tabs = {}
        tab_titles = ["Home", "Subjects Used", "Programming Used", "AI/ML Layer", "Live Demo", "About Project"]

        for title in tab_titles:
            frame = tk.Frame(self.notebook, bg="#FFFFFF")
            self.notebook.add(frame, text=f"  {title}  ")
            self.tabs[title] = frame

    def build_home_tab(self):
        home_frame = self.tabs["Home"]
        main_container = tk.Frame(home_frame, bg="#FFFFFF", padx=20, pady=20)
        main_container.pack(fill="both", expand=True)

        meta_card = tk.LabelFrame(
            main_container,
            text=" Project Overview & Academic Info ",
            font=("Helvetica", 11, "bold"),
            fg="#0F172A",
            bg="#FFFFFF",
            bd=1,
            relief="solid",
            padx=15,
            pady=15
        )
        meta_card.pack(fill="x", pady=(0, 15))

        info_items = [
            ("Project Title:", "Engineering Formula Calculator"),
            ("Institution:", "Department of Computer Science & Engineering"),
            ("Course & Year:", "B.Tech II Year (Semester I & II)"),
            ("Curriculum:", "JNTUK Regulation R23 Approved"),
            ("Team Members:", "Student Developer (Roll No: 2XX1A05XX)")
        ]

        for row_idx, (label_text, val_text) in enumerate(info_items):
            lbl = tk.Label(meta_card, text=label_text, font=("Helvetica", 10, "bold"), fg="#334155", bg="#FFFFFF", anchor="w")
            lbl.grid(row=row_idx, column=0, sticky="w", pady=4, padx=(0, 15))
            val = tk.Label(meta_card, text=val_text, font=("Helvetica", 10), fg="#0F172A", bg="#FFFFFF", anchor="w")
            val.grid(row=row_idx, column=1, sticky="w", pady=4)

        split_frame = tk.Frame(main_container, bg="#FFFFFF")
        split_frame.pack(fill="both", expand=True)

        obj_card = tk.LabelFrame(
            split_frame,
            text=" Key Project Objectives ",
            font=("Helvetica", 11, "bold"),
            fg="#0F172A",
            bg="#FFFFFF",
            bd=1,
            relief="solid",
            padx=15,
            pady=15
        )
        obj_card.pack(side="left", fill="both", expand=True, padx=(0, 10))

        objectives = [
            "• Perform Matrix Addition, Multiplication, Inverse, and Rank for 2x2 and 3x3 Matrices.",
            "• Calculate Multivariable Calculus concepts (Jacobians, Directional Derivatives).",
            "• Provide Classical Physics (Force, Work, KE) & R23 Physics (Bragg's Law, d_hkl, Hall Effect).",
            "• Natural language search assistant powered by a Rule-Based NLP engine.",
            "• Full defensive error handling against zero-division and input errors."
        ]

        for obj in objectives:
            o_lbl = tk.Label(obj_card, text=obj, font=("Helvetica", 9), fg="#475569", bg="#FFFFFF", anchor="w", justify="left")
            o_lbl.pack(anchor="w", pady=5)

    def build_subjects_tab(self):
        sub_frame = self.tabs["Subjects Used"]
        container = tk.Frame(sub_frame, bg="#FFFFFF", padx=20, pady=20)
        container.pack(fill="both", expand=True)

        math_card = tk.LabelFrame(container, text=" Linear Algebra & Calculus (LA&C) ", font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#FFFFFF", padx=15, pady=15)
        math_card.pack(fill="x", pady=(0, 15))

        math_topics = [
            ("Unit I & II (Matrices):", "Matrix Addition, Matrix Multiplication, Echelon Rank, 2x2/3x3 Inverse, Eigenvalues."),
            ("Unit III, IV & V (Calculus):", "Lagrange MVT, Directional Derivative, Jacobians, Multiple Integrals.")
        ]
        for title, desc in math_topics:
            tk.Label(math_card, text=title, font=("Helvetica", 10, "bold"), fg="#2563EB", bg="#FFFFFF").pack(anchor="w", pady=(3, 0))
            tk.Label(math_card, text=desc, font=("Helvetica", 9), fg="#334155", bg="#FFFFFF", justify="left", wraplength=900).pack(anchor="w", pady=(0, 5))

        phy_card = tk.LabelFrame(container, text=" Engineering Physics ", font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#FFFFFF", padx=15, pady=15)
        phy_card.pack(fill="x")

        phy_topics = [
            ("Classical Mechanics & Circuits:", "Force F=ma, Work W=Fd, Power P=W/t, Kinetic Energy KE=0.5mv^2, Ohm's Law."),
            ("JNTUK R23 Modern Physics:", "Miller Indices d_hkl, Bragg's Law 2d sin(theta)=n lambda, Newton's Rings, 1D Box Quantum Energy, Hall Effect.")
        ]
        for title, desc in phy_topics:
            tk.Label(phy_card, text=title, font=("Helvetica", 10, "bold"), fg="#166534", bg="#FFFFFF").pack(anchor="w", pady=(3, 0))
            tk.Label(phy_card, text=desc, font=("Helvetica", 9), fg="#334155", bg="#FFFFFF", justify="left", wraplength=900).pack(anchor="w", pady=(0, 5))

    def build_programming_tab(self):
        prog_frame = self.tabs["Programming Used"]
        container = tk.Frame(prog_frame, bg="#FFFFFF", padx=20, pady=20)
        container.pack(fill="both", expand=True)

        card = tk.LabelFrame(container, text=" Programming Architecture & Frameworks ", font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#FFFFFF", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        concepts = [
            ("• Python 3.x Modular Design:", "Logic divided across `math_engine.py`, `physics_engine.py`, and `ai_engine.py`."),
            ("• Tkinter Desktop GUI:", "Native desktop interface with multi-grid input controls."),
            ("• Streamlit Dashboard:", "Web-based responsive UI with live calculators.")
        ]

        for title, desc in concepts:
            tk.Label(card, text=title, font=("Helvetica", 10, "bold"), fg="#0F172A", bg="#FFFFFF").pack(anchor="w", pady=(4, 0))
            tk.Label(card, text=desc, font=("Helvetica", 9), fg="#475569", bg="#FFFFFF", justify="left", wraplength=880).pack(anchor="w", pady=(0, 6))

    def build_ai_tab(self):
        ai_frame = self.tabs["AI/ML Layer"]
        container = tk.Frame(ai_frame, bg="#FFFFFF", padx=20, pady=20)
        container.pack(fill="both", expand=True)

        query_card = tk.LabelFrame(container, text=" JNTUK R23 AI Formula Assistant ", font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#FFFFFF", padx=15, pady=15)
        query_card.pack(fill="both", expand=True)

        input_box_frame = tk.Frame(query_card, bg="#FFFFFF")
        input_box_frame.pack(fill="x", pady=(0, 15))

        tk.Label(input_box_frame, text="Type your query:", font=("Helvetica", 10, "bold"), bg="#FFFFFF", fg="#0F172A").pack(anchor="w", pady=(0, 5))

        self.ai_query_entry = ttk.Entry(input_box_frame, font=("Helvetica", 11), width=60)
        self.ai_query_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.ai_query_entry.insert(0, "Matrix Multiplication")

        tk.Button(
            input_box_frame,
            text="Search AI Rules",
            bg="#2563EB",
            fg="#FFFFFF",
            font=("Helvetica", 10, "bold"),
            padx=15,
            pady=5,
            command=self.handle_ai_query,
            cursor="hand2"
        ).pack(side="left")

        self.ai_res_card = tk.Frame(query_card, bg="#F8FAFC", bd=1, relief="solid", padx=15, pady=15)
        self.ai_res_card.pack(fill="both", expand=True)

        self.ai_title_lbl = tk.Label(self.ai_res_card, text="AI Recommendation Output", font=("Helvetica", 12, "bold"), fg="#0F172A", bg="#F8FAFC")
        self.ai_title_lbl.pack(anchor="w", pady=(0, 5))

        self.ai_formula_lbl = tk.Label(self.ai_res_card, text="Recommended Formula: --", font=("Helvetica", 11, "bold"), fg="#2563EB", bg="#F8FAFC")
        self.ai_formula_lbl.pack(anchor="w", pady=(0, 5))

        self.ai_desc_lbl = tk.Label(self.ai_res_card, text="Type a query above and click 'Search AI Rules'.", font=("Helvetica", 10), fg="#475569", bg="#F8FAFC", justify="left")
        self.ai_desc_lbl.pack(anchor="w")

    def handle_ai_query(self):
        query = self.ai_query_entry.get()
        matched_rule, msg = self.ai_engine.process_query(query)

        if matched_rule:
            self.ai_title_lbl.config(text=f"AI Suggestion: {matched_rule['name']} ({matched_rule['category']})", fg="#166534")
            self.ai_formula_lbl.config(text=f"Formula: {matched_rule['formula']}")
            self.ai_desc_lbl.config(text=f"{matched_rule['explanation']}\n\n[{msg}]")
        else:
            self.ai_title_lbl.config(text="No Match Found", fg="#991B1B")
            self.ai_formula_lbl.config(text="Formula: None")
            self.ai_desc_lbl.config(text=msg)

    # --- LIVE DEMO TAB BUILDER ---
    def build_live_demo_tab(self):
        demo_frame = self.tabs["Live Demo"]
        self.demo_notebook = ttk.Notebook(demo_frame)
        self.demo_notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.math_demo_frame = tk.Frame(self.demo_notebook, bg="#FFFFFF")
        self.physics_demo_frame = tk.Frame(self.demo_notebook, bg="#FFFFFF")

        self.demo_notebook.add(self.math_demo_frame, text="  LA&C Calculators  ")
        self.demo_notebook.add(self.physics_demo_frame, text="  Engineering Physics Calculators  ")

        self.build_math_calculators()
        self.build_physics_calculators()

    # --- MATH CALCULATORS SECTION ---
    def build_math_calculators(self):
        container = tk.Frame(self.math_demo_frame, bg="#FFFFFF", padx=20, pady=15)
        container.pack(fill="both", expand=True)

        select_frame = tk.Frame(container, bg="#F1F5F9", padx=10, pady=10, bd=1, relief="solid")
        select_frame.pack(fill="x", pady=(0, 15))

        tk.Label(select_frame, text="Select LA&C Calculator:", font=("Helvetica", 10, "bold"), bg="#F1F5F9", fg="#0F172A").pack(side="left", padx=(0, 10))

        math_options = [
            "Matrix Addition",
            "Matrix Multiplication",
            "2x2 / 3x3 Matrix Inverse & Det",
            "Matrix Rank (Echelon Form)",
            "3D Vector Magnitude",
            "3D Vector Dot Product",
            "Jacobian Determinant (2x2)",
            "Directional Derivative"
        ]

        self.math_choice = ttk.Combobox(select_frame, values=math_options, state="readonly", width=35, font=("Helvetica", 10))
        self.math_choice.pack(side="left")
        self.math_choice.current(0)
        self.math_choice.bind("<<ComboboxSelected>>", self.render_selected_math_calc)

        self.math_work_panel = tk.Frame(container, bg="#FFFFFF")
        self.math_work_panel.pack(fill="both", expand=True)

        self.render_selected_math_calc()

    def render_selected_math_calc(self, event=None):
        for widget in self.math_work_panel.winfo_children():
            widget.destroy()

        selected = self.math_choice.get()

        if selected in ["Matrix Addition", "Matrix Multiplication"]:
            self.render_matrix_op_ui(selected)
        elif selected == "2x2 / 3x3 Matrix Inverse & Det":
            self.render_matrix_inv_det_ui()
        elif selected == "Matrix Rank (Echelon Form)":
            self.render_matrix_rank_ui()
        elif selected == "3D Vector Magnitude":
            self.render_vector_mag_ui()
        elif selected == "3D Vector Dot Product":
            self.render_vector_dot_ui()
        elif selected == "Jacobian Determinant (2x2)":
            self.render_jacobian_ui()
        elif selected == "Directional Derivative":
            self.render_directional_derivative_ui()

    def render_matrix_op_ui(self, op_name):
        card = tk.LabelFrame(self.math_work_panel, text=f" {op_name} ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        size_frame = tk.Frame(card, bg="#FFFFFF")
        size_frame.pack(anchor="w", pady=(0, 10))

        tk.Label(size_frame, text="Matrix Size:", font=("Helvetica", 10, "bold"), bg="#FFFFFF").pack(side="left", padx=(0, 10))
        self.mat_size_var = tk.StringVar(value="2x2")
        ttk.Radiobutton(size_frame, text="2x2", variable=self.mat_size_var, value="2x2", command=lambda: self.update_double_matrix_grid(op_name)).pack(side="left", padx=5)
        ttk.Radiobutton(size_frame, text="3x3", variable=self.mat_size_var, value="3x3", command=lambda: self.update_double_matrix_grid(op_name)).pack(side="left", padx=5)

        self.double_grid_container = tk.Frame(card, bg="#FFFFFF")
        self.double_grid_container.pack(anchor="w", pady=10)

        self.update_double_matrix_grid(op_name)

        btn_frame = tk.Frame(card, bg="#FFFFFF")
        btn_frame.pack(fill="x", pady=10)

        tk.Button(
            btn_frame,
            text=f"Calculate {op_name}",
            bg="#0F172A",
            fg="#FFFFFF",
            font=("Helvetica", 10, "bold"),
            padx=15,
            pady=5,
            command=lambda: self.process_matrix_op(op_name),
            cursor="hand2"
        ).pack(side="left", padx=(0, 10))

        self.res_label = tk.Label(card, text="Result: Click Calculate to view matrix output.", font=("Helvetica", 10, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.res_label.pack(fill="x", pady=10)

    def update_double_matrix_grid(self, op_name):
        for w in self.double_grid_container.winfo_children():
            w.destroy()

        n = 2 if self.mat_size_var.get() == "2x2" else 3

        # Matrix A
        fA = tk.LabelFrame(self.double_grid_container, text=" Matrix A ", font=("Helvetica", 9, "bold"), bg="#FFFFFF")
        fA.pack(side="left", padx=(0, 20))
        self.entries_A = []
        for r in range(n):
            row = []
            for c in range(n):
                e = ttk.Entry(fA, width=5)
                e.grid(row=r, column=c, padx=3, pady=3)
                e.insert(0, "1" if r == c else "0")
                row.append(e)
            self.entries_A.append(row)

        # Matrix B
        fB = tk.LabelFrame(self.double_grid_container, text=" Matrix B ", font=("Helvetica", 9, "bold"), bg="#FFFFFF")
        fB.pack(side="left")
        self.entries_B = []
        for r in range(n):
            row = []
            for c in range(n):
                e = ttk.Entry(fB, width=5)
                e.grid(row=r, column=c, padx=3, pady=3)
                e.insert(0, "2" if r == c else "1")
                row.append(e)
            self.entries_B.append(row)

    def process_matrix_op(self, op_name):
        try:
            mA = [[float(e.get().strip()) for e in row] for row in self.entries_A]
            mB = [[float(e.get().strip()) for e in row] for row in self.entries_B]

            res = MathEngine.matrix_add(mA, mB) if op_name == "Matrix Addition" else MathEngine.matrix_multiply(mA, mB)

            out_str = f"Result Matrix ({op_name}):\n"
            for row in res:
                out_str += "[  " + "  ".join([f"{val:g}" for val in row]) + "  ]\n"
            self.res_label.config(text=out_str, fg="#166534")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid numeric matrix elements.")

    def render_matrix_inv_det_ui(self):
        card = tk.LabelFrame(self.math_work_panel, text=" 2x2 & 3x3 Matrix Inverse and Determinant ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        size_frame = tk.Frame(card, bg="#FFFFFF")
        size_frame.pack(anchor="w", pady=(0, 10))

        tk.Label(size_frame, text="Matrix Size:", font=("Helvetica", 10, "bold"), bg="#FFFFFF").pack(side="left", padx=(0, 10))
        self.mat_size_var = tk.StringVar(value="3x3")
        ttk.Radiobutton(size_frame, text="2x2", variable=self.mat_size_var, value="2x2", command=self.update_matrix_grid).pack(side="left", padx=5)
        ttk.Radiobutton(size_frame, text="3x3", variable=self.mat_size_var, value="3x3", command=self.update_matrix_grid).pack(side="left", padx=5)

        self.grid_container = tk.Frame(card, bg="#FFFFFF")
        self.grid_container.pack(anchor="w", pady=10)

        self.update_matrix_grid()

        btn_frame = tk.Frame(card, bg="#FFFFFF")
        btn_frame.pack(fill="x", pady=10)

        tk.Button(
            btn_frame,
            text="Calculate Inverse & Det",
            bg="#0F172A",
            fg="#FFFFFF",
            font=("Helvetica", 10, "bold"),
            padx=15,
            pady=5,
            command=self.process_matrix_inv_det,
            cursor="hand2"
        ).pack(side="left", padx=(0, 10))

        self.res_label = tk.Label(card, text="Result: Click Calculate to view output.", font=("Helvetica", 10, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.res_label.pack(fill="x", pady=10)

    def update_matrix_grid(self):
        for w in self.grid_container.winfo_children():
            w.destroy()

        n = 2 if self.mat_size_var.get() == "2x2" else 3
        self.matrix_entries = []
        for r in range(n):
            row_entries = []
            for c in range(n):
                ent = ttk.Entry(self.grid_container, width=6)
                ent.grid(row=r, column=c, padx=4, pady=4)
                ent.insert(0, "1" if r == c else "0")
                row_entries.append(ent)
            self.matrix_entries.append(row_entries)

    def process_matrix_inv_det(self):
        try:
            mA = [[float(e.get().strip()) for e in row] for row in self.matrix_entries]
            inv, det = MathEngine.matrix_inverse(mA)
            out_str = f"Determinant det(A) = {det}\n\nInverse Matrix A^-1:\n"
            for r in inv:
                out_str += "[  " + "  ".join([f"{val:g}" for val in r]) + "  ]\n"
            self.res_label.config(text=out_str, fg="#166534")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def render_matrix_rank_ui(self):
        card = tk.LabelFrame(self.math_work_panel, text=" Matrix Rank (Echelon Form Reduction) ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        size_frame = tk.Frame(card, bg="#FFFFFF")
        size_frame.pack(anchor="w", pady=(0, 10))

        tk.Label(size_frame, text="Matrix Size:", font=("Helvetica", 10, "bold"), bg="#FFFFFF").pack(side="left", padx=(0, 10))
        self.mat_size_var = tk.StringVar(value="3x3")
        ttk.Radiobutton(size_frame, text="2x2", variable=self.mat_size_var, value="2x2", command=self.update_matrix_grid).pack(side="left", padx=5)
        ttk.Radiobutton(size_frame, text="3x3", variable=self.mat_size_var, value="3x3", command=self.update_matrix_grid).pack(side="left", padx=5)

        self.grid_container = tk.Frame(card, bg="#FFFFFF")
        self.grid_container.pack(anchor="w", pady=10)

        self.update_matrix_grid()

        btn_frame = tk.Frame(card, bg="#FFFFFF")
        btn_frame.pack(fill="x", pady=10)

        tk.Button(
            btn_frame,
            text="Calculate Rank",
            bg="#0F172A",
            fg="#FFFFFF",
            font=("Helvetica", 10, "bold"),
            padx=15,
            pady=5,
            command=self.process_matrix_rank,
            cursor="hand2"
        ).pack(side="left", padx=(0, 10))

        self.res_label = tk.Label(card, text="Result: Click Calculate to view rank.", font=("Helvetica", 10, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.res_label.pack(fill="x", pady=10)

    def process_matrix_rank(self):
        try:
            mA = [[float(e.get().strip()) for e in row] for row in self.matrix_entries]
            rank = MathEngine.matrix_rank_echelon(mA)
            self.res_label.config(text=f"Matrix Rank (Echelon Form) = {rank}", fg="#166534")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid numeric matrix elements.")

    def render_vector_mag_ui(self):
        card = tk.LabelFrame(self.math_work_panel, text=" 3D Vector Magnitude ||v|| = sqrt(ax^2 + ay^2 + az^2) ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        f = tk.Frame(card, bg="#FFFFFF")
        f.pack(anchor="w", pady=10)
        tk.Label(f, text="ax (i):", bg="#FFFFFF").grid(row=0, column=0)
        self.vx = ttk.Entry(f, width=6)
        self.vx.grid(row=0, column=1, padx=5)
        self.vx.insert(0, "3")

        tk.Label(f, text="ay (j):", bg="#FFFFFF").grid(row=0, column=2)
        self.vy = ttk.Entry(f, width=6)
        self.vy.grid(row=0, column=3, padx=5)
        self.vy.insert(0, "4")

        tk.Label(f, text="az (k):", bg="#FFFFFF").grid(row=0, column=4)
        self.vz = ttk.Entry(f, width=6)
        self.vz.grid(row=0, column=5, padx=5)
        self.vz.insert(0, "12")

        tk.Button(card, text="Calculate Magnitude", bg="#0F172A", fg="#FFFFFF", font=("Helvetica", 10, "bold"), padx=15, pady=5, command=self.process_vmag, cursor="hand2").pack(anchor="w", pady=10)

        self.res_label = tk.Label(card, text="Result: Click Calculate.", font=("Helvetica", 10, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.res_label.pack(fill="x", pady=10)

    def process_vmag(self):
        try:
            mag = MathEngine.vector_magnitude(float(self.vx.get()), float(self.vy.get()), float(self.vz.get()))
            self.res_label.config(text=f"Vector Magnitude ||v|| = {mag}", fg="#166534")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Enter valid numbers.")

    def render_vector_dot_ui(self):
        card = tk.LabelFrame(self.math_work_panel, text=" 3D Vector Dot Product (a . b) ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        f = tk.Frame(card, bg="#FFFFFF")
        f.pack(anchor="w", pady=10)
        tk.Label(f, text="Vector A (ax, ay, az):", bg="#FFFFFF").grid(row=0, column=0)
        self.vax = ttk.Entry(f, width=5)
        self.vax.grid(row=0, column=1)
        self.vax.insert(0, "1")

        self.vay = ttk.Entry(f, width=5)
        self.vay.grid(row=0, column=2, padx=3)
        self.vay.insert(0, "3")

        self.vaz = ttk.Entry(f, width=5)
        self.vaz.grid(row=0, column=3)
        self.vaz.insert(0, "-5")

        tk.Label(f, text="Vector B (bx, by, bz):", bg="#FFFFFF").grid(row=1, column=0, pady=5)
        self.vbx = ttk.Entry(f, width=5)
        self.vbx.grid(row=1, column=1)
        self.vbx.insert(0, "4")

        self.vby = ttk.Entry(f, width=5)
        self.vby.grid(row=1, column=2, padx=3)
        self.vby.insert(0, "-2")

        self.vbz = ttk.Entry(f, width=5)
        self.vbz.grid(row=1, column=3)
        self.vbz.insert(0, "-1")

        tk.Button(card, text="Calculate Dot Product", bg="#0F172A", fg="#FFFFFF", font=("Helvetica", 10, "bold"), padx=15, pady=5, command=self.process_vdot, cursor="hand2").pack(anchor="w", pady=10)

        self.res_label = tk.Label(card, text="Result: Click Calculate.", font=("Helvetica", 10, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.res_label.pack(fill="x", pady=10)

    def process_vdot(self):
        try:
            dot = MathEngine.vector_dot_product(
                float(self.vax.get()), float(self.vay.get()), float(self.vaz.get()),
                float(self.vbx.get()), float(self.vby.get()), float(self.vbz.get())
            )
            self.res_label.config(text=f"Dot Product (a . b) = {dot}", fg="#166534")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Enter valid numbers.")

    def render_jacobian_ui(self):
        card = tk.LabelFrame(self.math_work_panel, text=" Jacobian Determinant J = d(u,v)/d(x,y) ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        f_frame = tk.Frame(card, bg="#FFFFFF")
        f_frame.pack(anchor="w", pady=10)

        tk.Label(f_frame, text="du/dx:", bg="#FFFFFF").grid(row=0, column=0, sticky="w", pady=5)
        self.du_dx = ttk.Entry(f_frame, width=8)
        self.du_dx.grid(row=0, column=1, padx=10)
        self.du_dx.insert(0, "2")

        tk.Label(f_frame, text="du/dy:", bg="#FFFFFF").grid(row=0, column=2, sticky="w", pady=5)
        self.du_dy = ttk.Entry(f_frame, width=8)
        self.du_dy.grid(row=0, column=3, padx=10)
        self.du_dy.insert(0, "3")

        tk.Label(f_frame, text="dv/dx:", bg="#FFFFFF").grid(row=1, column=0, sticky="w", pady=5)
        self.dv_dx = ttk.Entry(f_frame, width=8)
        self.dv_dx.grid(row=1, column=1, padx=10)
        self.dv_dx.insert(0, "1")

        tk.Label(f_frame, text="dv/dy:", bg="#FFFFFF").grid(row=1, column=2, sticky="w", pady=5)
        self.dv_dy = ttk.Entry(f_frame, width=8)
        self.dv_dy.grid(row=1, column=3, padx=10)
        self.dv_dy.insert(0, "4")

        tk.Button(card, text="Calculate Jacobian J", bg="#0F172A", fg="#FFFFFF", font=("Helvetica", 10, "bold"), padx=15, pady=5, command=self.process_jacobian, cursor="hand2").pack(anchor="w", pady=10)

        self.res_label = tk.Label(card, text="Result: Click Calculate.", font=("Helvetica", 10, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.res_label.pack(fill="x", pady=10)

    def process_jacobian(self):
        try:
            J = MathEngine.jacobian_2x2(
                float(self.du_dx.get().strip()), float(self.du_dy.get().strip()),
                float(self.dv_dx.get().strip()), float(self.dv_dy.get().strip())
            )
            self.res_label.config(text=f"Jacobian Determinant J = {J}", fg="#166534")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Enter valid partial derivatives.")

    def render_directional_derivative_ui(self):
        card = tk.LabelFrame(self.math_work_panel, text=" Directional Derivative D_u f = grad(f) . u_hat ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        f_frame = tk.Frame(card, bg="#FFFFFF")
        f_frame.pack(anchor="w", pady=10)

        tk.Label(f_frame, text="Grad f (df/dx, df/dy, df/dz):", font=("Helvetica", 10, "bold"), bg="#FFFFFF").grid(row=0, column=0, columnspan=6, sticky="w")
        self.gx = ttk.Entry(f_frame, width=6)
        self.gx.grid(row=1, column=0)
        self.gx.insert(0, "2")

        self.gy = ttk.Entry(f_frame, width=6)
        self.gy.grid(row=1, column=1, padx=5)
        self.gy.insert(0, "-1")

        self.gz = ttk.Entry(f_frame, width=6)
        self.gz.grid(row=1, column=2)
        self.gz.insert(0, "4")

        tk.Label(f_frame, text="Direction Vector u (ux, uy, uz):", font=("Helvetica", 10, "bold"), bg="#FFFFFF").grid(row=2, column=0, columnspan=6, sticky="w", pady=(10, 0))
        self.ux = ttk.Entry(f_frame, width=6)
        self.ux.grid(row=3, column=0)
        self.ux.insert(0, "1")

        self.uy = ttk.Entry(f_frame, width=6)
        self.uy.grid(row=3, column=1, padx=5)
        self.uy.insert(0, "2")

        self.uz = ttk.Entry(f_frame, width=6)
        self.uz.grid(row=3, column=2)
        self.uz.insert(0, "2")

        tk.Button(card, text="Calculate Directional Derivative", bg="#0F172A", fg="#FFFFFF", font=("Helvetica", 10, "bold"), padx=15, pady=5, command=self.process_dd, cursor="hand2").pack(anchor="w", pady=15)

        self.res_label = tk.Label(card, text="Result: Click Calculate.", font=("Helvetica", 10, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.res_label.pack(fill="x", pady=10)

    def process_dd(self):
        try:
            dd = MathEngine.directional_derivative(
                float(self.gx.get().strip()), float(self.gy.get().strip()), float(self.gz.get().strip()),
                float(self.ux.get().strip()), float(self.uy.get().strip()), float(self.uz.get().strip())
            )
            self.res_label.config(text=f"Directional Derivative D_u f = {dd}", fg="#166534")
        except ValueError as e:
            messagebox.showwarning("Error", str(e))

    # --- PHYSICS CALCULATORS SECTION ---
    def build_physics_calculators(self):
        container = tk.Frame(self.physics_demo_frame, bg="#FFFFFF", padx=20, pady=15)
        container.pack(fill="both", expand=True)

        select_frame = tk.Frame(container, bg="#F1F5F9", padx=10, pady=10, bd=1, relief="solid")
        select_frame.pack(fill="x", pady=(0, 15))

        tk.Label(select_frame, text="Select Physics Calculator:", font=("Helvetica", 10, "bold"), bg="#F1F5F9", fg="#0F172A").pack(side="left", padx=(0, 10))

        physics_options = [
            "Force (F = m * a)",
            "Work (W = F * d)",
            "Power (P = W / t)",
            "Kinetic Energy (KE = 0.5 * m * v^2)",
            "Interplanar Distance d_hkl",
            "Bragg's Law Wavelength",
            "Newton's Rings Lens Radius R",
            "Quantum Particle in 1D Box",
            "Hall Coefficient R_H"
        ]

        self.physics_choice = ttk.Combobox(select_frame, values=physics_options, state="readonly", width=35, font=("Helvetica", 10))
        self.physics_choice.pack(side="left")
        self.physics_choice.current(0)
        self.physics_choice.bind("<<ComboboxSelected>>", self.render_selected_physics_calc)

        self.physics_work_panel = tk.Frame(container, bg="#FFFFFF")
        self.physics_work_panel.pack(fill="both", expand=True)

        self.render_selected_physics_calc()

    def render_selected_physics_calc(self, event=None):
        for widget in self.physics_work_panel.winfo_children():
            widget.destroy()

        choice = self.physics_choice.get()

        if choice == "Force (F = m * a)":
            self.render_simple_physics_ui("Force", "Mass (m, kg)", "Acceleration (a, m/s^2)", "N", PhysicsEngine.calculate_force)
        elif choice == "Work (W = F * d)":
            self.render_simple_physics_ui("Work", "Force (F, N)", "Distance (d, m)", "J", PhysicsEngine.calculate_work)
        elif choice == "Power (P = W / t)":
            self.render_simple_physics_ui("Power", "Work (W, J)", "Time (t, s)", "W", PhysicsEngine.calculate_power)
        elif choice == "Kinetic Energy (KE = 0.5 * m * v^2)":
            self.render_simple_physics_ui("Kinetic Energy", "Mass (m, kg)", "Velocity (v, m/s)", "J", PhysicsEngine.calculate_kinetic_energy)
        elif choice == "Interplanar Distance d_hkl":
            self.render_dhkl_ui()
        elif choice == "Bragg's Law Wavelength":
            self.render_bragg_ui()
        elif choice == "Newton's Rings Lens Radius R":
            self.render_newton_ui()
        elif choice == "Quantum Particle in 1D Box":
            self.render_quantum_ui()
        elif choice == "Hall Coefficient R_H":
            self.render_hall_ui()

    def render_simple_physics_ui(self, title, label1, label2, unit, func):
        card = tk.LabelFrame(self.physics_work_panel, text=f" {title} Calculator ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        f = tk.Frame(card, bg="#FFFFFF")
        f.pack(anchor="w", pady=10)
        tk.Label(f, text=f"{label1}:", bg="#FFFFFF").grid(row=0, column=0, sticky="w", pady=4)
        e1 = ttk.Entry(f, width=12)
        e1.grid(row=0, column=1, padx=10)
        e1.insert(0, "10.0")

        tk.Label(f, text=f"{label2}:", bg="#FFFFFF").grid(row=1, column=0, sticky="w", pady=4)
        e2 = ttk.Entry(f, width=12)
        e2.grid(row=1, column=1, padx=10)
        e2.insert(0, "2.0")

        res_lbl = tk.Label(card, text="Result: Click Calculate.", font=("Helvetica", 10, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)

        def do_calc():
            try:
                v1, v2 = float(e1.get().strip()), float(e2.get().strip())
                val = func(v1, v2)
                res_lbl.config(text=f"Calculated {title} = {val} {unit}", fg="#166534")
            except ValueError as ex:
                messagebox.showwarning("Error", str(ex))

        tk.Button(card, text=f"Calculate {title}", bg="#0F172A", fg="#FFFFFF", font=("Helvetica", 10, "bold"), padx=15, pady=5, command=do_calc, cursor="hand2").pack(anchor="w", pady=10)
        res_lbl.pack(fill="x", pady=10)

    def render_dhkl_ui(self):
        card = tk.LabelFrame(self.physics_work_panel, text=" Interplanar Spacing d_hkl = a / sqrt(h^2 + k^2 + l^2) ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        f = tk.Frame(card, bg="#FFFFFF")
        f.pack(anchor="w", pady=10)
        tk.Label(f, text="Lattice Constant a (Å):", bg="#FFFFFF").grid(row=0, column=0, sticky="w")
        self.a_ent = ttk.Entry(f, width=10)
        self.a_ent.grid(row=0, column=1, padx=10)
        self.a_ent.insert(0, "4.0")

        tk.Label(f, text="Miller Indices (h, k, l):", bg="#FFFFFF").grid(row=1, column=0, sticky="w", pady=10)
        self.h_ent = ttk.Entry(f, width=5)
        self.h_ent.grid(row=1, column=1, sticky="w")
        self.h_ent.insert(0, "1")

        self.k_ent = ttk.Entry(f, width=5)
        self.k_ent.grid(row=1, column=2, padx=5)
        self.k_ent.insert(0, "1")

        self.l_ent = ttk.Entry(f, width=5)
        self.l_ent.grid(row=1, column=3)
        self.l_ent.insert(0, "1")

        tk.Button(card, text="Calculate d_hkl", bg="#0F172A", fg="#FFFFFF", font=("Helvetica", 10, "bold"), padx=15, pady=5, command=self.process_dhkl, cursor="hand2").pack(anchor="w", pady=10)

        self.phy_res_label = tk.Label(card, text="Result: Click Calculate.", font=("Helvetica", 10, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.phy_res_label.pack(fill="x", pady=10)

    def process_dhkl(self):
        try:
            d = PhysicsEngine.interplanar_spacing(
                float(self.a_ent.get().strip()),
                float(self.h_ent.get().strip()),
                float(self.k_ent.get().strip()),
                float(self.l_ent.get().strip())
            )
            self.phy_res_label.config(text=f"Interplanar Spacing d_hkl = {d} Å", fg="#166534")
        except ValueError as e:
            messagebox.showwarning("Error", str(e))

    def render_bragg_ui(self):
        card = tk.LabelFrame(self.physics_work_panel, text=" Bragg's Law: 2d sin(theta) = n lambda ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        f = tk.Frame(card, bg="#FFFFFF")
        f.pack(anchor="w", pady=10)
        tk.Label(f, text="Interplanar Spacing d (Å):", bg="#FFFFFF").grid(row=0, column=0, sticky="w", pady=4)
        self.br_d = ttk.Entry(f, width=10)
        self.br_d.grid(row=0, column=1, padx=10)
        self.br_d.insert(0, "2.82")

        tk.Label(f, text="Glancing Angle theta (degrees):", bg="#FFFFFF").grid(row=1, column=0, sticky="w", pady=4)
        self.br_th = ttk.Entry(f, width=10)
        self.br_th.grid(row=1, column=1, padx=10)
        self.br_th.insert(0, "30.0")

        tk.Label(f, text="Reflection Order n:", bg="#FFFFFF").grid(row=2, column=0, sticky="w", pady=4)
        self.br_n = ttk.Entry(f, width=10)
        self.br_n.grid(row=2, column=1, padx=10)
        self.br_n.insert(0, "1")

        tk.Button(card, text="Calculate Wavelength lambda", bg="#0F172A", fg="#FFFFFF", font=("Helvetica", 10, "bold"), padx=15, pady=5, command=self.process_bragg, cursor="hand2").pack(anchor="w", pady=10)

        self.phy_res_label = tk.Label(card, text="Result: Click Calculate.", font=("Helvetica", 10, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.phy_res_label.pack(fill="x", pady=10)

    def process_bragg(self):
        try:
            lam = PhysicsEngine.bragg_law_wavelength(
                float(self.br_d.get().strip()), float(self.br_th.get().strip()), int(self.br_n.get().strip())
            )
            self.phy_res_label.config(text=f"Wavelength lambda = {lam} Å", fg="#166534")
        except ValueError as e:
            messagebox.showwarning("Error", str(e))

    def render_newton_ui(self):
        card = tk.LabelFrame(self.physics_work_panel, text=" Newton's Rings Lens Radius R = (D_{n+m}^2 - D_n^2) / (4 m lambda) ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        f = tk.Frame(card, bg="#FFFFFF")
        f.pack(anchor="w", pady=10)
        tk.Label(f, text="D_(n+m) (cm):", bg="#FFFFFF").grid(row=0, column=0, sticky="w", pady=3)
        self.nr_d2 = ttk.Entry(f, width=10)
        self.nr_d2.grid(row=0, column=1, padx=10)
        self.nr_d2.insert(0, "0.7")

        tk.Label(f, text="D_n (cm):", bg="#FFFFFF").grid(row=1, column=0, sticky="w", pady=3)
        self.nr_d1 = ttk.Entry(f, width=10)
        self.nr_d1.grid(row=1, column=1, padx=10)
        self.nr_d1.insert(0, "0.4")

        tk.Label(f, text="Rings count m:", bg="#FFFFFF").grid(row=2, column=0, sticky="w", pady=3)
        self.nr_m = ttk.Entry(f, width=10)
        self.nr_m.grid(row=2, column=1, padx=10)
        self.nr_m.insert(0, "5")

        tk.Label(f, text="Wavelength lambda (nm):", bg="#FFFFFF").grid(row=3, column=0, sticky="w", pady=3)
        self.nr_lam = ttk.Entry(f, width=10)
        self.nr_lam.grid(row=3, column=1, padx=10)
        self.nr_lam.insert(0, "589.3")

        tk.Button(card, text="Calculate Lens Radius R", bg="#0F172A", fg="#FFFFFF", font=("Helvetica", 10, "bold"), padx=15, pady=5, command=self.process_newton, cursor="hand2").pack(anchor="w", pady=10)

        self.phy_res_label = tk.Label(card, text="Result: Click Calculate.", font=("Helvetica", 10, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.phy_res_label.pack(fill="x", pady=10)

    def process_newton(self):
        try:
            R = PhysicsEngine.newtons_rings_radius_curvature(
                float(self.nr_d2.get().strip()),
                float(self.nr_d1.get().strip()),
                int(self.nr_m.get().strip()),
                float(self.nr_lam.get().strip())
            )
            self.phy_res_label.config(text=f"Lens Radius of Curvature R = {R} m ({round(R * 100, 2)} cm)", fg="#166534")
        except ValueError as e:
            messagebox.showwarning("Error", str(e))

    def render_quantum_ui(self):
        card = tk.LabelFrame(self.physics_work_panel, text=" Quantum Particle in 1D Box: E_n = (n^2 h^2)/(8 m L^2) ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        f = tk.Frame(card, bg="#FFFFFF")
        f.pack(anchor="w", pady=10)
        tk.Label(f, text="Quantum State n:", bg="#FFFFFF").grid(row=0, column=0, sticky="w", pady=4)
        self.qm_n = ttk.Entry(f, width=10)
        self.qm_n.grid(row=0, column=1, padx=10)
        self.qm_n.insert(0, "1")

        tk.Label(f, text="Box Width L (nm):", bg="#FFFFFF").grid(row=1, column=0, sticky="w", pady=4)
        self.qm_L = ttk.Entry(f, width=10)
        self.qm_L.grid(row=1, column=1, padx=10)
        self.qm_L.insert(0, "1.0")

        tk.Button(card, text="Calculate Energy Level", bg="#0F172A", fg="#FFFFFF", font=("Helvetica", 10, "bold"), padx=15, pady=5, command=self.process_quantum, cursor="hand2").pack(anchor="w", pady=10)

        self.phy_res_label = tk.Label(card, text="Result: Click Calculate.", font=("Helvetica", 10, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.phy_res_label.pack(fill="x", pady=10)

    def process_quantum(self):
        try:
            E_eV = PhysicsEngine.quantum_particle_box_energy(
                int(self.qm_n.get().strip()), float(self.qm_L.get().strip())
            )
            self.phy_res_label.config(text=f"Energy Level E_{self.qm_n.get().strip()} = {E_eV} eV", fg="#166534")
        except ValueError as e:
            messagebox.showwarning("Error", str(e))

    def render_hall_ui(self):
        card = tk.LabelFrame(self.physics_work_panel, text=" Hall Coefficient R_H = 1 / (n * e) ", font=("Helvetica", 11, "bold"), bg="#FFFFFF", fg="#0F172A", padx=15, pady=15)
        card.pack(fill="both", expand=True)

        f = tk.Frame(card, bg="#FFFFFF")
        f.pack(anchor="w", pady=10)
        tk.Label(f, text="Carrier Density n (m^-3):", bg="#FFFFFF").grid(row=0, column=0, sticky="w", pady=4)
        self.hl_n = ttk.Entry(f, width=15)
        self.hl_n.grid(row=0, column=1, padx=10)
        self.hl_n.insert(0, "1e22")

        tk.Button(card, text="Calculate Hall Coefficient", bg="#0F172A", fg="#FFFFFF", font=("Helvetica", 10, "bold"), padx=15, pady=5, command=self.process_hall, cursor="hand2").pack(anchor="w", pady=10)

        self.phy_res_label = tk.Label(card, text="Result: Click Calculate.", font=("Helvetica", 10, "bold"), fg="#0F172A", bg="#F8FAFC", relief="solid", bd=1, pady=10)
        self.phy_res_label.pack(fill="x", pady=10)

    def process_hall(self):
        try:
            RH = PhysicsEngine.hall_coefficient(float(self.hl_n.get().strip()))
            self.phy_res_label.config(text=f"Hall Coefficient R_H = {RH:.4e} m³/C", fg="#166534")
        except ValueError as e:
            messagebox.showwarning("Error", str(e))

    def build_about_tab(self):
        about_frame = self.tabs["About Project"]
        container = tk.Frame(about_frame, bg="#FFFFFF", padx=25, pady=25)
        container.pack(fill="both", expand=True)

        title = tk.Label(container, text="About 'Engineering Formula Calculator'", font=("Helvetica", 15, "bold"), fg="#0F172A", bg="#FFFFFF")
        title.pack(anchor="w", pady=(0, 10))

        desc_text = (
            "Custom-designed B.Tech Mini Project aligned strictly with JNTUK Curriculum R23.\n\n"
            "Modules Covered:\n"
            "1. Linear Algebra & Calculus (LA&C): Matrix Addition/Multiplication, Echelon Matrix Rank, 2x2/3x3 Matrix Inverses, Jacobians, Directional Derivatives.\n"
            "2. Engineering Physics: Classical Mechanics (Force, Work, KE) + R23 Physics (Miller Indices d_hkl, Bragg's Law, Newton's Rings, 1D Box Quantum Energy, Hall Coefficient)."
        )

        desc = tk.Label(container, text=desc_text, font=("Helvetica", 10), fg="#334155", bg="#FFFFFF", justify="left", wraplength=850)
        desc.pack(anchor="w", pady=(0, 20))

        tech_frame = tk.LabelFrame(container, text=" Technical Specs ", font=("Helvetica", 11, "bold"), fg="#0F172A", bg="#FFFFFF", bd=1, relief="solid", padx=15, pady=15)
        tech_frame.pack(fill="x")

        specs = [
            ("Version:", "v2.0.0 (JNTUK R23 Edition)"),
            ("Language:", "Python 3.x"),
            ("GUI Engine:", "Tkinter Desktop & Streamlit Web Interface"),
            ("Syllabus:", "JNTUK Regulation R23 Approved")
        ]

        for idx, (spec_k, spec_v) in enumerate(specs):
            k_lbl = tk.Label(tech_frame, text=spec_k, font=("Helvetica", 9, "bold"), fg="#475569", bg="#FFFFFF")
            k_lbl.grid(row=idx, column=0, sticky="w", pady=3, padx=(0, 20))
            v_lbl = tk.Label(tech_frame, text=spec_v, font=("Helvetica", 9), fg="#0F172A", bg="#FFFFFF")
            v_lbl.grid(row=idx, column=1, sticky="w", pady=3)


if __name__ == "__main__":
    main_window = tk.Tk()
    app = EngineeringCalculatorApp(main_window)
    main_window.mainloop()
