# Вывод в консоль названия всех книг в библиотеке
def book_list_view(library):
    if not library:  # Проверка "пустоты" библиотеки
        print("Библиотека пуста.")
        return
    print("Список книг в библиотеке:")
    for book in library.keys():  #  По всем ключам-названиям книг
        print("\t", book)  #  Вывод каждого названия


def add_book(title, author, year):
    if title not in library:
        # Добавляем новую книгу
        library[title] = {
            "автор": author,
            "год_издания": year,
            "наличие": None
        }
        print(f"\nКнига '{title}' ({author}, {year}) успешно добавлена.")
    else:
        # Если книга с таким title уже есть, предлагаем обновить или оставить без изменений
        choice = ''
        while choice != 'да' and choice != 'нет':
            print(f"\nКнига '{title}' уже существует.")
            choice = input(f"Хотите обновить информацию о книге '{title}'? (да/нет): ").strip().lower()
            if choice == 'да':
                book_info = library[title]  #  получаеи словарь с информацией о книге с таким title
                # Обновляем словарь с информацией о книге
                book_info['автор'] = author
                book_info['год_издания'] = year
                library[title] = book_info  #  возвращаем/обновляем словарь в library
                print(f"Информация о книге '{title}' обновлена:")
                print(f"Книга '{title}' ({author}, {year})")
            elif choice == 'нет':
                print("Обновление отменено.")
            else:
                print("Ответ не принят. Пожалуста, в следующий раз введите или ДА, или НЕТ.")


library = {
    "Война и мир": {
        "автор": "Лев Толстой",
        "год_издания": 1869,
        "наличие": "в наличии"
    },
    "Мастера и Маргарита": {
        "автор": "Михаил Булгаков",
        "год_издания": 1967,
        "наличие": "выдана"
    }
}


book_list_view(library)
(title, author, year) = ("Война и мир", "Лев Толстой", 1980)
add_book(title, author, year)
(title, author, year) = ("Лолита", "Владимир Навбоков", 1999)
add_book(title, author, year)
print("\n", library)