OFFSET_LOWER = 1 - ord('a')
OFFSET_UPPER = 27 - ord('A')


def get_priority(item: str) -> int:
    if item.islower():
        return ord(item) - OFFSET_LOWER
    elif item.isupper():
        return ord(item) - OFFSET_UPPER


def get_duplicate(rucksack: str) -> str:
    items_both_compartments = len(rucksack)
    items_per_compartment = items_both_compartments // 2

    compartment1_set = set(rucksack[:items_per_compartment])
    compartment2_set = set(rucksack[items_per_compartment:])

    in_both = compartment1_set.intersection(compartment2_set)
    duplicate = in_both.pop()
    return duplicate


def solve(lines):
    total_priorities = 0
    for rucksack in lines:
        duplicate = get_duplicate(rucksack)
        dupe_priority = get_priority(duplicate)
        total_priorities += dupe_priority

    return total_priorities
