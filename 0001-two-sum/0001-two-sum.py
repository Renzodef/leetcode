class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_hashmap = {}
        for i, x in enumerate(nums):
            if x in index_hashmap:
                return [index_hashmap[x], i]
            complement = target - x
            index_hashmap[complement] = i