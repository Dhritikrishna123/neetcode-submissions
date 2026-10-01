class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for _ , x in enumerate(nums):
            if x in seen:
                return True
            seen.add(x)
        return False