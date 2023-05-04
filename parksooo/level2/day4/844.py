class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        x, y = [], []
        for i in range(len(s)):
            if x and s[i] == '#': # #앞의 것을 pop 해버린다
                x.pop()
            else :
                if s[i] != '#': # 아니면 append
                    x.append(s[i])
        for i in range(len(t)):
            if y and t[i] == '#':
                y.pop()
            else :
                if t[i] != '#':
                    y.append(t[i])
        print(x, y)
        if x == y: # 같으면 투루
            return True
        return False

test = Solution()
print(test.backspaceCompare("ab##", "c#d#"))