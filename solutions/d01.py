def solve(lines):
    sums = []
    current_sum = 0
    for li in lines:
        try:
            current_sum += int(li)
        except ValueError:
            sums.append(current_sum)
            current_sum = 0

    sums.sort(reverse=True)
    top3 = sums[:3]
    total = sum(top3)

    return total
