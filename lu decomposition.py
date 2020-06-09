import pprint
import scipy
import scipy.linalg
import numpy as np
T = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
print("Enter the entries in a single line: ")
entries = list(map(int, input().split())) 
A = np.array(entries).reshape(T, C)
print("Enter the entries of vector B in a single line: ") 
entries = list(map(float, input().split()))
B = np.array(entries).reshape(T,1) 
print("B = ","\n",B)

print("_______LU Decomposition")
P, L, U = scipy.linalg.lu(A)
print("A:")
pprint.pprint(A)

#print("P:")
#pprint.pprint(P)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)
#x
L_inv=scipy.linalg.inv(L)
U_inv=scipy.linalg.inv(U)
D=L_inv*B
X=D*U_inv
print("D=","\n",D)
print("X=","\n",X)

