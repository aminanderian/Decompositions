import numpy as np
import scipy.linalg as la

T = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
print("Enter the entries in a single line: ") 
entries = list(map(int, input().split())) 
A = np.array(entries).reshape(T, C) 
print("A = ","\n",A)
U, s, VT = la.svd(A)
print("__ Singular-Value Decomposition (SVD)")
print("U = ")
print(U,"\n")
print("Sigma = ")
print(s,"\n")
print("V_Transpose = ")
print(VT,"\n")
I1=np.identity(min(T,C))*s.T
s_inv=la.inv(I1)
s_inv+=np.zeros((2,2))
print("s_inv = ","\n",s_inv)
B = np.ones([T,1])
X=VT.T*s_inv*U.T*B
print("X =","\n",X)
