class Book:
    def __init__(self, author, pagenum, year, name):
        self.set_author(author)
        self.set_pagenum(pagenum) 
        self.set_year(year)
        self.__name = name
    
    def set_author(self, author):
        if all(char.isanum() or char == '.' for char in author) and ' ' in author:
            self.__author = author 
        else:
            print ("Ошибка в записи имени автора")

    def get_author(self):
        return self.__author
    
    def set_pagenum(self, pagenum):
        if pagenum < 5 or pagenum > 2000:
            print("Количество страниц не должно быть меньше 5 или больше 2000")
            self.__pagenum = 5
        else:
            self.__pagenum = pagenum

    def get_pagenum(self):
        return self.__pagenum

    def set_year(self, year):
        if year > 2025:
            print ("Год выпуска не может быть больше текущего")
            self.__year = year

    def get_year(self):
        return self.__year

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def display(self):
        print(f"Автор книги: {self.__author}, количество страниц: {self.__pagenum}, год выпуска: {self.__year}, название: {self.__name}")

NewBook = Book("А.С. Пушкин", 50, 1833, "Золотая рыбка")
NewBook.display()
SecondBook = Book("М.Ю. Лермонтов", 5, 1837, "Бородино")
SecondBook.display()