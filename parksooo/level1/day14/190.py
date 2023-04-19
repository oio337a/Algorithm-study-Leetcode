class Solution:
	def reverseBits(self, n: int) -> int:
		binary = (bin(n))[2:][::-1] # 2진수로 바꾸어주는 함수, 0b를 뺴고 나머지를 역순으로 바꿈
		res = binary + "0"*(32 - len(binary)) # 32비트에 맞추어야하기에 32 - len 나머지를 0으로 채움
		return int(res, 2) #2진수를 int 형으로 바꾸어준다

test = Solution()
n = 0b00000010100101000001111010011100
print(test.reverseBits(n))
