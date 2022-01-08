Question_Link: https://practice.geeksforgeeks.org/problems/palindrome-string0817/1#
    
#User function Template for python3
class Solution:
	def isPalindrome(self, S):
		# code here
		i=0
		e=len(S)-1
		
		while i<=e:
		    if S[i]!=S[e]:
		        return 0
		    else:
		        i+=1
		        e-=1
		return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends
