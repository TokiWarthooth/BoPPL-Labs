# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Date: 07.09.2025

# Констатнта (входной json)
LIBRARY = [
    {"name": "Программирование на языке Python.", "price": 469, "pages": 389},
    # {"name": 'Сказка "Колобок".', "price": 99, "pages": 15},
    # {"name": "Программирование на Symfony PHP 8.4.", "price": 849, "pages": 568},
    # {
    #     "name": "Говори красиво и уверенно. Постановка голоса и речи.",
    #     "price": -249,
    #     "pages": 189,
    # },
]


class Book:
    def __init__(self, name, price, pages):
        self.name = name
        self.price = price
        self.pages = pages

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def pages(self):
        return self.__pages

    @name.setter
    def name(self, value):
        if value == "":
            raise BookPropertyException
        self.__name = value

    @price.setter
    def price(self, value):
        if value <= 0:
            raise BookPropertyException
        self.__price = value

    @pages.setter
    def pages(self, value):
        if value <= 0:
            raise BookPropertyException
        self.__pages = value

    # Переменные и функции в snake_case
    def page_cost(self):
        return round(self.price / self.pages, 2)

    def to_dict(self):
        return {"name": self.__name, "price": self.__price, "pages": self.__pages}

    def __str__(self):
        return f"Название: {self.__name} \t Цена: {self.__price} руб. \t Страницы: {self.__pages} \t Цена одной страницы: {self.page_cost()} руб."


# Класс в CamelCase
class LibraryManager:
    def __init__(self, library_data):
        self.books = []
        for book_data in library_data:
            book = Book(book_data["name"], book_data["price"], book_data["pages"])
            self.books.append(book)

    def price_changer(self):
        for book in self.books:
            if book.name.startswith("Программирование"):
                book.price *= 2

    def print_books(self):
        for book in self.books:
            print(book)


# library_manager = LibraryManager(LIBRARY)
# print("Исходные цены:")
# library_manager.print_books()

# print("\nЦены после изменения:")
# library_manager.price_changer()
# library_manager.print_books()


import json

class BookPropertyException(Exception):
    """Custom exception raised whenever an incorrect value is assigned to the properties of a Book object."""

    pass


