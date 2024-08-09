#Dictionary of books.
library = {
    
    "1": {
        "title": "Hard Times", 
        "author": "Charles Dickens", 
        "quantity": 7
    },
        
    "2": {
        "title": "Emma", 
        "author": "Jane Austen", 
        "quantity": 4
    },
        
    "3": {
        "title": "Jane Eyre", 
        "author": "Charlotte Bronte", 
        "quantity": 12
    },
    
    "4": {
        "title": "Kim", 
        "author": "Rudyard Kipling", 
        "quantity": 3}
    }

#Add a book
def add_book(new_book, add_title, add_author, add_quantity):
    new_book = input("Please enter the id of the book you'd like to add: ") #Save id to a variable
if  new_book in library.keys(): #search for the id variable in keys
    add_quantity = input("Enter the quantity of the book you're adding: ") #Prompt for quantity
    new_quantity = int(library[new_book]['quantity']) + int(add_quantity) #Add the added amount to quantity
    print(f"This book is already in our system. We have added a copy.There are now {new_quantity} copies.") #Message to user
else: 
    print("This book is not in our system yet. Please provide some information so we can add it.") #Message to user
    add_title = input("Enter the title of the book you're adding: ") #Prompts for info
    add_author = input("Enter the author of the book you're adding: ")
    add_quantity = input("Enter the quantity of the book you're adding: ")
    library.append(add_book) #add new book to library dictionary

#Deleting A Book
def delete_book(book_id):
   remove_book = input("Please enter the id of the book you'd like to remove: ") #Save id to a variable
if remove_book in library.keys(): #Search for book
    library.remove(remove_book) #Remove book
    print("This book has been removed") #Message to user
else:
    print("This book is not in our system") #Message to user

#Search For A Book
def search_book(keyword):
   search_word = input("Please enter a book or author for the book you're looking for: ") #Assign input to variable
if search_word in library.values(): #Check for variable in values
    print(f"The ID of the book you are looking for is {library.keys}." ) #Message to user
else:
    print("I'm sorry. We could not find this book or author in our system.") #Message to user

#Display Entire Inventory, Sorted
def display_inventory():
       sort_list = list(library.items()) #Turn dictionary into list so it can be sorted
       sort_books = sort_list.sort #Sort the list
       print(sort_books) #Print the sorted list





#List of Borrowed Books
borrowed_books = ("Secret Garden": {"5", "Kelly Taylor", "03/07/24"}, "Harry Potter": {"6", "Monica Morgan", "08/23/24"}, 
                  "Lord of the Rings": {"7", "Jake Murray", "02/01/24"}) #List of books with dictionaries for book id, borrower name, and borrow date

#Borrow A Book
def borrow_book(book_id, borrower_name, borrow_date): 
    book_id = input("Please enter the id of the book that was borrowed: ") #Assign input to variables
    borrower_name = input("What is the borrower's name: ")
    borrower_date = input("When is the book due?: ")
if book_id in library.values(): #Check for book availability
    borrowed_books.append(book_id, borrower_name, borrow_date) #Add book and borrower info to the borrowed books list
    int(library[new_book]['quantity']) - 1 #subtract the book from quantity available
    print("This book has been checked out.") #Message about book availability
else:
    print("This book is not available.") #Message about book availability


#Return A Book
def return_book(book_id):
    book_id = input("Enter the id of the book being returned: ") #Assign input to variable
if book_id in borrowed_books:
    borrowed_books.remove(book_id) #Remove book from borrowed books list
    int(library[new_book]['quantity']) + 1 #Update quantity in library
    print("This book has been returned.") #Message about book
else:
    print("This book is not in our system.") #Message about book