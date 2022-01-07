Question_Link: https://practice.geeksforgeeks.org/problems/find-the-highest-number2259/1/?problemStatus=unsolved&difficulty[]=0&page=1&category[]=Binary%20Search&query=problemStatusunsolveddifficulty[]0page1category[]Binary%20Search#
    
class Solution:
	def findPeakElement(self, arr):
		# Code here
		if arr[0]>=arr[1]:
		    return arr[0]
		    
		if arr[n-1]>=arr[n-2]:
		    return arr[n-1]
		
		
		for i in range(0,len(a)-1):
		    if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
		        return arr[i]
		
		    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		a = list(map(int,input().split()))
		ob = Solution();
		ans = ob.findPeakElement(a)
		print(ans)




# } Driver Code Ends
