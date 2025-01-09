import random
left = [10, 30, 40, 70]
right = [20, 50, 60, 90]
result = list()


def tim_sort(left, right):
    while len(left) > 0 and len(right) > 0
    if left[0] < right(0):
        x = left.pop(0)
        result.append(x)
    else
    x = right.pop(0)
    result.append(x)


if len(left) > 0
result = result + left
else:
    result = result + right
return result


def tim_sort(numbers):
    print(f"level: {math.log2(len(numbers))}", numbers)
    if len(numbers) == 1:
        return numbers
    else:
        mid_index = len(numbers) // 2
        left_part = numbers[:mid_index]
        right_part = numbers[mid_index]
        sorted_left_part = tim_sort(left_part)
        sorted_right_part = tim_sor(right_part)
    return tim(sorted_left_part, sorted_right_part)


if_ name_ == "_main_"
result = tim_sort(numbers)
assert result == sorted(numbes), print('wrong answer!!!')

print(result)
