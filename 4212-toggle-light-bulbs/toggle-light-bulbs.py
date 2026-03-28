class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        state = [0] * 101
        
        for b in bulbs:
            state[b] ^= 1
        
        return [i for i in range(1, 101) if state[i] == 1]