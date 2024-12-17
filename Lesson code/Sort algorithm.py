import math_problems


# Selection sort
#  a circle
nums = [40, 30, 60, 50, 20]

min_index = 0
for index in range(1, len(nums)):

    if nums[index] < nums[min_index]:
        min_index = index
    print(min_index)
    nums[0], nums[min_index] = nums[min_index], nums[0]
    print(nums)

if__name__ == "__main__":
    print("ABC")
    nums = [40, 50, 60, 30, 20]
    print('Bubble Sort:'，bubble_sort(nums))
    print("Selection Sort: ", selection_sort(nums, is_log=True))
else
print("ABC:", __name__)


# Bubble sort
# a circle

nums = [40, 30, 60, 50, 20]

for index in range(len(nums)-1):
    print(index, index+1)
    print(nums[index], nums[index+1])


# Get prime
def get_prime(max_limit=10000):
    primes = list()
    nums = 2
    while nums < max_limit:
        is_prime = True
        for i in primes:
            if nums % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(nums)
        nums += 1
    return primes


# triangle
def get_right_angle_edge(edge_1, edge_2):
    answer = list()
    answer.append((edge_1 ** 2 + edge_2 ** 2) ** 0.5)

    if edge_1 != edge_2:
        answer += (abs(edge_1 ** 2 + edge_2 ** 2) ** 0.5)
    return answer
