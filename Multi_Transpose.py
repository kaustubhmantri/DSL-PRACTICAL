row,col=3,3
print("Enter First Matix One by One")
mat1=[[int(input()) for i in range(row)]for j in range(col)]
print("Enter Second Matrix One by One : ")
mat2=[[int(input()) for i in range(row)]for j in range(col)]
mat=[[0,0,0],[0,0,0], [0,0,0]]    
matT=[[0,0,0],[0,0,0],[0,0,0]]   

print("Multiplication of matrix is : ")    

for i in range(len(mat1)):
    for j in range(len(mat2[0])):
        for k in range(len(mat2)):
            mat[i][j] += mat1[i][k] * mat2[k][j]


for m in mat:
    print(m)
print()
                            # Transpose

for i in range(len(mat)):
    for j in range(len(mat[0])):
        matT[j][i] = mat[i][j]
print("Transpose Of Matrix is : ")
for t in matT:
    print(t)

