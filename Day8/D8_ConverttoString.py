Question_Link https://practice.geeksforgeeks.org/problems/implement-atoi/1/?category[]=Strings&category[]=Strings&company[]=Amazon&company[]=Amazon&problemStatus=unsolved&page=1&sortBy=submissions&query=category[]Stringscompany[]AmazonproblemStatusunsolvedpage1sortBysubmissionscompany[]Amazoncategory[]Strings#
 

#User function template for Python
import re
class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,S):
     result = re.match("[-+]?\d+$", S)
     if result is not None:
         return S
     else:
         return -1
              
#{ 
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends
