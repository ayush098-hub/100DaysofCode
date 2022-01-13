Question_Link:https://practice.geeksforgeeks.org/problems/kth-element-in-matrix/1/?company[]=Amazon&company[]=Amazon&difficulty[]=1&page=1&category[]=Matrix&query=company[]Amazondifficulty[]1page1company[]Amazoncategory[]Matrix
    
    
#User function Template for python3

def kthSmallest(mat, n, k): 
    result=[]
    for i in range(n):
        for j in range(n):
            result.append(mat[i][j])
            
    result.sort()
    
    return result[k-1]



#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Driver Code 

def main():
    T=int(input())
    while(T>0):
        n = int(input())
        mat=[[0 for j in range(n)] for i in range(n)]
        line1=[int(x) for x in input().strip().split()]
        k = int(input())

        temp=0
        for i in range(n):
            for j in range (n):
                mat[i][j]=line1[temp]
                temp+=1
        
        print(kthSmallest(mat, n, k))
        T-=1


if __name__=="__main__":
    main()



