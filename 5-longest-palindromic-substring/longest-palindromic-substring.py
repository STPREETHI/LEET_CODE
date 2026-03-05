class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        if len(s)==2:
            if s[0]==s[1]:
                return s
        res=''
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                sub=s[i:j+1]
                if sub==sub[::-1] and len(sub)>len(res):
                    res=sub
        return res

        