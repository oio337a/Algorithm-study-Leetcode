def climbStairs(n: int) -> int:
    first, second = 1, 1
    for i in range(n - 1):
        temp = first + second # 첫 번째 와 두번쨰 값을 더해서 temp에 넣어놓는다 
        first = second # 첫번째를 두번째 값으로 만들어준다
        second = temp # 두번째를 첫번쨰로 만들어준다 즉, dp를 활용하는 문제이다 n - 2, n -1, n!!
    return second

print(climbStairs(5))