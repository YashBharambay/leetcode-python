class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = 0
        time = 0
        n = len(tickets)
        while True:
            if tickets[i] != 0:
                tickets[i] -= 1
                time += 1
            if i == k and tickets[i] == 0:
                return time
            i += 1
            if i == len(tickets):
                i = 0
        return 0 
