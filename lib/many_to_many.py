class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

  
    def total_royalties(self):
        
        return sum([contract.royalties for contract in self.contracts()])

class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


    def create_contract(self, author, date, royalties):
        return Contract(author, self, date, royalties)


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

  
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string")
        self._date = value


    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Royalties must be an integer")
        self._royalties = value

    # 
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be of type Author")
        self._author = value

   
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be of type Book")
        self._book = value
        

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]