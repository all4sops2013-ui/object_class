#object oriented programming is more safer because there are no other programms that can access that program without the users permission
#it is more flexible. it is nore object centric

class Student:

    # constructor is used to create and initiate an object in our program
    def __init__(self,id,marks):
        self.id = id
        self.marks = marks

    def display(self):
        print("the marks of student with id", self.id, 'is', self.marks)
    
    # destructor is used to delete an object in our program
    def __init__(self):
        print('object deleted......OOPS we lost it !!!')

ob1 = Student('id11',28)
ob1.display()
#calling destuctor
del ob1
#ob1.display()


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



Write a program to create a class with the named employee and create a 
constructor and destructor. Then, write a function to create an
 object for that class and delete the object. Make sure you call the function to get everything implemented!

#task 2

class employee_1:

    def __init__(self):
        print('object created')

    def __del__(self):
        print('Delete the message')
    
def create_object():
    ob1 = employee_1()
    del ob1
create_object()