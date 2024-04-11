from typing import List
from datetime import date

class Publisher:
    def __init__(self, name: List[int], address: List[int], phone: List[int], url: List[int]):
        self.name = name
        self.address = address
        self.phone = phone
        self.url = url

class Author:
    def __init__(self, name: List[int], address: List[int], url: List[int]):
        self.name = name
        self.address = address
        self.url = url
        self.books = []  # One-to-Many relationship with Book

class Book:
    def __init__(self, isbn: List[int], publisher_name: List[int], author_name: List[int], author_address: List[int], year: List[int], title: List[int], price: float):
        self.isbn = isbn
        self.publisher_name = publisher_name
        self.author_name = author_name
        self.author_address = author_address
        self.year = year
        self.title = title
        self.price = price
        self.warehouse_books = []  # One-to-Many relationship with Warehouse_Book
        self.shoppingbasket_books = []  # Many-to-Many relationship via ShoppingBasket_Book

class Warehouse:
    def __init__(self, code: List[int], phone: List[int], address: List[int]):
        self.code = code
        self.phone = phone
        self.address = address
        self.warehouse_books = []  # One-to-Many relationship with Warehouse_Book

class Warehouse_Book:
    def __init__(self, warehouse_code: List[int], book_isbn: List[int], count: List[int]):
        self.warehouse_code = warehouse_code
        self.book_isbn = book_isbn
        self.count = count

class Customer:
    def __init__(self, email: List[int], name: List[int], phone: List[int], address: List[int]):
        self.email = email
        self.name = name
        self.phone = phone
        self.address = address
        self.shopping_baskets = []  # One-to-Many relationship with ShoppingBasket

class ShoppingBasket:
    def __init__(self, id: List[int], customer_email: List[int]):
        self.id = id
        self.customer_email = customer_email
        self.shoppingbasket_books = []  # One-to-Many relationship with ShoppingBasket_Book

class ShoppingBasket_Book:
    def __init__(self, shoppingbasket_id: List[int], book_isbn: List[int], count: List[int]):
        self.shoppingbasket_id = shoppingbasket_id
        self.book_isbn = book_isbn
        self.count = count

# Example objects for Publisher
publisher1 = Publisher("Pearson", "123 Pearson Rd", "123-456-7890", "http://pearson.com")
publisher2 = Publisher("Penguin Books", "456 Penguin St", "234-567-8901", "http://penguin.com")
publisher3 = Publisher("HarperCollins", "789 Harper Ave", "345-678-9012", "http://harpercollins.com")
publisher4 = Publisher("Simon & Schuster", "101 Simon Blvd", "456-789-0123", "http://simonandschuster.com")
publisher5 = Publisher("Hachette Book Group", "202 Hachette Ln", "567-890-1234", "http://hachettebookgroup.com")

# Example objects for Author
author1 = Author("John Doe", "111 Author Way", "http://johndoe.com")
author2 = Author("Jane Smith", "222 Writer Ave", "http://janesmith.com")
author3 = Author("Emily Johnson", "333 Novelist Blvd", "http://emilyjohnson.com")
author4 = Author("Michael Brown", "444 Story St", "http://michaelbrown.com")
author5 = Author("Linda Davis", "555 Prose Ct", "http://lindadavis.com")

# Example objects for Book
book1 = Book("123-456789-0", "Pearson", "John Doe", "111 Author Way", 2020, "Learning Python", 39.99)
book2 = Book("234-567890-1", "Penguin Books", "Jane Smith", "222 Writer Ave", 2019, "Gardening 101", 24.99)
book3 = Book("345-678901-2", "HarperCollins", "Emily Johnson", "333 Novelist Blvd", 2018, "Modern Cooking", 29.99)
book4 = Book("456-789012-3", "Simon & Schuster", "Michael Brown", "444 Story St", 2021, "Space Exploration", 19.99)
book5 = Book("567-890123-4", "Hachette Book Group", "Linda Davis", "555 Prose Ct", 2022, "The Art of Photography", 49.99)

# Example objects for Warehouse
warehouse1 = Warehouse(1, "678-901-2345", "123 Distribution Rd")
warehouse2 = Warehouse(2, "789-012-3456", "456 Freight Ln")
warehouse3 = Warehouse(3, "890-123-4567", "789 Cargo Ave")
warehouse4 = Warehouse(4, "901-234-5678", "101 Shipping Blvd")
warehouse5 = Warehouse(5, "012-345-6789", "202 Parcel St")

