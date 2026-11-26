import mysql.connector

class library_management_system:
    def __init__(self):
        self.connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='library_management'
        )

        self.c=self.connection.cursor()

    def Add_book(self):
        try:
            title=input("Enter the title of the book : ")
            author=input("Enter the author of the book : ")
            category=input("Enter the category of the book : ")
            total_copies=int(input("Enter the total copies of the book : "))
            available_copies=int(input("Enter the available_copies of the book : "))

            if available_copies>total_copies:
                print("Error:available copies greater than total copies ")

            elif available_copies<0 or total_copies<0:
                print("Error:available_copies or total copies can't be negative")

            else:

                query="insert into books(title,author,category,total_copies,available_copies) values (%s,%s,%s,%s,%s)"
                data=(title,author,category,total_copies,available_copies)
                self.c.execute(query,data)
                self.connection.commit()
                print("new book added")
        except:
            print("Some value or syntax error occured: couldn't add book")

    def ViewAvailableBooks(self):
        try:
            query="select * from books where available_copies>0"
            self.c.execute(query)
            result=self.c.fetchall()
            if result:
                for row in result:
                    print(row)

            else:
                print("no available books")

        except:
            print("Some value or syntax error occured")

    def SearchBook(self):
        try:
            book_id=int(input("enter the id of the book : "))
            query="Select * from books where book_id=%s"
            data=(book_id,)
            self.c.execute(query,data)
            result=self.c.fetchall()
            if result:
                for row in result:
                    print(row)
            else:
                print("NO book found")

        except:
            print("Some value or syntax error occured")


    def UpdateAvailableCopies(self):
        try:
            id=int(input("Enter the id of the book : "))
            query="select total_copies from books where book_id=%s"
            d=(id,)
            self.c.execute(query,d)
            total_copies=self.c.fetchone()
            print("total copies:",total_copies[0])
            available_copies=int(input("Enter available copies : "))
            if available_copies>total_copies[0] or available_copies<0:
                print("Available copies can't be negative or more than the total copies.")

            else:
                query="Update books set available_copies=%s where book_id=%s"
                data=(available_copies,id)
                self.c.execute(query,data)
                self.connection.commit()
                print("Updated Successfully")

        except:
            print("Some value or syntax error occured")

    def DeleteBook(self):
        try:
            id=int(input("enter the id of the book : "))
            query="delete from books where book_id=%s"
            data=(id,)
            self.c.execute(query,data)
            self.connection.commit()
            if self.c.rowcount>0:
                print("deleted succesfully")
            else:
                print("no record found")

        except:
            print("Some value or syntax error occured")


    def LibrarySummary(self):
        try:
            query="select count(title),sum(available_copies),avg(total_copies) from books"
            self.c.execute(query)
            result=self.c.fetchone()
            if result:
                print("Total number of books: ",result[0])
                print("Sum of all available books: ",result[1])
                print("Average of totla copies: ",result[2])
            # if result:
            #     for row in result:
            #         print(row)
            else:
                print("no books in the library")
        except:
            print("Some value or syntax error occured")


book=library_management_system()
while True:
    print("Menu:")
    print("1. Add Book\n2. View Available Books \n3. Search Book\n4. Update Available Copies\n5. Delete Book\n6. Library Summary\n7. Exit\n")
    choice=int(input("Enter your choice:"))

    if choice==1:
        book.Add_book()
    elif choice==2:
        book.ViewAvailableBooks()
    elif choice==3:
        book.SearchBook()
    elif choice==4:
        book.UpdateAvailableCopies()
    elif choice==5:
        book.DeleteBook()
    elif choice==6:
        book.LibrarySummary()
    elif choice==7:
        print("Thank you : EXIT")
        break



