class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_temp = []
        t_temp = []
        for letter in s:
            if letter == '#' and s_temp:
                s_temp.pop()
                continue
            elif letter != '#':
                s_temp.append(letter)
        for letter in t:
            if letter == '#' and t_temp:
                t_temp.pop()
                continue
            elif letter != '#':
                t_temp.append(letter)
        return s_temp == t_temp


s = "ab#c"
t = "ad#c"
test = Solution()
print(test.backspaceCompare(s, t))
