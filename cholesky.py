import math 
MAX = 100; 
  
def Cholesky_Decomposition(matrix, n): 
  
    lower = [[0 for x in range(n + 1)]  
                for y in range(n + 1)]; 
  
    for i in range(n):  
        for j in range(i + 1):  
            sum1 = 0; 
  
            if (j == i):  
                for k in range(j): 
                    sum1 += pow(lower[j][k], 2); 
                lower[j][j] = int(math.sqrt(matrix[j][j] - sum1)); 
            else: 
                  
                for k in range(j): 
                    sum1 += (lower[i][k] *lower[j][k]); 
                if(lower[j][j] > 0): 
                    lower[i][j] = int((matrix[i][j] - sum1) / 
                                               lower[j][j]); 
  
    print("Lower Triangular\t\tTranspose"); 
    for i in range(n):  
          
        # Lower Triangular 
        for j in range(n): 
            print(lower[i][j], end = "\t"); 
        print("", end = "\t"); 
          
        for j in range(n): 
            print(lower[j][i], end = "\t"); 
        print(""); 
  
# Driver Code 
n = 3; 
matrix = [[3, 6, -9], 
          [2, 5, -3], 
          [-4, 1, 10]]; 
Cholesky_Decomposition(matrix, n); 
  
# This code is contributed by mits 
