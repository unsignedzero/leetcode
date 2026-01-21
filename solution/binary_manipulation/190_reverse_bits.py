class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            # Interestingly + is faster than | by 3ms (51->48) ms
            result = (result<<1) + (n&1)
            n>>=1
        return result

