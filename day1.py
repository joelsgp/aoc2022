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


print(max(sums))
