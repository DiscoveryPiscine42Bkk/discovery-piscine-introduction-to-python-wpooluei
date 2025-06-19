original_array = [2, 8, 9, 48, 8, 22, -12, 2]
seen = set()

print("2 8 9 48 22 -12:")
for value in original_array:
    if value not in seen:
        print(value, end=' ')
        seen.add(value)