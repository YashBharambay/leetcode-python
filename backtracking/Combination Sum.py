class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack( temp_list, total, start):
            if total > target:
                return
            if total == target: 
                result.append(temp_list[:])
                return
                
            for i in range(start, len(nums)):
                temp_list.append(nums[i])
                backtrack(temp_list,total + nums[i], i)
                temp_list.pop()
        
        # nums.sort()
        backtrack([], 0, 0)
        return result

            
