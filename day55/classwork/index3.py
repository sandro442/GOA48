def solve(s):
    upper_count = 0
    lower_count = 0

    for char in s:
        if char.isupper():
            upper_count += 1
        else:
            lower_count += 1

    if upper_count == lower_count:
        return s.lower()
    if lower_count > upper_count:
        return s.lower()
    else:
        return s.upper()