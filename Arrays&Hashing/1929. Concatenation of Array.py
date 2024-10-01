class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # ans = [0]*n*2
        # for i in range(len(nums)):
        #     ans[i], ans[n+i] = nums[i], nums[i]
        # return ans

        ans = []

        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
        
