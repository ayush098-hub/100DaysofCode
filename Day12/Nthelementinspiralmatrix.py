Question_Link: https://practice.geeksforgeeks.org/problems/find-nth-element-of-spiral-matrix/1/?category[]=Matrix&category[]=Matrix&company[]=Amazon&company[]=Amazon&problemStatus=unsolved&difficulty[]=1&page=1&query=category[]Matrixcompany[]AmazonproblemStatusunsolveddifficulty[]1page1company[]Amazoncategory[]Matrix
    
    
# You are required to complete this fucntion
# Function should return the an integer
def findK(a, m, n, q):
    #Code here
    k = 0
    l = 0

    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''

    result=[]

    while (k < m and l < n):

        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            result.append(a[k][i])

        k += 1

        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            result.append(a[i][n - 1])

        n -= 1

        # Print the last row from
        # the remaining rows
        if (k < m):

            for i in range(n - 1, (l - 1), -1):
                result.append(a[m - 1][i])

            m -= 1

        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                result.append(a[i][l])

            l += 1
    return result[q-1]

#{ 
#  Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1
        print(findK(matrix, n[0], n[1], n[2]))
# } Driver Code Ends
