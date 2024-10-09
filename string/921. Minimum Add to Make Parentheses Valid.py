class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openParen, minAddReq = 0 , 0
        for char in s:
            if char == '(':
                openParen += 1
            elif char == ')' and openParen>0:
                openParen -= 1
            else:
                minAddReq +=1
        return openParen + minAddReq
        
