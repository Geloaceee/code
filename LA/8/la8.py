#LA8
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
libro = Book("Stephen kings" , "IT")    
print(f"Title: {libro.author} Author: {libro.title}")      
del libro.author
#print(f"Title: {libro.author} Author: {libro.title}")  
libro2 = Book("J.K. Rowling", "Harry Potter")
print(f"Title: {libro2.author} Author: {libro2.title}")     
