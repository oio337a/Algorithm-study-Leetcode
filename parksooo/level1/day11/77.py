from itertools import combinations
from typing import List

def combine(n: int, k: int) -> List[List[int]]:
    res = [i + 1 for i in range(n)]
    res = list(combinations(res, k))
    return res

print(combine(4, 2))