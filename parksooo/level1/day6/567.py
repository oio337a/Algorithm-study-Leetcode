def checkInclusion(s1: str, s2: str) -> bool:
	for i in range(len(s2) - len((s1) + 1)):
		s1Com = s2[i : i + len(s1)]
		# 길이만큼 substr 한다!
		if (sorted(s1Com) == sorted(s1)):
			return True
		# 아스키 코드 순으로 정렬해서 비교후 맞으면 true 리턴 ! 
	return False
