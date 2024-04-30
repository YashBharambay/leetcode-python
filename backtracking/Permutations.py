class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(temp_list):
            if len(temp_list) == len(nums):
                res.append(temp_list.copy())
                return
            for i in range(len(nums)):
                if nums[i] in temp_list: continue
                temp_list.append(nums[i])
                backtrack(temp_list)
                temp_list.pop()

        backtrack([])
        return res
        