class CLILibraryManager:
    CLI_MANUAL = """
--- CLI library manual ---

A little guide on how to use this CLI tool

Commands:
exit - terminate the program. You will be asked to save any unsaved changes.
help - print this CLI library manual (you are reading it right now).
print_books - prints a chart of all library books.
load_books - load books from a specified .json file into the library. Unsaved changes will be lost if you proceed without saving.
save_books - save the current library data to a specified file path. The file does not need to exist, but the path must be valid.
add_book - add a new book to the library. You will be prompted to enter the book's name, price, and number of pages.
delete_book - delete an existing book from the library by entering its name. You will be prompted to confirm the deletion.

Notes:
- any other command will not be recognised and you'll get this message:
"Undefined command. Try something else or open the manual ("help" command)"

- keep an eye on what is being outputed: sometimes you'll have to input some additional data
to finish the execution of command.

--------------------------
"""

    def __init__(self, library_data=[], prompt="command: "):
        self.library_manager = LibraryManager(library_data)
        self.changes_saved = True
        self.running = False
        self.prompt = prompt
        self.methods = {
            "help": self.__help,
            "print_books": self.__print_books,
            "load_books": self.__load_books,
            "add_book": self.__add_book,
            "delete_book": self.__delete_book,
            "save_books": self.__save_books,
            "exit": self.__exit,
        }

    def run(self):
        self.running = True
        print('Welcome to CLI library manager! Type "help" to get started')
        while self.running:
            self[input(self.prompt).split(" ")[0]]()

        print("The CLI library manager is being terminated. Goodbye, user")

    # -------------------------
    # --- cli functionality ---
    # -------------------------

    def __help(self):
        print(self.CLI_MANUAL)

    def __print_books(self):
        if len(self.library_manager.books) == 0:
            print("Currently your library is empty. Total: 0 books")
            return
        self.library_manager.print_books()
        print(f"\nTotal: {len(self.library_manager.books)} books")

    def __load_books(self):
        if not self.changes_saved:
            self.__binary_choise(
                "Your unsaved changes will be irreversibly overwritten by loaded data. Proceed anyway?",
                {"y": self.__save_books(), "n": lambda: 0},
            )
        print("Input path to your .json library file:")
        library_file_path = input("path: ")

        try:
            with open(library_file_path, "r", encoding="utf-8") as lib:
                loaded_library = json.load(lib)
                self.library_manager = LibraryManager(loaded_library)
                print("Data loaded successfully!")
                self.changes_saved = True
        except FileNotFoundError:
            print("Incorrect library file path")
        except BookPropertyException:
            print(
                "Some books in this library file posses incorrect data (f.e., { ..., pages: -1) }"
            )
        except:
            print("Incorrect library data format")

    def __save_books(self):
        print(
            "Input path for a file to save your library at.\nNote: existance of the file itself is not nessesary, but path to it Must exist"
        )
        file_path = input("path: ")
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                jsonified_books = list(
                    map(lambda book: book.to_dict(), self.library_manager.books)
                )
                json.dump(jsonified_books, file, ensure_ascii=False, indent=4)
                print("Library data saved successfully!")
        except FileNotFoundError:
            print("Incorrect path to save file to")
        except Exception as e:
            print(e)

    def __add_book(self):
        name = self.__filtered_input(
            lambda name: name != "", "Input non-empty book name", prompt="book name: "
        )
        price = int(
            self.__filtered_input(
                lambda price: price.isdigit() and int(price) > 0,
                "Input a positive integer, that will represent price",
                prompt="price: ",
            )
        )
        pages = int(
            self.__filtered_input(
                lambda pages: pages.isdigit() and int(pages) > 0,
                "Input a positive integer, that will represent amount of pages",
                prompt="pages: ",
            )
        )

        new_book = Book(name, price, pages)

        def confirm_adding():
            self.library_manager.books.append(new_book)
            self.changes_saved = False
            print('New book was added to library!')

        self.__binary_choise(
            f"Your new book:\n{str(new_book)}\nConfirm adding it?",
            {"y": confirm_adding, "n": lambda: 0},
        )

    def __delete_book(self):
        book_names = list(map(lambda book: book.name, self.library_manager.books))
        deleting_book_name = self.__filtered_input(lambda name: name in book_names, "Input name of book you want to delete. Input empty string to interrupt deletion", 'delete: ')
        if not deleting_book_name:
            return
        for index, book in enumerate(self.library_manager.books):
            if book.name == deleting_book_name:
                self.library_manager.books.pop(index)
        self.changes_saved = False

    def __exit(self):
        if not self.changes_saved:
            self.__binary_choise(
                "Your unsaved changes will be irreversibly lost. Do you want to save changes you made?",
                {"y": self.__save_books, "n": lambda: 0},
            )

        self.__binary_choise(
            "Are you sure you want to quit?", {"y": self.__terminate, "n": lambda: 0}
        )

    # -----------------------
    # --- utility methods ---
    # -----------------------

    def __terminate(self):
        self.running = False

    def __filtered_input(self, filter_function, message, prompt="your input:"):
        while True:
            print(message)
            user_input = input(prompt)
            if filter_function(user_input):
                return user_input

    def __binary_choise(self, question, callbacks):
        answered = False
        while not answered:
            print(f"{question} - y / n")
            user_input = input().lower()
            if user_input in ["y", "n"]:
                callbacks[user_input]()
                answered = True

    def __handle_command_error(self):
        print(
            'Undefined command. Try something else or open the manual ("help" command)'
        )

    def __getitem__(self, key):
        try:
            return self.methods[key]
        except:
            return self.__handle_command_error


print("\n\n")
CLILibraryManager().run()
# CLILibraryManager(library_manager=LibraryManager(LIBRARY)).run()