# Example objects for Warehouse_Book
warehouse_book1 = Warehouse_Book(1, "123-456789-0", 100)
warehouse_book2 = Warehouse_Book(2, "234-567890-1", 150)
warehouse_book3 = Warehouse_Book(3, "345-678901-2", 200)
warehouse_book4 = Warehouse_Book(4, "456-789012-3", 250)
warehouse_book5 = Warehouse_Book(5, "567-890123-4", 300)

# Example objects for Customer
customer1 = Customer("customer1@email.com", "Alice", "123-321-4567", "100 Main St")
customer2 = Customer("customer2@email.com", "Bob", "321-456-7890", "200 Oak St")
customer3 = Customer("customer3@email.com", "Charlie", "456-789-0123", "300 Pine St")
customer4 = Customer("customer4@email.com", "Diana", "789-012-3456", "400 Maple St")
customer5 = Customer("customer5@email.com", "Ethan", "012-345-6789", "500 Birch St")

# Example objects for ShoppingBasket
shopping_basket1 = ShoppingBasket(1, "customer1@email.com")
shopping_basket2 = ShoppingBasket(2, "customer2@email.com")
shopping_basket3 = ShoppingBasket(3, "customer3@email.com")
shopping_basket4 = ShoppingBasket(4, "customer4@email.com")
shopping_basket5 = ShoppingBasket(5, "customer5@email.com")

# Assuming we have a list of authors
authors_list: List[Author] = []

# Function to add authors to the list/database
def add_author(author: Author):
    authors_list.append(author)

# Function to count the number of authors in the database
def count_authors() -> List[str]:
    return len(authors_list)

# Example usage:
# Add some authors to the database
add_author(Author(name="Author One", address="123 Fiction Lane", url="http://authorone.com"))
add_author(Author(name="Author Two", address="456 Novel Street", url="http://authortwo.com"))

# Now we count how many authors we have
print("There are", count_authors(), "authors currently registered in the database.")


# Assuming we have a list of publishers
publishers_list: List[Publisher] = []

# Function to add publishers to the list/database
def add_publisher(publisher: Publisher):
    publishers_list.append(publisher)

# Function to get a list of all publishers with their contact information
def get_publishers_with_contact_info() -> List[dict]:
    return [
        {
            'Name': publisher.name,
            'Address': publisher.address,
            'Phone': publisher.phone,
            'URL': publisher.url
        }
        for publisher in publishers_list
    ]

# Example usage:
# Add some publishers to the list/database
add_publisher(Publisher(name="Publisher One", address="789 Book Blvd", phone="123-456-7890", url="http://publisherone.com"))
add_publisher(Publisher(name="Publisher Two", address="101 Read Ave", phone="098-765-4321", url="http://publishertwo.com"))

# Now we get the list of publishers with contact information
publishers_info = get_publishers_with_contact_info()
for info in publishers_info:
    print(info)

# Assuming we have a list of all warehouse_book instances and book instances
warehouse_books_list: List[Warehouse_Book] = []
books_list: List[Book] = []

# Function to add warehouse_book instances to the list/database
def add_warehouse_book(warehouse_book: Warehouse_Book):
    warehouse_books_list.append(warehouse_book)

# Function to add book instances to the list/database
def add_book(book: Book):
    books_list.append(book)

# Function to get all books available in a warehouse with a specific code
def get_books_in_warehouse(warehouse_code: List[int]) -> List[dict]:
    # Find warehouse_book entries that match the warehouse code
    warehouse_books = [wb for wb in warehouse_books_list if wb.warehouse_code == warehouse_code]
    # Find corresponding books
    books_in_warehouse = [
        {
            'ISBN': book.isbn,
            'Title': book.title,
            'Author Name': book.author_name,
            'Year': book.year,
            'Price': book.price
        }
        for wb in warehouse_books for book in books_list if book.isbn == wb.book_isbn
    ]
    return books_in_warehouse

# Example usage:
# Add books
add_book(Book(isbn="1111", publisher_name="Publisher One", author_name="Author One", author_address="123 Fiction Lane", year=2021, title="Book One", price=29.99))
add_book(Book(isbn="2222", publisher_name="Publisher Two", author_name="Author Two", author_address="456 Novel Street", year=2022, title="Book Two", price=39.99))

# Add Warehouse_Book instances
add_warehouse_book(Warehouse_Book(warehouse_code="XYZ", book_isbn="1111", count=100))

