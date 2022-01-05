def rotate(arr,D):
    result=[]

    for i in range(D,len(arr)):
        result.append(arr[i])

    for i in range(0,D):
        result.append(arr[i])

    arr=result.copy()
    


    return arr

arr=[]

for i in range(5):
    lst=int(input())
    arr.append(lst)

D=2

print(rotate(arr,D))


