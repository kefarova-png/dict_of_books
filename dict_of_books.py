# Вывод в консоль названия всех книг в библиотеке
def book_list_view(library):
    if not library:  # Проверка "пустоты" библиотеки
        print("Библиотека пуста.")
        return
    print("\nСписок книг в библиотеке:")
    for book in library.keys():  #  По всем ключам-названиям книг
        print("\t", book)  #  Вывод каждого названия


#  Добавление/обновление книги
def add_book(library):
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
def remove_book(library):
    if title not in library:
        print(f"\nКнига '{title}'отсутствует в списке книг библиотеки.")
    else:
        del library[title]
        print(f"\nКнига '{title}' успешно удалена из списка книг библиотеки.")


#  Выдача книги
def issue_book(library):
    if title not in library:
        print(f"\nКнига '{title}' отсутствует в списке книг библиотеки.")
        return
    if library[title]['наличие'] == "False":
        print(f"\nОшибка! Книга '{title}' уже отмечена как выданная.")
    else:
        library[title]['наличие'] = "False"
        print(f"\nКнига '{title}' отмечена как выданная.")


#  Возврат книги
def return_book(library):
    if title not in library:
        print(f"\nКнига '{title}' отсутствует в списке книг библиотеки.")
        return
    if library[title]['наличие'] == "True":
        print(f"\nОшибка! Книга '{title}' уже отмечена как вернувшаяся в библиотеку.")
    else:
        library[title]['наличие'] = "True"
        print(f"\nКнига '{title}' отмечена как вернувшаяся в библиотеку.")


#  Поиск книги по названию с выводом статуса (наличия)
def find_book(library):
    if title not in library:
        print(f"\nКнига '{title}' отсутствует в списке книг библиотеки.")
        return
    presence_dict = {
        "True": "Книга доступна",
        "False": "Книга выдана",
        "None": "Книга в библиотеке, но ее статус не определен"
    }
    print(f'''
Информация о книге '{title}':
  - автор: {library[title]['автор']},
  - год издания: {library[title]['год_издания']}.
  - {presence_dict[library[title]['наличие']]}.''')


def library_exit(library):
    #  выход пока без сохранения изменений library
    print("\nРабота программы завершена. \nБиблиотека закрыта. \nИзменения не сохранены.")


def main_menu():
    dict_menu = {
        1: ["Посмотреть список книг", book_list_view],
        2: ["Найти книгу", find_book],
        3: ["Взять книгу", issue_book],
        4: ["Вернуть книгу", return_book],
        5: ["Добавить/Обновить книгу", add_book],
        6: ["Удалить книгу", remove_book],
        7: ["Выйти", library_exit]
    }
    max_number = len(dict_menu)
    while True:
        print("\n--- Меню библиотеки ---")
        for key in dict_menu:
            print(f"{key}. {dict_menu[key][0]}")  #  ключ словаря и 1-й элемент списка
        try:
            choice = int(input(f"\nВыберите пункт меню (1-{max_number}): ").strip())
            if choice in dict_menu:
                function_call = dict_menu[choice][1](library)  #  Вызов функции 2-й элемент списка
                if choice == 7:  # Если выбран выход – прерываем цикл
                    break
            else:
                print("Введённый номер отсутствует в списке. Попробуйте снова.")
        except ValueError:
            print(f"Ввод должен быть числом [1-{max_number}]. Попробуйте снова.")


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
    },
    "Лолита": {
        "автор": "Владимир Набоков",
        "год_издания": 1999,
        "наличие": "None"
    }
}
#  Некоторые функции будут требовать от пользователя ввода значений переменных title, author, year.
#  Пока это не реализовано, эти значения заданы заранее:
title = "Война и мир"
author = "Лев Толстой"
year = 1980
main_menu()