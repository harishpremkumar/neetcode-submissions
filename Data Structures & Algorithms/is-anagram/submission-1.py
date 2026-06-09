class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
s = Solution()
result = s.isAnagram(s='jar',t='jam')
print(result)
        