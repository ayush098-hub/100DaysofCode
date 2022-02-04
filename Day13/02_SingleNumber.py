Question Link https://practice.geeksforgeeks.org/problems/single-number1014/1/
  
  
#User function Template for python3

class Solution:
    
    def getSingle(self,arr, n):
        # code here
        
        xor=0
        
        for i in range(n):
            xor=xor^arr[i]
        return xor


#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getSingle(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
