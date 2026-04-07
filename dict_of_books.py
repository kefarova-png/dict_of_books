# Вывод в консоль названия всех книг в библиотеке
def book_list_view(library):
    if not library:  # Проверка "пустоты" библиотеки
        print("Библиотека пуста.")
        return
    print("Список книг в библиотеке:")
    for book in library.keys():  #  По всем ключам-названиям книг
        print("\t", book)  #  Вывод каждого названия


def add_book(library, title, author, year):
    choice = ''  #  параметр решения об обновлении
    if title in library:
        print(f"\nКнига '{title}' уже существует.")
        while choice != 'да' and choice != 'нет':
            choice = input(f"Хотите обновить информацию о книге '{title}'? (да/нет): ").strip().lower()
            if choice == 'нет':
                print(f"Обновление записи о книге '{title}' отменено.")
                return
            if choice == 'да':
                book_info = library[title]  #  получаем словарь книги title для обновления
            else:
                print("Ответ не принят. Пожалуста, в следующий раз введите или ДА, или НЕТ.")
        book_action = 'Обновление'
        presence = library[title]['наличие']
    else:
        book_action = 'Добавление'
        presence = "None"
    library[title] = {"автор": author, "год_издания": year, "наличие": presence}
    print(f"\n{book_action} записи о книге '{title}' завершено:")
    print(f"Книга '{title}' ({author}, {year})")


library = {
    "Война и мир": {
        "автор": "Лев Толстой",
        "год_издания": 1869,
        "наличие": "True"
    },
    "Мастера и Маргарита": {
        "автор": "Михаил Булгаков",
        "год_издания": 1967,
        "наличие": "False"
    }
}
book_list_view(library)
title = "Война и мир"
author = "Лев Толстой"
year = 1980
add_book(library, title, author, year)
title = "Лолита"
author = "Владимир Набоков"
year = 1999
add_book(library, title, author, year)
print('\n', library)  #  для контроля происходящего