#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

while True:
    user_words: str = input('Введите нескольких слов, разделённых пробелами >>> ')
    if user_words.isspace():
        print('Oшибка ввода, введите нескольких слов, разделённых пробелами >>> ')
        break

    for idx, word in enumerate(user_words.split(), 1):
        if len(word) > 10:
            print(idx, word[0:10])
        else:
            print(idx, word)




