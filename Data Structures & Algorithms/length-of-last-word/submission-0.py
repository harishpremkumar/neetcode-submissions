class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.strip().split()
        return len(new[-1])


if __name__ == "__main__":
    obj = Solution()
    result = obj.lengthOfLastWord("   fly me   to   the moon  ")
    print(result)
        