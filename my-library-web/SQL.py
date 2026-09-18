from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# 4. Define the Book Model
class Book(db.Model):
    __tablename__ = "books"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

# 5. Create the database and table within the app context
# with app.app_context():
#     db.create_all()

#     # 6. Create a new book record
#     new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
# #     db.session.commit()     
# with app.app_context():
#     result = db.session.execute(db.select(Book))
#     all_books = result.scalars().all()
#     for book in all_books:
#         print(book.title, book.author, book.rating)

# with app.app_context():
#     # 1. Add a second unique book
#     new_book = Book(id=2, title="Atomic Habits", author="James Clear", rating=9.1)
#     db.session.add(new_book)
#     db.session.commit()

#     # 2. Query and print all books in the database
#     result = db.session.execute(db.select(Book))
#     all_books = result.scalars().all()
    
#     print("--- Current Library ---")
#     for book in all_books:
#         print(f"ID: {book.id} | Title: {book.title} | Author: {book.author} | Rating: {book.rating}")

# with app.app_context():
#     # 1. Find the specific book by its title
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Atomic Habits")).scalar()
    
#     if book_to_update:
#         # 2. Change the rating
#         book_to_update.rating = 9.8
        
#         # 3. Commit the changes
#         db.session.commit()
#         print(f"Updated '{book_to_update.title}' rating to {book_to_update.rating}!")
#     else:
#         print("Book not found.")

with app.app_context():
    # 1. Find the book you want to delete
    book_to_delete = db.session.execute(db.select(Book).where(Book.title == "Atomic Habits")).scalar()
    
    if book_to_delete:
        # 2. Delete it from the session
        db.session.delete(book_to_delete)
        
        # 3. Commit the changes
        db.session.commit()
        print(f"Deleted '{book_to_delete.title}' from the database.")