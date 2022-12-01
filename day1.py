with open('input') as file:
    lines = file.readlines()


sums = []
current_sum = 0
for li in lines:
    try:
        current_sum += int(li.strip())
    except ValueError:
        sums.append(current_sum)
        current_sum = 0


sums.sort(reverse=True)
top3 = sums[:3]
total = sum(top3)
print(total)
