Question_link: https://practice.geeksforgeeks.org/problems/intersection-of-two-arrays2404/1/?category[]=Arrays&category[]=Arrays&problemStatus=unsolved&difficulty[]=0&page=2&query=category[]ArraysproblemStatusunsolveddifficulty[]0page2category[]Arrays#

def intersection(a,b):
    # count=0

    # for i in range(len(a)):
    #     for j in range(len(b)):
    #         if a[i]<b[j]:
    #             pass
    #         elif a[i]==b[j]:
    #             count=count+1

    # return count
    
    
    #optiised code

     res=set(a).intersection(set(b))
     ans=len(res)
     print(set(a))
     print(set(b))
     print(res)
     return ans




a=[1, 2, 3, 4, 5, 6]
b=[3, 4, 5, 6, 7]

print(intersection(a,b))
