def validate(n):
    digits = [int(i) for i in str(n)]
    if len(digits) % 2 == 0:
        digits = [y * 2 if x % 2 == 0 else y for x, y in enumerate(digits)]
    else:
        digits = [y * 2 if x % 2 != 0 else y for x, y in enumerate(digits)]
    return digits


print(validate(1714))
