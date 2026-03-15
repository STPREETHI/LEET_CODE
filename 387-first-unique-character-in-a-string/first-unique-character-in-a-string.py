class Solution:
    def firstUniqChar(self, s: str) -> int:
        h={}
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        for i in range(len(s)):
            ch=s[i]
            if h[ch]==1:
                return i
        return -1        