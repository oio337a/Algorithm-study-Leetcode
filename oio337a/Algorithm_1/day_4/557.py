# 1.

s = "Let's take LeetCode contest"
result = []
split_str = s.split() # 공백으로 자르기
for string in split_str: # 단어들 반복
    for letter in string[::-1]: # 단어들 글자 역순으로 반복
        result.append(letter) # 글자 하나씩 넣어주기
    result.append(' ') # 공백 넣기
result.pop() # 마지막 공백 제거
print(''.join(result)) # 리스트 -> 문자열 변환

# 2.
result = []
for st in s.split(): # split 한 것들 순회
    result.append(st[::-1]) # 뒤집어서 추가
print(' '.join(result)) # 공백으로 구분해서 문자열 반환

