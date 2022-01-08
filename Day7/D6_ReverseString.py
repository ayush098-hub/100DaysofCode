Q_L: https://leetcode.com/problems/reverse-string/submissions/
    
def reverse(str):
    s=0
    e=len(str)-1

    while s<e:
        str[s],str[e]=str[e],str[s]
        s+=1
        e-=1

str=['h','e','l','l','o']
reverse(str)
print(str)
