### 1. Проверка на существование треугольника и определение его типа:
def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a != b and a != c and b != c:
            print("Треугольник разносторонний.")
        elif a == b == c:
            print("Треугольник равносторонний.")
        else:
            print("Треугольник равнобедренный.")
    else:
        print("Треугольника с такими сторонами не существует.")

# Пример использования
check_triangle(3, 4, 5)  # Вы укажите свои значения сторон a, b, c здесь