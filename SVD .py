import numpy as np
import scipy.linalg as la

T = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
print("Enter the entries of matrix A in a single line: ") 
entries = list(map(float, input().split()))
A = np.array(entries).reshape(T, C) 
print("A = ","\n",A)
print("Enter the entries of vector B in a single line: ") 
entries = list(map(float, input().split()))
B = np.array(entries).reshape(T,1) 
print("B = ","\n",B)
U, s, VT = la.svd(A)
print("__ Singular-Value Decomposition (SVD)")
print("U = ")
print(U,"\n")
print("Sigma = ")
print(s,"\n")
print("V_Transpose = ")
print(VT,"\n")
sss=np.zeros((T,C))
splus=np.zeros((C,T))
for i in range(0,min(T,C)):
    sss[i,i] = s[i]
    splus[i,i]=1/s[i]
Aplus=np.dot(np.dot(VT.T,splus),U.T)
X=np.dot(Aplus,B)
print("S = ")
print(sss,"\n")
print("S_Plus = ")
print(splus,"\n")
print("X = ")
print(X,"\n")
