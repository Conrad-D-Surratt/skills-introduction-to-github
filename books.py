class Book:
    def __init__(self, title, genre):
        # Private attributes
        self.__title = title
        self.__genre = genre

    # Setters (Allows controlled updates)
    def set_title(self, title):
        if title.strip(): # validation
            self.__title = title

    def set_genre(self, genre):
        self.__genre = genre

    # Getters (Allows safe access to private data)
    def get_title(self):
        return self.__title

    def get_genre(self):
        return self.__genre

    # The display method
    def display_order(self, index):
        return f"{index}. 📖 Title: {self.__title} | Category: {self.__genre}"