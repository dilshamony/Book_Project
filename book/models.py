from django.db import models

# Create your models here.
#1
class Book(models.Model):
    book_name=models.CharField(max_length=150,unique=True) #unique=true is to avoid duplicate
    auther = models.CharField(max_length=150)
    price = models.IntegerField()
    pages = models.IntegerField()

    def __str__(self):
        return self.book_name



# ORM QUERIES

#from book.models import Book


# Creating a book==>mysql queries
# insert into Book values("randamoozham", "mt",280,250)

#But here sql queries are not using bt instead orm queries are using
# Orm queries for creating a book
#book=Book(book_name="randamoozham", auther="mt",price=280,pages=250)
#book.save()
#book1=Book(book_name="halfgirlfriend", author="cb",price=290,poages=250)
#book1.save()



#Fetching all queries==>mysql query
#select * from Book

#Orm query for fetching all queries
#books=Book.objects.all()
#books



#Orm query to fetch a particular object
#book=Book.objects.get(id=1)
#print (book.book_name)
#print(book.price)


# To take all books and details
#for book in books: ===>  after enter press, press tab also
#    print (book.book_name)
#    print(book.price)
#    print(book.pages)
#    print(book.auther)
#press enter ==>backspace==>enter




#To update the value of price
#book=Book.objects.get(id=2)
#print(book.price)
#book.price=350
# book.save()
#book.price

#select all books whose price<300
#select * from books where price<300=====>mysql query
#Orm Query
# books=Book.objects.filter(price__lte=300)

#select all books whose price>300
# books
# books=Book.objects.filter(price__gte=300)
# books



# To check id numbers
# books=Book.objects.all()
# ids=[book.id for book in books]
# ids
#====>[1, 2, 3]


# To delete a book
# book=Book.objects.get(id=1)
# book.delete()
#====>(1, {'book.Book': 1})







#work to do

#create employee model
#employee name,desig,salary
#create 4 employee objects
#fetch all employee objacts
#print their ename
#fetch a particular employee
#update an employee
#update an employee salary whose id=3