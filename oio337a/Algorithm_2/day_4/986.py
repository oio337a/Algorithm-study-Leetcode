from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0 # 처음 인덱스 세팅

        result = [] # 결과 값 리턴할 배열
        while i < len(A) and j < len(B): # A 또는 B가 있을 때까지 반복
            a_start, a_end = A[i] # A 의 0, 1 인덱스 세팅
            b_start, b_end = B[j] # B 의 0, 1 인덱스 세팅
            if a_start <= b_end and b_start <= a_end: # 시작과 끝을 비교해 시작 위치가 작으면 값이 중복되는 구간이 있음 
                result.append([max(a_start, b_start), min(a_end, b_end)]) # 시작위치의 큰값과, 종료위치의 작은값 저장
            if a_end <= b_end: # A의 끝값이 B보다 작으면 A리스트의 다음 인덱스 확인
                i += 1
            else:
                j += 1 # 아니면 B인덱스 추가
        return result


A = [[0, 2], [5, 10], [13, 23], [24, 25]]
B = [[1, 5], [8, 12], [15, 24], [25, 26]]

test = Solution()
print(test.intervalIntersection(A, B))
