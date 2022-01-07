Question_Link: https://practice.geeksforgeeks.org/problems/who-will-win-1587115621/1/?category[]=Binary%20Search&category[]=Binary%20Search&problemStatus=unsolved&difficulty[]=-1&page=1&query=category[]Binary%20SearchproblemStatusunsolveddifficulty[]-1page1category[]Binary%20Search#

#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        
        s=0
        e=N-1
        mid=int(s+(e-s)/2)
        
        while s<=e:
            if arr[mid]==K:
                return 1
            if K>arr[mid]:
                s=mid+1
            else:
                e=mid-1
            mid=int(s+(e-s)/2)
        return -1
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
	t = int(input())
	for _ in range(t):
		NK = input().strip().split()
		N = int(NK[0])
		K = int(NK[1])
		A = [ int(x) for x in input().strip().split() ]
		ob=Solution()
		print(ob.searchInSorted(A,N,K))

# } Driver Code Ends
