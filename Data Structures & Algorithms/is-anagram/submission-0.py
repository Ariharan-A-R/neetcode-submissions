class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=s.strip()
        t=t.strip()
        if len(s) != len(t):
            return False
        a = [0 for _ in range(26)]
        for i in range(len(s)):
            a[ord(s[i]) - ord('a')] += 1
            
            a[ord(t[i]) - ord('a')] -= 1    
        for i in a:
            if i != 0:
                return False
        return True