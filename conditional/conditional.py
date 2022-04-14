def max_101(n: float, m: float) -> float:
    if n > m:
        return n
    else:
        return m

def max_of_three(x: float, y: float, z: float) -> float:
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z
def rental_late_fee(days: int) -> int:
    afee = days <= 0
    bfee = days <= 9 and days > 0
    cfee = days<= 15 and days > 9
    dfee = days<=24  and days > 15
    efee = days>24
    if afee:
        return 0
    elif bfee:
        return 5
    elif cfee:
        return 7
    elif dfee:
        return 19
    else:
        return 100