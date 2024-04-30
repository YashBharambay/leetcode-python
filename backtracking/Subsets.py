class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack( temp_list, start):
            result.append(temp_list[:])
            for i in range(start, len(nums)):
                temp_list.append(nums[i])
                backtrack(temp_list, i + 1)
                temp_list.pop()
        
        # nums.sort()
        backtrack([], 0)
        return result
