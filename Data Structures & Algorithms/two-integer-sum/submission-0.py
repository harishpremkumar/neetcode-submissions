class Solution:
    def twoSum(self, nums, target: int) -> List[int]:
        stack = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    tup = i, j
                    for k in tup:
                        stack.append(k)
                    return stack    
