import random

def load_words_from_file(filename):           #пары слово-определение
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            words = {}
            for line in file:
                line = line.strip()
                if ' - ' in line:
                    try:
                        word, definition = line.split(' - ', 1)
                        words[word.lower()] = definition.strip() #добавление в словарь ниж рег
                    except ValueError:
                        print(f"Пропускаю неверную строку: {line}")
            return words
    except FileNotFoundError:               #файл не найден
        print(f"Ошибка: файл ‘{filename}’ не найден.")
        return None

def play_game(words):
    if words is None or not words:           #проверка словаря
        print("Загрузка слов не удалась. Выход.")
        return

    word_to_guess = random.choice(list(words.keys()))
    word_lower = word_to_guess.lower()
    attempts = 7
    guessed_letters = set()         #хранение угад букв

    print(f"Определение: {words[word_to_guess]}")

    while attempts > 0:
        display_word = ''.join(letter if letter.lower() in guessed_letters else '_' for letter in word_to_guess)
        print(f"Слово: {display_word}")

        guess = input("Угадайте букву или слово: ").lower()

        if guess.isalpha():         #проверка сосстоит из букв
            if len(guess) == 1:
                if guess in guessed_letters:
                    print("Вы уже угадали эту букву.")
                    continue
                guessed_letters.add(guess)
                if guess in word_lower:
                    print("Правильно!")
                    if all(letter.lower() in guessed_letters for letter in word_to_guess):
                        print(f"Поздравляем! Вы угадали слово: {word_to_guess}")
                        return
                else:
                    attempts -= 1
                    print(f"Неправильно! У вас осталось {attempts} попыток.")
            elif guess == word_lower:
                print(f"Поздравляем! Вы угадали слово: {word_to_guess}")
                return
            else:
                attempts -= 1
                print(f"Неправильно! У вас осталось {attempts} попыток.")

        else:
            print("Пожалуйста, введите букву или слово.")


    print(f"Вы проиграли! Загаданное слово: {word_to_guess}")


if __name__ == "__main__":
    words = load_words_from_file('words_definitions.txt')
    play_game(words)
    input("Нажмите Enter для выхода...")