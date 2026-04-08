# Вывод в консоль названия всех книг в библиотеке
def book_list_view(library):
    if not library:  # Проверка "пустоты" библиотеки
        print("Библиотека пуста.")
        return
    print("Список книг в библиотеке:")
    for book in library.keys():  #  По всем ключам-названиям книг
        print("\t", book)  #  Вывод каждого названия


#  Добавление/обновление книги
def add_book(library, title, author, year):
    choice = ''  #  параметр решения об обновлении
    if title in library:
        print(f"\nКнига '{title}' уже существует.")
        while choice != 'да' and choice != 'нет':
            choice = input(f"Хотите обновить информацию о книге '{title}'? (да/нет): ").strip().lower()
            if choice == 'нет':
                print(f"Обновление записи о книге '{title}' отменено.")
                return
            if choice != 'да':
                print("Ответ не принят. Пожалуста, в следующий раз введите или ДА, или НЕТ.")
        book_action = 'Обновление'
        presence = library[title]['наличие']
    else:
        book_action = 'Добавление'
        presence = "None"
    library[title] = {"автор": author, "год_издания": year, "наличие": presence}
    print(f"\n{book_action} записи о книге '{title}' завершено:")
    print(f"Книга '{title}' ({author}, {year})")


#  Удаление книги из библиотеки
def remove_book(library, title):
    if title not in library:
        print(f"\nКнига '{title}'отсутствует в списке книг библиотеки.")
    else:
        del library[title]
        print(f"\nКнига '{title}' успешно удалена из списка книг библиотеки.")


#  Выдача книги
def issue_book(library, title):
    if title not in library:
        print(f"\nКнига '{title}' отсутствует в списке книг библиотеки.")
        return
    if library[title]['наличие'] == "False":
        print(f"\nОшибка! Книга '{title}' уже отмечена как выданная.")
    else:
        library[title]['наличие'] = "False"
        print(f"\nКнига '{title}' отмечена как выданная.")


#  Возврат книги
def return_book(library, title):
    if title not in library:
        print(f"\nКнига '{title}' отсутствует в списке книг библиотеки.")
        return
    if library[title]['наличие'] == "True":
        print(f"\nОшибка! Книга '{title}' уже отмечена как вернувшаяся в библиотеку.")
    else:
        library[title]['наличие'] = "True"
        print(f"\nКнига '{title}' отмечена как вернувшаяся в библиотеку.")


#  Поиск книги по названию
def find_book(library, title):
    if title not in library:
        print(f"\nКнига '{title}' отсутствует в списке книг библиотеки.")
        return
#   dict = {}
    print(f"Информация о книге '{title}':\n\t- автор: {library[title]['автор']},\n\t- год издания: {library[title]['год_издания']}")


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
# book_list_view(library)
# title = "Война и мир"
# author = "Лев Толстой"
# year = 1980
# add_book(library, title, author, year)
# title = "Лолита"
# author = "Владимир Набоков"
# year = 1999
# add_book(library, title, author, year)
# print('\n', library)  #  для контроля происходящего
#
# title = 'Война и мир'
# remove_book(library, title)
# print("\n", library)  #  для контроля происходящего
# title = 'Война и мир'
# remove_book(library, title)
# print("\n", library)  #  для контроля происходящего
#
# title = "QWERTY"
# issue_book(library, title)
# return_book(library, title)
# title = "Лолита"
# issue_book(library, title)
# title = "Война и мир"
# issue_book(library, title)
# issue_book(library, title)
title = "Мастера и Маргарита"
# return_book(library, title)
# return_book(library, title)
# print("\n", library)  #  для контроля происходящего
find_book(library, title)
title = "QWERTY"
find_book(library, title)