### 2. Подсчет частоты встречаемых слов в тексте:
from collections import Counter
import re

def most_common_words(text, n=10):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    most_common = word_counts.most_common(n)
    return most_common

# Пример использования
text = "your large input text here"
common_words = most_common_words(text, 10)
print("Наиболее часто встречаемые слова:", common_words)