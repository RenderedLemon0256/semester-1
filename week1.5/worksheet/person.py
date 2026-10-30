# Worksheet 1.5: Person class

from datetime import date

def getInitals(name):
    """returns the initals of the person"""
    words = name.split(" ")
    initials = ""
    for word in words:
        initials += word[0].upper()
    return initials

class Person:
    """
    A Person, with a name and a date of birth.
    """
    name = "Bob"
    birth = date.today()
    initals = "BDB"
    def __init__(self, name, birth):
            if(type(name) != str):
                raise TypeError
            if(type(birth) != date):
                raise TypeError
    
            if (name == ""):
                raise ValueError
                raise ValueError

            self.name = name
            self.birth = birth
            self.initals = getInitals(name)

   
    def is_birthday(self):
         """returns whether it is the person's birthday today"""
         if self.birth.month == date.today().month and self.birth.day == date.today().day:
            return True
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
