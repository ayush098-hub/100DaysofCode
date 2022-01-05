Question_Link: https://practice.geeksforgeeks.org/problems/index-of-an-extra-element/1/?category[]=Arrays&category[]=Arrays&company[]=Amazon&company[]=Amazon&problemStatus=unsolved&difficulty[]=0&page=1&query=category[]Arrayscompany[]AmazonproblemStatusunsolveddifficulty[]0page1company[]Amazoncategory[]Arrays#
    

class Solution:
    def findExtra(self,a,b,n):
        #add code here
        
        m=list(set(a)-set(b))
        m=int(m[0])
        
        for i in range(n):
            if a[i]==m:
                return i

#{ 
#  Driver Code Starts
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(Solution().findExtra(a,b,n))
# } Driver Code Ends
