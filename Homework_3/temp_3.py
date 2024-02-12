### 3. Определение набора предметов, помещающихся в рюкзак до максимальной грузоподъемности:
def fit_items_backpack(items, weights, max_weight):
    fitted_items = []
    current_weight = 0
    for item, weight in zip(items, weights):
        if current_weight + weight <= max_weight:
            fitted_items.append(item)
            current_weight += weight
    return fitted_items

# Пример использования
items = ["sleeping bag", "tent", "food", "water", "clothes"]
weights = [2, 3, 5, 2, 4]  # масса каждого предмета
max_backpack_weight = 10
fit_result = fit_items_backpack(items, weights, max_backpack_weight)
print("Вещи, влезающие в рюкзак:", fit_result)