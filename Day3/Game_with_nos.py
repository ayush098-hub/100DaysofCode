Question_link: https://practice.geeksforgeeks.org/problems/game-with-nos3123/1/?category[]=Arrays&category[]=Arrays&problemStatus=unsolved&page=1&query=category[]ArraysproblemStatusunsolvedpage1category[]Arrays#

#User function Template for python3

def game_with_number (arr,  n) : 
    
    result=[]
    last=arr[n-1]
    
    for i in range(n):
       
        if i==n-1:
            result.append(last)
        else:
            
            xored=arr[i] ^ arr[i+1]
            result.append(xored)
    
    return result
        
    
    #Complete the function

#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = game_with_number(arr, n);
    print(*res)




# } Driver Code Ends
