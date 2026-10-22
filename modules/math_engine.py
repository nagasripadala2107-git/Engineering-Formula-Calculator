import math
import sympy as sp

class MathEngine:
    """
    Comprehensive Mathematical Engine supporting standard operations,
    JNTUK R23 LA&C methods, and SymPy-powered symbolic calculus.
    """

    # --- STANDARD MATRIX & VECTOR OPERATIONS ---

    @staticmethod
    def matrix_add(m1, m2):
        """Adds two matrices of identical dimensions (2x2 or 3x3) and provides steps."""
        rows = len(m1)
        cols = len(m1[0])
        result = [[round(m1[r][c] + m2[r][c], 4) for c in range(cols)] for r in range(rows)]
        steps = [
            f"Add corresponding elements: C[i, j] = A[i, j] + B[i, j]",
            f"Resulting {rows}x{cols} matrix computed."
        ]
        return result, steps

    @staticmethod
    def matrix_subtract(m1, m2):
        """Subtracts m2 from m1 (2x2 or 3x3)."""
        rows = len(m1)
        cols = len(m1[0])
        return [[round(m1[r][c] - m2[r][c], 4) for c in range(cols)] for r in range(rows)]

    @staticmethod
    def matrix_multiply(m1, m2):
        """Multiplies two square matrices with detailed dot-product calculation steps."""
        rows = len(m1)
        cols = len(m2[0])
        inner = len(m2)
        result = [[0.0 for _ in range(cols)] for _ in range(rows)]
        steps = []
        for r in range(rows):
            for c in range(cols):
                expr_parts = [f"({m1[r][k]} × {m2[k][c]})" for k in range(inner)]
                val = sum(m1[r][k] * m2[k][c] for k in range(inner))
                result[r][c] = round(val, 4)
                steps.append(f"C[{r+1},{c+1}] = {' + '.join(expr_parts)} = {round(val, 4)}")
        return result, steps

    @staticmethod
    def vector_magnitude(ax, ay, az):
        """3D Vector Magnitude ||v|| with formula steps."""
        val = math.sqrt(ax**2 + ay**2 + az**2)
        step = f"||v|| = √(({ax})² + ({ay})² + ({az})²) = √({ax**2 + ay**2 + az**2}) = {val:.4f}"
        return round(val, 4), step

    @staticmethod
    def vector_dot_product(ax, ay, az, bx, by, bz):
        """3D Vector Dot Product (a · b) with step-by-step arithmetic."""
        val = (ax * bx) + (ay * by) + (az * bz)
        step = f"a · b = ({ax} × {bx}) + ({ay} × {by}) + ({az} × {bz}) = {ax*bx} + {ay*by} + {az*bz} = {val:.4f}"
        return round(val, 4), step

    @staticmethod
    def vector_cross_product(ax, ay, az, bx, by, bz):
        """3D Vector Cross Product (a × b)."""
        cx = ay * bz - az * by
        cy = az * bx - ax * bz
        cz = ax * by - ay * bx
        steps = [
            f"cx = ({ay} × {bz}) - ({az} × {by}) = {cx:.4f}",
            f"cy = ({az} × {bx}) - ({ax} × {bz}) = {cy:.4f}",
            f"cz = ({ax} × {by}) - ({ay} × {bx}) = {cz:.4f}"
        ]
        return [round(cx, 4), round(cy, 4), round(cz, 4)], steps

    # --- JNTUK R23 ADVANCED LA&C METHODS ---

    @staticmethod
    def matrix_rank_echelon(matrix):
        """Rank of matrix using upper-triangular echelon reduction with row-operation log."""
        m = [[float(val) for val in row] for row in matrix]
        rows = len(m)
        cols = len(m[0])
        steps = ["Initial Matrix:"]
        for r in m:
            steps.append(f"  {r}")

        rank = cols
        for row in range(rank):
            if abs(m[row][row]) > 1e-9:
                for col in range(rows):
                    if col != row:
                        mult = m[col][row] / m[row][row]
                        if abs(mult) > 1e-9:
                            for i in range(rank):
                                m[col][i] -= mult * m[row][i]
                            steps.append(f"Row operation: R{col+1} ← R{col+1} - ({mult:.2f}) × R{row+1}")
            else:
                reduce_flag = True
                for i in range(row + 1, rows):
                    if abs(m[i][row]) > 1e-9:
                        m[row], m[i] = m[i], m[row]
                        steps.append(f"Row Swap: Swap R{row+1} with R{i+1}")
                        reduce_flag = False
                        break
                if reduce_flag:
                    rank -= 1
                    for i in range(rows):
                        m[i][row] = m[i][rank]
                row -= 1

        steps.append(f"Number of non-zero rows in echelon form = {rank}")
        return rank, steps

    @staticmethod
    def matrix_determinant(m):
        n = len(m)
        if n == 2:
            val = (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
            step = f"det = ({m[0][0]} × {m[1][1]}) - ({m[0][1]} × {m[1][0]}) = {val:.4f}"
            return round(val, 4), step
        elif n == 3:
            term1 = m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            term2 = m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            term3 = m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
            det = term1 - term2 + term3
            step = f"det = {m[0][0]}({m[1][1]}·{m[2][2]} - {m[1][2]}·{m[2][1]}) - {m[0][1]}({m[1][0]}·{m[2][2]} - {m[1][2]}·{m[2][0]}) + {m[0][2]}({m[1][0]}·{m[2][1]} - {m[1][1]}·{m[2][0]}) = {det:.4f}"
            return round(det, 4), step

    @staticmethod
    def matrix_inverse(m):
        det, det_step = MathEngine.matrix_determinant(m)
        if abs(det) < 1e-9:
            raise ValueError("Inverse does not exist! Determinant is 0 (Singular Matrix).")
        n = len(m)
        steps = [
            f"Step 1: Compute Determinant: {det_step}",
            f"Step 2: Construct Adjugate Matrix adj(A)",
            f"Step 3: Multiply Adjugate Matrix by 1/det(A)"
        ]
        if n == 2:
            adj = [
                [m[1][1], -m[0][1]],
                [-m[1][0], m[0][0]]
            ]
            inv = [
                [round(adj[0][0] / det, 4), round(adj[0][1] / det, 4)],
                [round(adj[1][0] / det, 4), round(adj[1][1] / det, 4)]
            ]
            return inv, det, steps
        elif n == 3:
            adj = [
                [m[1][1]*m[2][2] - m[1][2]*m[2][1], -(m[0][1]*m[2][2] - m[0][2]*m[2][1]), m[0][1]*m[1][2] - m[0][2]*m[1][1]],
                [-(m[1][0]*m[2][2] - m[1][2]*m[2][0]), m[0][0]*m[2][2] - m[0][2]*m[2][0], -(m[0][0]*m[1][2] - m[0][2]*m[1][0])],
                [m[1][0]*m[2][1] - m[1][1]*m[2][0], -(m[0][0]*m[2][1] - m[0][1]*m[2][0]), m[0][0]*m[1][1] - m[0][1]*m[1][0]]
            ]
            inv = [[round(adj[r][c] / det, 4) for c in range(3)] for r in range(3)]
            return inv, det, steps

    # --- SYMPY SYMBOLIC CALCULUS & EIGENVALUES ---

    @staticmethod
    def eigenvalues_and_vectors(matrix_list):
        """Computes exact eigenvalues and eigenvectors using SymPy."""
        M = sp.Matrix(matrix_list)
        char_poly = M.charpoly()
        poly_str = sp.latex(char_poly.as_expr())
        eigenvals = M.eigenvals()
        eigenvects = M.eigenvects()
        
        val_summary = []
        for val, mult in eigenvals.items():
            val_summary.append(f"λ = {sp.latex(val)} (Algebraic Multiplicity: {mult})")
            
        vect_summary = []
        for val, mult, vects in eigenvects:
            for v in vects:
                v_latex = sp.latex(v)
                vect_summary.append(f"For λ = {sp.latex(val)}: eigenvector v = {v_latex}")
                
        return poly_str, val_summary, vect_summary

    @staticmethod
    def symbolic_gradient_and_directional(func_str, point_dict, dir_vector):
        """Calculates Gradient and Directional Derivative of scalar function f(x,y,z)."""
        x, y, z = sp.symbols('x y z')
        f = sp.sympify(func_str)
        
        grad_f = [sp.diff(f, var) for var in (x, y, z)]
        grad_latex = f"\\nabla f = \\left[ {sp.latex(grad_f[0])},\\, {sp.latex(grad_f[1])},\\, {sp.latex(grad_f[2])} \\right]"
        
        # Evaluate gradient at point
        grad_at_pt = [float(comp.subs(point_dict).evalf()) for comp in grad_f]
        
        # Unit direction vector
        vx, vy, vz = dir_vector
        mag_v = math.sqrt(vx**2 + vy**2 + vz**2)
        if mag_v == 0:
            raise ValueError("Direction vector cannot be zero vector.")
        u_dir = [vx / mag_v, vy / mag_v, vz / mag_v]
        
        # Directional derivative = grad · u
        d_u_f = sum(g * u for g, u in zip(grad_at_pt, u_dir))
        
        steps = [
            f"1. Computed Gradient: ∇f = [{sp.diff(f, x)}, {sp.diff(f, y)}, {sp.diff(f, z)}]",
            f"2. Evaluated ∇f at point {point_dict}: [{grad_at_pt[0]:.4f}, {grad_at_pt[1]:.4f}, {grad_at_pt[2]:.4f}]",
            f"3. Normalized direction vector ||v|| = {mag_v:.4f}  ==>  û = [{u_dir[0]:.4f}, {u_dir[1]:.4f}, {u_dir[2]:.4f}]",
            f"4. Directional Derivative Duf = ∇f · û = {d_u_f:.4f}"
        ]
        return grad_latex, round(d_u_f, 4), steps

    @staticmethod
    def solve_linear_system(a_matrix, b_vector):
        """Solves A X = B using SymPy exact matrix solver."""
        A = sp.Matrix(a_matrix)
        b = sp.Matrix(b_vector)
        try:
            sol = A.LUsolve(b)
            sol_list = [round(float(val.evalf()), 4) for val in sol]
            steps = [
                f"Coefficient Matrix determinant det(A) = {float(A.det()):.4f}",
                "Solved system using LU Decomposition [A | B]",
                f"Solution vector X: {sol_list}"
            ]
            return sol_list, steps
        except Exception as e:
            raise ValueError(f"System cannot be solved: {str(e)}")

    @staticmethod
    def jacobian_2x2(du_dx, du_dy, dv_dx, dv_dy):
        return round((du_dx * dv_dy) - (du_dy * dv_dx), 4)

    @staticmethod
    def directional_derivative(df_dx, df_dy, df_dz, ux, uy, uz):
        u_mag = math.sqrt(ux**2 + uy**2 + uz**2)
        if u_mag == 0:
            raise ValueError("Direction vector cannot be zero vector.")
        return round((df_dx * (ux/u_mag)) + (df_dy * (uy/u_mag)) + (df_dz * (uz/u_mag)), 4)
