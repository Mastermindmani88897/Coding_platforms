class Solution:
    def profession(self, level, pos):
        
        x = pos - 1
        
        if bin(x).count('1') % 2 == 0:
            return "Engineer"
        else:
            return "Doctor"