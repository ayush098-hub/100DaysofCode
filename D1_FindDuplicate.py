#Question_Link: https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1/?category[]=Arrays&category[]=Arrays&problemType=functional&difficulty[]=0&page=1&sortBy=submissions&query=category[]ArraysproblemTypefunctionaldifficulty[]0page1sortBysubmissionscategory[]Arrays#

def findDuplicate(arr, n):
    arr.sort()

    result=[]

    for i in range(n-1):
        if arr[i]==arr[i+1]:
            result.append(arr[i])

    if len(result)==0:
        return -1
    else:
        return result


arr=[3,1,2,2,4,4,5] 

print(findDuplicate(arr,7))
