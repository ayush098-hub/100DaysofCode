QuestionLink: https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1/?category[]=Arrays&category[]=Arrays&problemStatus=unsolved&page=1&query=category[]ArraysproblemStatusunsolvedpage1category[]Arrays

def findmaxmin(arr):
    
    max=arr[0]
    min=arr[0]
    for x in range(len(arr)):
        if arr[x]>max:
            max=arr[x]
        elif arr[x]<min:
            min=arr[x]
    
    return max,min

arr=[12,13,45,6,7,8,9,90]

print("Max and min element in array is: "+str(findmaxmin(arr)))
