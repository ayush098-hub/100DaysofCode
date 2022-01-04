Question Link: https://practice.geeksforgeeks.org/problems/minimum-number-to-form-the-sum-even0326/1/?category[]=Arrays&category[]=Arrays&problemStatus=unsolved&page=1&query=category[]ArraysproblemStatusunsolvedpage1category[]Arrays#
    

class Solution:
    def minNum(self, arr, n):
        sum=0
        min=0
        
        for i in range(n):
            sum=sum+arr[i]
        
        if sum%2==0:
            min=2
        else:
            min=1
            
        return min
        
        
        

#{ 
#  Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a=list(map(int,input().split()))
        ob = Solution()
        ans=ob.minNum(a,n)
        print(ans)
# } Driver Code Ends
