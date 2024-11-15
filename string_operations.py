"""
Модуль содержит функции для работы со строками.
"""

import re


# Шаг 1: Функция с форматированием строки
def formatted_string(name, number1, number2):
    """
    Формирует строку с подстановкой:
    - name: строка
    - number1: результат арифметической операции
    - number2: результат вызова другой функции
    """

    def double_number(n):
        return n * 2

    result = (
        f"Hello, {name}! Your first number is {number1 + 10}, "
        f"and double of your second is {double_number(number2)}."
    )
    return result


# Шаг 2: Функция повторений строк
def repeated_string(base, repeat):
    """
    Выводит строку, состоящую из повторений базовой строки (каждое на новой строке).
    """
    result = (base + "\n") * repeat
    print(result.strip())


# Шаг 3: Функция подсчёта вхождений подстроки без учёта регистра
def substring_count(text, sub):
    """
    Возвращает количество вхождений подстроки sub в текст text без учёта регистра.
    """
    return text.lower().count(sub.lower())


# Шаг 4: Функция извлечения подстроки
def extract_substring(s, start, end):
    """
    Извлекает подстроку между индексами start и end (однострочная реализация).
    """
    return s[start:end]


# Шаг 5: Функция поиска латинских символов
def find_latin_words(*args):
    """
    Ищет слова, содержащие латинские буквы. Возвращает:
    - Список строк, где найдены латинские буквы
    - Количество таких слов
    """
    latin_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    count = 0

    for string in args:
        words = string.split()
        for word in words:
            if any(char in latin_chars for char in word):
                result.append(word)
                count += 1

    return result, count


# Шаг 6: Проверка строки на палиндром
def is_palindrome(s):
    """
    Проверяет, является ли строка палиндромом (без учёта регистра и пробелов).
    """
    cleaned = ''.join(filter(str.isalnum, s)).lower()
    return cleaned == cleaned[::-1]


# Шаг 7: Удаление лишних пробелов
def normalize_whitespace(s):
    """
    Удаляет лишние пробелы в строке. Возвращает длину нормализованной строки.
    """
    return len(' '.join(s.split()))


# Шаг 8: Замена окончания предложения на перенос строки
def replace_sentence_endings(text):
    """
    Заменяет окончания предложений (.!?...) на символ переноса строки.
    """
    return re.sub(r'[.!?]+', '\n', text)


# Шаг 9: Дополнительные функции работы со строками
def reverse_words(text):
    """Переворачивает слова в строке."""
    return ' '.join(word[::-1] for word in text.split())


def capitalize_each_word(text):
    """Приводит каждое слово в строке к капитализированному виду."""
    return ' '.join(word.capitalize() for word in text.split())


def remove_vowels(text):
    """Удаляет все гласные из строки."""
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return ''.join(char for char in text if char not in vowels)
