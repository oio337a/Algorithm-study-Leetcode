from collections import deque
def length_of_longest_substring(self, s: str) -> int:
    max_len = 0

    q = deque()
    for letter in s:
        if letter not in q: # 큐에 들어있지 않다면 삽입한다.
            q.append(letter)
        else: # 큐에 이미 있는 경우
            index = q.index(letter) # 큐에 들어있다면 index를 찾는다
            for j in range(index + 1): # 인덱스까지의 모든 요소를 pop 한다.
                q.popleft()
            q.append(letter) # 다시 문자열을 넣어준다.
        max_len = max(max_len, len(q)) # 문자열이 들어오고 나갈때 마다 최대값을 비교한다.
    return max_len