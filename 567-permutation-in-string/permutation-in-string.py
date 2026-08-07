class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = [0] * 26

        for ch in s1:
            freq1[ord(ch) - ord('a')] += 1

        wind_size = len(s1)

        for i in range(len(s2)):
            wind_freq = [0] * 26
            windind = 0
            ind = i

            while windind < wind_size and ind < len(s2):
                wind_freq[ord(s2[ind]) - ord('a')] += 1
                windind += 1
                ind += 1

            if wind_freq == freq1:
                return True

        return False