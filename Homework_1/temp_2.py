### 2. Проверка числа на простоту:
def is_prime(num):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    return False

# Запрос числа
num = int(input("Введите число (от 2 до 100000): "))
if num < 2 or num > 100000:
    print("Пожалуйста, введите число от 2 до 100000.")
else:
    if is_prime(num):
        print("Число", num, "является простым.")
    else:
        print("Число", num, "является составным.")