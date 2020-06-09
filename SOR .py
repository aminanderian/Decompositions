import numpy as np
T = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
print("Enter the entries in a single line: ")
entries=list(map(int, input().split())) 
A1 = np.array(entries).reshape(T, C)
print("A = ","\n",A1)
print("Enter the entries of vector B in a single line: ") 
entries = list(map(int, input().split()))
b1 = np.array(entries).reshape(T,1) 
print("B = ","\n",b1)


def sor_solver(A, b, omega, initial_guess, convergence_criteria):
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
residual_convergence = 1e-8
omega = 0.5


A = np.ones((T, C))
b = np.ones((b1.shape[0],b1.shape[1]))
for i in range(T):
    for j in range(C):
        A[i][j]=float(A1[i][j])
for i in range(b1.shape[0]):
    for j in range(b1.shape[1]):
        b[i][j]=float(b1[i][j])
print(A)
print(b)



initial_guess = np.zeros(b.shape[0])
phi = sor_solver(A, b, omega, initial_guess, residual_convergence)
print("X =","\n",phi,"\n")
