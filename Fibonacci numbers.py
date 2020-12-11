# Meaning
value_1 = 0
value_2 = 1
cycle = 0
CONST_LIMIT = 2

# Options
max_number = 100000**10
program_limit = 10 - CONST_LIMIT
min_cycle_number = 0

while value_2 < max_number:
    cycle += 1
    if cycle > program_limit:
        print('Loop stopped, no result found')
        break

    next_value_2 = value_1 + value_2
    next_value_1 = value_2
    value_1 = next_value_1
    value_2 = next_value_2
    if cycle < min_cycle_number:
        continue

    print(cycle + CONST_LIMIT, ' - ', value_2)

else:
    print("The total number of cycles was", cycle + CONST_LIMIT, "Final result ", value_2)
