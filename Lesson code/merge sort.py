left = [10, 30, 40, 70]
right = [20, 50, 60, 90]
result = list()

while len(left) > 0 and len(right) > 0
if left[0] < right(0):
    x = left.pop(0)
    result.append(x)
    else
    x = right.pop(0)
    result.append(x)

if len(left) > 0
result = result + left
else
result = result + right

print(result)
