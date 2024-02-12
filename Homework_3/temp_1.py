### 1. Удаление дубликатов из списка повторяющихся элементов:
def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

# Пример использования
input_list = [1, 2, 2, 3, 4, 4, 5]
result_list = remove_duplicates(input_list)
print("Список без дубликатов:", result_list)