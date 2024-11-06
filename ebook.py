class Ebook:
    
    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    def get_title(self):
        # Returns the title of the ebook
        return self.__title

    def set_title(self, title):
        # Sets the title of the ebook
        self.__title = title

    def get_author(self):
        # Returns the author of the ebook
        return self.__author

    def set_author(self, author):
        # Sets the author of the ebook
        self.__author = author

    def get_price(self):
        # Returns the price of the ebook
        return self.__price

    def set_price(self, price):
        # Sets the price of the ebook
        self.__price = price

    def __str__(self):
        # Returns a string representation of the ebook
        return "Title: " + self.__title + ", Author: " + self.__author + ", Price: " + str(self.__price)

