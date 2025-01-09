numbers = [40, 30, 50, 60, 20]

answer = [40]
new = 30
if answer:
    is_insert = False
    for index, num in enumerate(answer):
        if new < num:
            is_insert = True
            answer = answer[:index] + [new] + answer[index:]
            break
    if not is_insert:
        answer = answer + [new]
else:
    answer = [new]

print(answer)


numbers = [40, 30, 50, 60, 20]
answer = list()
for new in numbers:
    if answer:  # 不是空的
        is_insert = False
        for index, num in enumerate(answer):  # enumerate 同時給你編碼跟對應編號的值
            if new < num:
            is_insert = True
            answer = answer[:index] + [new] + answer[index:]
            break
         if not is_insert:
            answer = answer + [new]
    else: # 第一張牌
        answer = [new]

print(answer)