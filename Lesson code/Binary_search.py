
numbers = [40, 30, 50, 60, 20]
target = numbers
start = 0
end = len(numbers) - 1
while start <= end:
    mid = (start + end)//2
    mid_value = numbers[mid]
    if mid_value < target:
        start = mid + 1
    elif mid_value > target:
        end = mid - 1
    else:
        print("Find target at ", mid)
        break

# need to rewrite the binary search code -
