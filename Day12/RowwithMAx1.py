Question_Link: https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1/?category[]=Matrix&category[]=Matrix&company[]=Amazon&company[]=Amazon&problemStatus=solved&difficulty[]=1&page=1&query=category[]Matrixcompany[]AmazonproblemStatussolveddifficulty[]1page1company[]Amazoncategory[]Matrix
    
    
#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
	    ans=-1
	    temp=0
	    for i in range(n):
	        count=0
	        for j in range(m):
	            if arr[i][j]==1:
	               count+=1
	            
	        if count>temp:
	            temp=count
	            ans=i
	    return ans
	            
	       
	            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends
