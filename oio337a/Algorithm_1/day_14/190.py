class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:][::-1]
        res = b + "0" * (32 - len(b))
        return int(res, 2)
        # num = int((bin(n))[2:][::-1], 2)
        # print(num)
        # if n == 0:
        #     return 0
        # num = 0
        # for i in range(31, -1, -1):
        #     if n == 0:
        #         break
        #     if n % 2 != 0:
        #         num += 2 ** i
        #     n /= 2
        return num

'''
3 = 0000000000000000000000000011
1100000000000
111111111111111111111111111101
00000000000000000000000000000000
00000010100101000001111010011100
'''
n = 0b01000000000000000000000000000000
test = Solution()
print(test.reverseBits(n))