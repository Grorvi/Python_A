### 1. Сложение и произведение дробей в формате "a/b":
from fractions import Fraction

def operate_fractions(fraction1, fraction2):
    num1, denom1 = map(int, fraction1.split('/'))
    num2, denom2 = map(int, fraction2.split('/'))
    
    fraction_sum = Fraction(num1, denom1) + Fraction(num2, denom2)
    fraction_product = Fraction(num1, denom1) * Fraction(num2, denom2)
    
    return fraction_sum, fraction_product

# Запрос двух дробей
fraction1 = input("Введите первую дробь в формате a/b: ")
fraction2 = input("Введите вторую дробь в формате a/b: ")

sum_result, product_result = operate_fractions(fraction1, fraction2)
print("Сумма дробей:", sum_result)
print("Произведение дробей:", product_result)