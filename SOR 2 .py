import numpy as np

def sor_solver(A, b, omega, initial_guess, convergence_criteria):
    """
    This is an implementation of the pseudo-code provided in the Wikipedia article.
    Arguments:
        A: nxn numpy matrix.
        b: n dimensional numpy vector.
        omega: relaxation factor.
        initial_guess: An initial solution guess for the solver to start with.
        convergence_criteria: The maximum discrepancy acceptable to regard the current solution as fitting.
    Returns:
        phi: solution vector of dimension n.
    """
    phi = initial_guess[:]
    residual = np.linalg.norm(np.matmul(A, phi) - b) #Initial residual
    while residual > convergence_criteria:
        for i in range(A.shape[0]):
            sigma = 0
            for j in range(A.shape[1]):
                if j != i:
                    sigma += A[i][j] * phi[j]
            phi[i] = (1 - omega) * phi[i] + (omega / A[i][i]) * (b[i] - sigma)
        residual = np.linalg.norm(np.matmul(A, phi) - b)
        print('Residual: {0:10.6g}'.format(residual))
    return phi


# An example case that mirrors the one in the Wikipedia article
residual_convergence = 1e-8
omega = 0.5 #Relaxation factor

A = np.ones((4, 4))
A[0][0] = 4
A[0][1] = -1
A[0][2] = -6
A[0][3] = 0

A[1][0] = -5
A[1][1] = -4
A[1][2] = 10
A[1][3] = 8

A[2][0] = 0
A[2][1] = 9
A[2][2] = 4
A[2][3] = -2

A[3][0] = 1
A[3][1] = 0
A[3][2] = -7
A[3][3] = 5

b = np.ones(4)
b[0] = 2
b[1] = 21
b[2] = -12
b[3] = -6

initial_guess = np.zeros(4)
print("A = ",A)
print("b = ",b)
phi = sor_solver(A, b, omega, initial_guess, residual_convergence)
print(phi)
