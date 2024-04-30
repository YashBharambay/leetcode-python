class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(temp_list, start,total):
            if total == target:
                res.append(temp_list[:])
            elif total>target:
                return
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    temp_list.append(candidates[i])
                    backtrack(temp_list, i+1,total + candidates[i])
                    temp_list.pop()

        candidates.sort()
        backtrack([],0,0)
        return res
