Question_link: https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1
 

#User function Template for python3

class Solution:
    def median(self, M, r, c):
    	R=[]
        for i in range(r):
          for j in range(c):
           R.append(M[i][j])
        
        R.sort()
           
        mid=int(0+len(R)/2)
        
        return R[mid]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(r):
            for j in range (c):
                matrix[i][j]=line1[k]
                k+=1
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends
