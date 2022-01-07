QL: https://practice.geeksforgeeks.org/problems/square-root/1/?category[]=Binary%20Search&category[]=Binary%20Search&problemStatus=unsolved&difficulty[]=1&page=1&sortBy=submissions&query=category[]Binary%20SearchproblemStatusunsolveddifficulty[]1page1sortBysubmissionscategory[]Binary%20Search

#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, x): 
    #Your code here
     s=0
     e=x
     mid=int((s+e)/2)
     ans=-1
    
     while s<=e:
        square=mid*mid
        
        if square==x:
            return mid
            
        if square < x:
            ans=mid
            s=mid+1
        else:
            e=mid-1
        mid=int((s+e)/2)
     return ans
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
