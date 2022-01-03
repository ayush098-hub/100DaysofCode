QuestionLink: https://practice.geeksforgeeks.org/problems/value-equal-to-index-value1330/1/?category[]=Arrays&category[]=Arrays&problemStatus=unsolved&page=2&query=category[]ArraysproblemStatusunsolvedpage2category[]Arrays#
def valueatindex(arr):
    ans=[]
    for i in range(1,len(arr)):
        if arr[i]==i+1:
            ans.append(arr[i])
    return ans

arr=[15, 2, 45, 12, 7]
print(valueatindex(arr))
