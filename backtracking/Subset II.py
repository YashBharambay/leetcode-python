class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(temp_list,start):
            res.append(temp_list[:])
            for i in range(start, len(nums)):
                if(i > start and nums[i] == nums[i-1]): 
                    continue
                temp_list.append(nums[i])
                backtrack(temp_list, i + 1)
                temp_list.pop()
        nums.sort()
        backtrack([],0)
        return res
