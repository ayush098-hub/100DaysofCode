Question_Link: https://practice.geeksforgeeks.org/problems/display-longest-name0853/1/?category[]=Arrays&category[]=Arrays&problemStatus=unsolved&page=1&query=category[]ArraysproblemStatusunsolvedpage1category[]Arrays#
    
#User function Template for python3

class Solution:
    def longest(self, names, n):
        longest_name=names[0]
    	
    	for i in range(n):
    	    if len(names[i])>len(longest_name):
    	        longest_name=names[i]
    	 
    	return longest_name
    	
    	

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
    	n=int(input())
    	names = []
    	for i in range(n):
    		names.append(input())
    	ob = Solution()
    	print(ob.longest(names, n))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
