def addBinary(a: str, b: str) -> str:
    result = []
    carry = 0
    i = 1
    max_len = max(len(a), len(b))

    while i <= max_len:
        