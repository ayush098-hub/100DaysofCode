Question_Link: https://practice.geeksforgeeks.org/problems/print-first-letter-of-every-word-in-the-string3632/1/?category[]=Strings&category[]=Strings&company[]=Amazon&company[]=Amazon&page=1&query=category[]Stringscompany[]Amazonpage1company[]Amazoncategory[]Strings#

#User function Template for python3
class Solution:
	def firstAlphabet(self, S):
     S=S.split()
     ans=[]
     for i in range(len(S)):
      ans.append(S[i][0])
     words="".join(ans)
 
     return words
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.firstAlphabet(S)
		
		print(answer)


# } Driver Code Ends
