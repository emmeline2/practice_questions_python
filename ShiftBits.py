class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        power = 31
        while n:
            # shift bits based on position, if 1
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret
        
