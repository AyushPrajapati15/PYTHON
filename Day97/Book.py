class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.bestseller = False

    def Bestseller(self):
        if self.year > 2010:
            self.bestseller = True
        else:
            self.bestseller = False

    def display_details(self):
        print("Book Details:")
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print("Bestseller:", "Yes" if self.bestseller else "No")
        print()


book1 = Book("The Alchemist", "Paulo Coelho", 1988)
book2 = Book("The Richest Man in Babylon", "George Samuel Clason", 2011)
book3 = Book("Rich Dad, Poor Dad", "Robert Kiyosaki", 2014)


book1.Bestseller()
book2.Bestseller()
book3.Bestseller()


book1.display_details()
book2.display_details()
book3.display_details()
