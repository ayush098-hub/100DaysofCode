Q_L: https://www.codingninjas.com/codestudio/problems/check-if-the-string-is-a-palindrome_1062633?utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_5&leftPanelTab=1

import re
def tolowercase(s):
    i=0
    ch2=''
    while s[i::]:
        ch=ord(s[i])
        if ch > 64 and ch<91:
            ch2+=chr(ch+32)
        else:
            ch2+=chr(ch)
        i=i+1
    return ch2

def removespecial(s):
    s = re.sub(r"[^a-zA-Z0-9]","",tolowercase(s))
    return s
    
def checkpalindrome(s):

    s=removespecial(s)
    # print(s)
#two pointer
    i=0
    e=len(s)-1
    while i<=e:
        if s[i]!=s[e]:
            return 0
        else:
            i+=1
            e-=1
    return 1

#reverse array approach
    # s1=s[::-1]

    # if s==s1:
    #     return 1
    # else:
    #     return 0
    


s='121xox121'

print(checkpalindrome(s))
