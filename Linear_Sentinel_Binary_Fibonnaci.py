def LinearSearch(a,n,key):
    for i in range(0,n):
        if(a[i] == key): 
            return i;
    return -1;

    
def SentinelSearch(a,n,key):
    i=0 
    l=a[n-1]
    a[n-1]=key
    while(a[i] != key):
        i+=1
    a[n-1]=l
    if((i < n-1) or a[n-1] == key):return i
    else: return -1


def BinarySearch(a,n,key):
    s=0
    e=n
    while(s <= e):
        mid = int((s+e)/2)
        if(a[mid] == key): return mid
        elif (a[mid] > key): e=mid-1
        else: s = mid+1
    return -1


def fiboSearch(a,n,key):
    f1=1
    f2=0
    f=f1+f2
    while( f < n):
        f2=f1
        f1=f
        f=f1+f2
    s= -1
    while(f > 1):
        m = min((s+f2), (n-1))
        if(a[m] < key):
            f=f1
            f1=f2
            f2=f-f1
            s=m
        elif(a[m] > key):
            f=f2
            f1=f1-f2
            f2=f1=f2
        else: return m
    if(f1 and a[s+1] == key): return s+1
    return -1

    
#main
n=int(input("Enter Number of student : "))
a=[]
print(("Enter Roll No of Student (Press ENTER after each input) : "))
for i in range(0,n):
    e=int(input())
    a.append(e)
key=int(input("Enter RollNo(Key) To Find : "))
print("Linear Search : ",LinearSearch(a, n, key))
print("Sentinel Search : ",SentinelSearch(a, n, key))
print("Binary Search : ",BinarySearch(a, n, key))
print("Fibonacci Search : ",fiboSearch(a, n, key))



