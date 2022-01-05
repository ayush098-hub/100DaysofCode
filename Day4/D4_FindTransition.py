Question Link: https://practice.geeksforgeeks.org/problems/find-transition-point-1587115620/1/?category[]=Arrays&category[]=Arrays&company[]=Amazon&company[]=Amazon&problemStatus=unsolved&difficulty[]=0&page=1&query=category[]Arrayscompany[]AmazonproblemStatusunsolveddifficulty[]0page1company[]Amazoncategory[]Arrays#
    
def transitionPoint(arr, n):
    
    
    # count=0
    # i=0

    # while i<n:
        
    #     if 1 not in arr:
    #         return -1
    #     elif arr[i]==0:
    #         count=count+1
    #     i=i+1
    
    # return count
    
    #optimised code
    if 1 not in arr:
        return -1
    else:
        return arr.count(0)

#{ 
#  Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

# } Driver Code Ends
