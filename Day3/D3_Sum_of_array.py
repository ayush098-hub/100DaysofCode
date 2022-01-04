
Question_link: https://practice.geeksforgeeks.org/problems/sum-of-array-elements2502/1/?category[]=Arrays&category[]=Arrays&problemStatus=unsolved&page=1&query=category[]ArraysproblemStatusunsolvedpage1category[]Arrays
    
#User function Template for python3

def sumElement(arr,n):
    sum=0
    
    for i in range(n):
        sum=sum+arr[i]
    return sum
    #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    testCase=int(input())
    
    for _ in range(testCase):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        print(sumElement(arr,n))
# } Driver Code Ends
    
