
def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    # Get sign and work with absolute value
    sign = -1 if x < 0 else 1
    x = abs(x)

    reversed_num = 0
    while x != 0:
        digit = x % 10
        x //= 10

        # Check for overflow before actually multiplying/adding
        if (reversed_num > INT_MAX // 10 or
           (reversed_num == INT_MAX // 10 and digit > INT_MAX % 10)):
            return 0

        reversed_num = reversed_num * 10 + digit

    return sign * reversed_num


# ---- Test cases ----
print(reverse(123))    # 321
print(reverse(-123))   # -321
print(reverse(120))    # 21
print(reverse(1534236469))  # 0 (overflow case)