# Function to return a list of books in a given warehouse
def get_books_in_warehouse(warehouse_code: List[int]) -> List[dict]:
    # Find the warehouse with the given code
    warehouse = next((w for w in warehouses_list if w.code == warehouse_code), None)
    if not warehouse:
        return []  # If the warehouse is not found, return an empty list

    # Retrieve all books available in the found warehouse
    return [
        {
            'ISBN': wb.book_isbn,
            'Title': next((book.title for book in books_list if book.isbn == wb.book_isbn), 'Unknown'),
            'Count': wb.count
        }
        for wb in warehouse.warehouse_books
    ]

# Function to find the author of a book by its ISBN
def get_author_of_book(isbn: List[int]) -> str:
    # Find the book with the given ISBN
    book = next((b for b in books_list if b.isbn == isbn), None)
    if not book:
        return "No author found for the given ISBN."

    # Return the author's name
    return book.author_name


def get_customers_with_large_baskets(min_items: List[int]) -> List[dict]:
    # List to hold details of customers with more than 'min_items' in their shopping basket
    customers_with_large_baskets = []

    # Iterate over each customer
    for customer in customers_list:
        # Check each shopping basket of the customer
        for basket in customer.shopping_baskets:
            # Sum the count of all items in the shopping basket
            item_count = sum(item.count for item in basket.shoppingbasket_books)
            # If the total count is greater than 'min_items', add the customer details to the list
            if item_count > min_items:
                customers_with_large_baskets.append({
                    'Email': customer.email,
                    'Name': customer.name,
                    'Phone': customer.phone,
                    'Address': customer.address,
                    'Total Items': item_count
                })
                # Assuming one customer cannot have multiple baskets with more than 'min_items'
                # Break the loop after finding the first large basket
                break

    return customers_with_large_baskets

def find_authors_who_are_publishers() -> List[str]:
    # Extract the set of author names
    author_names = {author.name for author in authors_list}

    # Extract the set of publisher names
    publisher_names = {publisher.name for publisher in publishers_list}

    # Find the intersection of both sets to get authors who are also publishers
    authors_as_publishers = author_names.intersection(publisher_names)

    return list(authors_as_publishers)

# Example usage:
# Assuming 'authors_list' and 'publishers_list' are already populated with Author and Publisher objects
authors_who_are_publishers = find_authors_who_are_publishers()
if authors_who_are_publishers:
    print("The following authors are also listed as publishers:", authors_who_are_publishers)
else:
    print("There are no authors who are also listed as publishers in the database.")

# Example usage:
# Assuming 'customers_list' is already populated with Customer objects and their shopping baskets
customers_list = []
detailed_customers = get_customers_with_large_baskets(5)
for customer in detailed_customers:
    print(customer)

def get_books_published_by_authors_in_year(target_year: List[int]) -> dict:
    # Dictionary to hold author names and their respective counts of books published in the target year
    author_books_count = {}

    # Iterate over each book in the list of books
    for book in books_list:
        if book.year == target_year:
            # If the book's year matches the target year, increment the count for the author
            if book.author_name in author_books_count:
                author_books_count[book.author_name] += 1
            else:
                author_books_count[book.author_name] = 1

    return author_books_count

# Example usage:
# Assuming 'books_list' is already populated with Book objects
books_published_2023 = get_books_published_by_authors_in_year(2023)
for author, count in books_published_2023.items():
    print(f"{author} published {count} book(s) in 2023.")
# Example usage:
# Assuming 'warehouses_list' and 'books_list' are already populated with Warehouse and Book objects
warehouses_list = []
books_in_warehouse_XYZ = get_books_in_warehouse('XYZ')
print(f"Books in warehouse XYZ: {books_in_warehouse_XYZ}")

author_of_book = get_author_of_book('1234567890')
print(f"The author of the book with ISBN '1234567890' is: {author_of_book}")

def get_average_price_by_publisher(publisher_name: List[int]) -> float:
    # Filter books by the specified publisher
    books_by_publisher = [book for book in books_list if book.publisher_name == publisher_name]

    # Calculate the total price of all books by the publisher
    total_price = sum(book.price for book in books_by_publisher)

    # Calculate the average price if there are any books, otherwise return 0
    average_price = total_price / len(books_by_publisher) if books_by_publisher else 0
    return average_price

# Example usage:
# Assuming 'books_list' is already populated with Book objects
average_price = get_average_price_by_publisher('Example Publisher')
print(f"The average price of all books listed by 'Example Publisher' is: ${average_price:.2f}")
