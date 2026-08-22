# Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook


class Book:
    def __init__(self, bid=0, bname="", price=0.0, author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def __del__(self):
        print("Book destructor called.")

    def ShowBook(self):
        print("\n--- Book Details ---")
        print("Book ID   :", self.bid)
        print("Book Name :", self.bname)
        print("Price     :", self.price)
        print("Author    :", self.author)



# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

# 2. Product Class

class Product:
    def __init__(self, pid=0, pname="", price=0.0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print("Product destructor called.")

    def ShowBook(self):
        print("\n--- Product Details ---")
        print("Product ID   :", self.pid)
        print("Product Name :", self.pname)
        print("Price        :", self.price)
        print("Quantity     :", self.quantity)


# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

# 3. Shirt Class

class Shirt:
    def __init__(self, sid=0, sname="", type="", price=0.0, size=""):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print("Shirt destructor called.")

    def ShowBook(self):
        print("\n--- Shirt Details ---")
        print("Shirt ID   :", self.sid)
        print("Shirt Name :", self.sname)
        print("Type       :", self.type)
        print("Price      :", self.price)
        print("Size       :", self.size)


# Main Program

# Book objects
b1 = Book()
b2 = Book(101, "C++ Programming", 450.50, "Bjarne Stroustrup")

b1.ShowBook()
b2.ShowBook()


# Product objects
p1 = Product()
p2 = Product(201, "Laptop", 55000, 5)

p1.ShowBook()
p2.ShowBook()


# Shirt objects
s1 = Shirt()
s2 = Shirt(301, "Formal Shirt", "Formal", 1200, "Large")

s1.ShowBook()
s2.ShowBook()