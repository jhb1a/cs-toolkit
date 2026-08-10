num1 = 10
num2 = 3


def divideTwoInt(dividend: int, divisor: int) -> int:
    negative = (dividend < 0) != (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    n = 0
    INT_MAX = 2**31 -1

    while dividend >= divisor:
        chunk = divisor
        multiple = 1

        while dividend >= chunk + chunk:
            chunk += chunk
            multiple += multiple

        dividend -= chunk
        n += multiple

    result = -n if negative else n

    if result > INT_MAX:
        return INT_MAX
    return result


print(divideTwoInt(num1, num2))
