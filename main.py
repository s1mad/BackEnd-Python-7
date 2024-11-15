"""
Этот модуль вызывает функции из модуля string_operations.py для демонстрации их работы.
"""

from string_operations import (
    formatted_string,
    repeated_string,
    substring_count,
    extract_substring,
    find_latin_words,
    is_palindrome,
    normalize_whitespace,
    replace_sentence_endings,
    reverse_words,
    capitalize_each_word,
    remove_vowels
)


def main():
    """
    Основная функция для последовательного вызова всех функций из string_operations.py.
    """

    # Шаг 1
    print(formatted_string("Alice", 15, 20))

    # Шаг 2
    repeated_string("RepeatMe", 3)

    # Шаг 3
    print("Count of 'test':", substring_count("This is a Test. Testing is fun!", "test"))

    # Шаг 4
    print("Extracted substring:", extract_substring("Hello, World!", 1, 5))

    # Шаг 5
    latin_words, count = find_latin_words("Пример текста", "Hello мир", "текст C0ntains latin")
    print(f"Latin words: {latin_words}, Count: {count}")

    # Шаг 6
    print("Is palindrome:", is_palindrome("A man, a plan, a canal, Panama"))

    # Шаг 7
    print("Normalized length:", normalize_whitespace("  Hello    world   "))

    # Шаг 8
    print(replace_sentence_endings("Hello! How are you? I am fine. Thanks."))

    # Шаг 9
    print(reverse_words("Reverse these words!"))
    print(capitalize_each_word("capitalize each word"))
    print(remove_vowels("Remove vowels from this sentence"))


if __name__ == "__main__":
    main()
