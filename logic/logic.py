import math
def is_even(n:int)-> bool:
    number = n % 2
    return math.isclose (number, 0)

def in_an_interval(n: float) -> bool:
    range1 = (2 <= n) and  (n < 9)
    range2 = (47 < n) and  (n < 92)
    range3 = (12 < n) and (n <= 19)
    range4 = (101 < n) and (n <= 103)
    return range1 or range2 or range3 or range4

