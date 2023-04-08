def reverseString(s: List[str]) -> None:
	for i in range(len(s) // 2):
		l = len(s) - i - 1
		temp = s[i]
		s[i] = s[l]
		s[l] = temp
		#별 다르게 생각안하고 반 뚝 잘라서 스왑스켜주었습니다!!