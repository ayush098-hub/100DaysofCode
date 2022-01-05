Question_Link: https://practice.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1/?category[]=Arrays&category[]=Arrays&company[]=Amazon&company[]=Amazon&problemStatus=unsolved&difficulty[]=0&page=1&query=category[]Arrayscompany[]AmazonproblemStatusunsolveddifficulty[]0page1company[]Amazoncategory[]Arrays#
    
#User function Template for python3
class Solution:

	def findMaximum(self,arr, n):
	    
        maxnum=0
        for i in range(len(arr)):

           if arr[i]>maxnum:
             maxnum=arr[i]
        return maxnum
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1
