row=int(input("Enter Number Of Rows : "))
col=int(input("Enter Number Of Columns : "))

# mat=[[0,0,0],[0,0,0],[0,0,0]]
mat=[[0 for j in range(col)]for i in range(row)]

print("Enter Elements of Matrix1 one by one: ")
mat1=[[int(input()) for j in range(col)]for i in range(row)]
print("Enter Elements of Matrix2 one by one: ")
mat2=[[int(input()) for j in range(col)]for i in range(row)]

                        #Sum  

mat=[[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
print("Sum of Matrix is : \n") 

for sum in mat:
    print(sum)
print()
                    # Substraction

print("Substaction of matrix is : \n")
mat=[[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

for sub in mat:
    print((sub))