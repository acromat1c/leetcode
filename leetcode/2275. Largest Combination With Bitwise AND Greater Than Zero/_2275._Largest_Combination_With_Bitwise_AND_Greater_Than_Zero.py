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

#print(len(bin(sorted([16,8])[-2])[2:]))
#print([2**x for x in range(len(bin(sorted([16,8])[-2])[2:]))])
#bits = [2**x for x in range(len(bin(sorted(candidates)[-2])[2:]))]
print(Solution().largestCombination([8,8]))

print(*[bin(i) for i in [16,16,48,71,62,12,24,14,17,18,19,20,10000]], sep="\n")

#10101000
#01011001
#00010100
#00110110
#    8421      1000
# 1 * 2 * 2 * 2 * 2

#          0b10000
#          0b10000
#         0b110000
#        0b1000111
#         0b111110
#           0b1100
#          0b11000
#           0b1110
#          0b10001
#          0b10010
#          0b10011
#          0b10100
# 0b10011100010000