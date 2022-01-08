Question_LInk: https://practice.geeksforgeeks.org/problems/red-or-green5711/1/?category[]=Strings&category[]=Strings&difficulty[]=-1&page=1&query=category[]Stringsdifficulty[]-1page1category[]Strings#
    
#User function Template for python3

class Solution:
    def RedOrGreen(self,N,S):
        
        countr=0
        countg=0
        for i in range(N):
         if S[i]=='R':
            countr+=1
         else:
            countg+=1

        if countg<countr:
         return countg
        else:
         return countr
            #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        S=input()
        
        ob=Solution()
        print(ob.RedOrGreen(N,S))
