def lengthOfLongestSubstring(s: str) -> int:
	dic = {}
	# dic 선언해서 중복되지 않은 값을 넣어준다
	l = 0
	# 첫 시작 점 인덱스를 가리킨다
	res = 0
	# 결과값 즉, 가장 긴 길이
	for r in range(len(s)): #길이 만큼 탐색하면서 최장길이를 찾는다
		if s[r] not in dic:
			res = max(res, r - l + 1) # 딕셔너리에 없으면 길이를 갱신해준다 
		else :
			if dic[s[r]] < l: # 문자열 위치의 인덱스가 l 보다 작으면 다시 길이를 갱신한다 
				res = max(res, r - l + 1)
			else:
				l = dic[s[r]] + 1 # 그게 아니면 그냥~ 더해주자
		dic[s[r]] = r # 딕셔너리에 넣어준다
	return res

