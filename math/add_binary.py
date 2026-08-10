def addBinary(a: str, b: str) -> str:
    result = []
    carry = 0
    i = 1
    max_len = max(len(a), len(b))

    while i <= max_len:
       digit_a = int(a[-i]) if i <= len(a) else 0
       digit_b = int(b[-i]) if i <= len(b) else 0

       total = digit_a + digit_b + carry
       result.append(str(total % 2))
       carry = total // 2
       i += 1

    if carry:
        result.append(str(carry))
    result.reverse()

    return "".join(result)
