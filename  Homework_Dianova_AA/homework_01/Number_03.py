# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
# ввёл число 3. Считаем 3 + 33 + 333 = 369.

# 1 вариант
n = input("Введите число n: ")
print(int(n) + int(n * 2) + int(n * 3))

# 2 вариант
n = input("Введите число n: ")
i: int = 1
sum_num = 0

while i <= 3:
    sum_num = sum_num + int(n * i)
    i += 1
print(sum_num)