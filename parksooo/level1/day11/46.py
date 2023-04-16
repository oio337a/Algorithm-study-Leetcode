from typing import List
from itertools import permutations

def permute(nums: List[int]) -> List[List[int]]:
    res = list(permutations(nums, len(nums)))
    return res

print(permute([1,2,3]))
