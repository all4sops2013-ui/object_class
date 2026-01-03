#object oriented programming is more safer because there are no other programms that can access that program without the users permission
#it is more flexible. it is nore object centric

class Student:
    def __init__(self,id,marks):
        self.id = id
        self.marks = marks

    def display(self):
        print("the marks of student with id", self.id, 'is', self.marks)
    
ob1 = Student('id11',28)
ob1.display()

#defining behaviour mean what it does
#instance of class is same as object 




#task 1

class IOString:
    def __init__(self):
        self.str1 = ""

    def take_input(self):
        self.str1 = input("enter a string: ")

    def display_uppercase(self):
        print(self.str1.upper())

ob1 = IOString()
ob1.display_uppercase()
ob1.take input()