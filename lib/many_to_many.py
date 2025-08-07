# Author class represents a writer who can sign contracts for books
class Author:
    # Class variable to keep track of all author instances
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)  # Add new author to the list of all authors

    # Return all contracts that belong to this author
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    # Return all books that the author has contracts for
    def books(self):
        # Use set to avoid duplicates, then convert to list
        return list({contract.book for contract in self.contracts()})

    # Create a new contract between this author and a book
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    # Return total royalties this author has earned from all contracts
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


# Book class represents a book that can have contracts with multiple authors
class Book:
    # Class variable to keep track of all book instances
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)  # Add new book to the list of all books

    # Return all contracts that include this book
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    # Return all authors who have contracts for this book
    def authors(self):
        return list({contract.author for contract in self.contracts()})


# Contract class links authors and books and stores contract details
class Contract:
    # Class variable to keep track of all contract instances
    all = []

    def __init__(self, author, book, date, royalties):
        # Type checking to ensure valid input
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        # Assign attributes
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Add this contract to the list of all contracts
        Contract.all.append(self)

    # Class method to return all contracts signed on a specific date
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
