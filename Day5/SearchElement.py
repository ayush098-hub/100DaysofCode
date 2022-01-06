Question_Link: https://practice.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1/?category[]=Arrays&category[]=Arrays&problemStatus=unsolved&page=2&sortBy=submissions&query=category[]ArraysproblemStatusunsolvedpage2sortBysubmissionscategory[]Arrays#

class Solution:
    def thirdLargest(self,a, n):
        arr.sort()
        arr.reverse()
        for i in range(n):
            if i==2:
                return arr[i]
                
        return -1

#{ 
#  Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr, n))
# } Driver Code Ends
