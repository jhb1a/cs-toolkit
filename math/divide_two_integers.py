num1 = 10
num2 = 3


def divideTwoInt(dividend: int, divisor: int) -> int:
    n = 0

    while dividend >= divisor:
        chunk = divisor
        multiple = 1

        while dividend >= chunk + chunk:
            chunk += chunk
            multiple += multiple

        dividend -= chunk
        n += multiple
    return n


print(divideTwoInt(num1, num2))
