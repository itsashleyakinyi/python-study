# 1.Create a class Animal with attributes species and sound.Add a method make_sound that prints: "The [species] goes [sound]!",Instantiate objects for different animals and call make_sound.

# 2.Create a class Book with attributes like title, author, and year.
# Add a method that returns a description of the book.
# Create an object of Book and print out the description.

# 3.Define a class BankAccount with attributes owner and balance (set balance to 0 by default).Add methods deposit and withdraw to modify the balance and a method get_balance to display the balance.
# Ensure that the withdraw method does not allow the balance to go negative.

#1
class Animal:
    def __init__(self,species,sound):
        self.species=species
        self.sound=sound
    def species_sound(self):
        return f"The {self.species} goes {self.sound}!"

solution_one=Animal("American Robin","chirp")
print(solution_one.species_sound())

#2
class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def description(self):
        return f"The book is titled {self.title}. The author is {self.author} , published in the year {self.year}"  
    
book_1=Book("Siku Njema","Ken Walibora",2000)
print(book_1.description())


#3

