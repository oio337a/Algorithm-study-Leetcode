class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_temp = []
        t_temp = []
        for letter in s: # s 확인
            if letter == '#' and s_temp: # '#'이 있고 temp에 값이 있으면
                s_temp.pop() # temp 의 값 빼고 다음으로
                continue
            elif letter != '#': # 백스페이스 없으면 값 추가
                s_temp.append(letter)
        for letter in t: # t 확인 로직 상동
            if letter == '#' and t_temp:
                t_temp.pop()
                continue
            elif letter != '#':
                t_temp.append(letter)
        return s_temp == t_temp # 남은 temp값 비교


s = "ab#c"
t = "ad#c"
test = Solution()
print(test.backspaceCompare(s, t))
