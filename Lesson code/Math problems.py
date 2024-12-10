# P31 Tuple example
list_height = [165, 170, 175]
list_name = ['Tony', 'Mark', 'Selina']

tuple_a = (list_height[0],list_name[0])
tuple_b = (list_height[1],list_name[1])
tuple_c = (list_height[2],list_name[2])

tuple_a, tuple_b, tuple_c


# Fibonacci 數列 - while with break
F0 = FN_2 = 1
F1 = FN_1 = 1
while True:
    FN = FN_1 + FN_2
    if FN < 10000:
        print(FN)
    else:
        break # 強制跳出"迴圈"
    FN_1, FN_2 = FN, FN_1

print("Over")


# with continue: "跳過"本次迴圈的剩餘部分，直接執行下次迴圈
primes = list()
nums = 2
primes.append(2)
while nums < 10000:
    is_prime = { False for i in primes if nums % i == 0}
    nums += 1
    if is_prime == {}:
        continue
    primes.append(nums - 1)

print(primes)

