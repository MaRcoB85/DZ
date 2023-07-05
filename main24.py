def second_largest_number(lst):
    if not lst:
        return None
    largest = float('-inf')  # float('-inf') - це від'ємна нескінченність
    second_largest = float('-inf')  # float('-inf') - це від'ємна нескінченність
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest


print(second_largest_number([1, 2, 2]))
print(second_largest_number([]))
