### 3. Угадай число за 10 попыток:
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num_to_guess = randint(LOWER_LIMIT, UPPER_LIMIT)

attempts = 10
for _ in range(attempts):
    guess = int(input(f"Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: "))
    
    if guess < num_to_guess:
        print("Больше.")
    elif guess > num_to_guess:
        print("Меньше.")
    else:
        print("Угадали!")
        break
    attempts -= 1

if attempts == 0:
    print("У вас закончились попытки. Загаданное число было:", num_to_guess)