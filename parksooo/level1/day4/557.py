def reverseWords(s: str) -> str:
	spl = s.split(" ")
	res = ""
	for i in range(len(spl)):
		res += spl[i][::-1]
		# [::-1] 문자열을 뒤집어주는 내장함수를 사용했습니다! 그리고 빈문자열에 더해줬어요!
		if i != len(spl) - 1:
			res += " "
			#마지막에는 ' ' 들어가면 안되서 if로 걸러주었습니둥!
	return res