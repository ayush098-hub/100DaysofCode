https://practice.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1/?category[]=Arrays&category[]=Arrays&problemStatus=unsolved&page=2&query=category[]ArraysproblemStatusunsolvedpage2category[]Arrays
  
  
  #User function Template for python3

class Solution:
    def segregate0and1(self, arr, n):
      
      #mylogic
        # result1=[]
        # result2=[]
        # for i in range(n):
        #  if arr[i]==0:
        #     result1.append(arr[i])
        #  if arr[i]==1:
        #     result2.append(arr[i])
        
        # oresult=result1+result2
                
        # return oresult
        
        
        count=0

        for i in range(n):
         if arr[i]==0:
            count=count+1
    
        for i in range(count):
         arr[i]=0

        for i in range(count,n):
         arr[i]=1
     
        return arr
                
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregate0and1(arr, n)
        print(*arr)
        tc -= 1

# } Driver Code Ends
