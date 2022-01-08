Question_Link: https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1#
    
 
# User function Template for python3
def reverse(s):
    i=0
    e=len(s)-1
    
    while i<e:
        s[i],s[e]=s[e],s[i]
        i+=1
        e-=1
class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,string):
        words=string.split('.')
        reverse(words)
        words=".".join(words)
        return words
