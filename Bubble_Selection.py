def Selection_Sort(marks):
    for i in range(len(marks)):
        m = i
        for j in range(i + 1, len(marks)):
            if marks[m] > marks[j]:
                m = j
        marks[i], marks[m] = marks[m], marks[i]
    print("Selection Sort : ")
    for i in range(len(marks)):
        print(marks[i],end=" ")
    print()


def Bubble_Sort(marks):
    n = len(marks)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
    print("Bubble Sort :")
    for i in range(len(marks)):
        print(marks[i],end=" ")
    print()


def top_5_marks(marks):
    print()
    print("Top 5 Marks are : ")
    M=marks[::-1]
    for i in range(5):
        print(M[i])
    print()

    
# Main
marks=[]
n = int(input("Enter number of students : "))
print("Enter marks of ",n," students (Press ENTER after each marks): ")
for i in range(0, n):
    e = int(input())
    marks.append(e)  
print("The marks of",n,"students are : ")
print(marks)
print()

Selection_Sort(marks)
top_5_marks(marks)
     
Bubble_Sort(marks)
top_5_marks(marks)
     