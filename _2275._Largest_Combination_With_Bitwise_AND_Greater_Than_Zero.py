class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        if len(candidates) == 1: return 1
        bits = [2**x for x in range(len(bin(sorted(candidates)[-2])[2:]))]
        for bit in bits:
            count = 0
            for number in candidates:
                if number & bit > 0:count += 1
            if count > bits[0]: bits[0] = count
        return bits[0]

print(Solution().largestCombination([8,8]))
