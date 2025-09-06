# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Date: 07.09.2025

library = [
    {
        'name': 'Программирование на языке Python.',
        'price': 469,
        'pages': 389
    },
    {
        'name': 'Сказка "Колобок".',
        'price': 99,
        'pages': 15
    },
    {
        'name': 'Программирование на Symfony PHP 8.4.',
        'price': 849,
        'pages': 568
    },
    {
        'name': 'Говори красиво и уверенно. Постановка голоса и речи.',
        'price': 249,
        'pages': 189
    }
]

class Book:
    def __init__(self, name, price, pages):
        self.__name = name
        self.__price = price
        self.__pages = pages

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def pages(self):
        return self.__pages

    def pageCost(self):
        return round(self.price / self.pages, 2)

    def __str__(self):
        return f"Название: {self.__name} \t Цена: {self.__price} руб. \t Страницы: {self.__pages} \t Цена одной страницы: {self.pageCost()} руб."


class LibraryManager:
    def __init__(self, libraryData):
        self.books = []
        for bookData in libraryData:
            book = Book(bookData['name'], bookData['price'], bookData['pages'])
            self.books.append(book)

    def priceChanger(self):
        for book in self.books:
            if book.name.startswith('Программирование'):
                book.price *= 2

    def printBooks(self):
        for book in self.books:
            print(book)


libraryManager = LibraryManager(library)
print("Исходные цены:")
libraryManager.printBooks()

print("\nЦены после изменения:")
libraryManager.priceChanger()
libraryManager.printBooks()