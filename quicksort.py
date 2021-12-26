def partition(arr, l, h):
    i = (l-1)       
    pivot = arr[h]     
  
    for j in range(l, h):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return (i+1)
  
def quickSort(arr, l, h):
    if len(arr) == 1:
        return arr
    if l < h:
        p = partition(arr, l, h)
        quickSort(arr, l, p-1)
        quickSort(arr, p+1, h)

#main
n = int(input("Enter Number of Student : "))
print("Enter Percentages (Hit ENTER after Each input) :")
arr = [float(input()) for i in range(n)]

quickSort(arr, 0, n-1)

print("\nPercentage List :")
for i in arr:
    print(i,end=" ")

print("\n\nTop Five Scores are : ")
arr.reverse()
for i in range(5):
    print(arr[i],end=" ")