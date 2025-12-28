#object orienting programming - is used to make of your program be more secured
#types of concepts - class and object
#class - set of rule that are defined to be used later in any other program to save time
#objects - are the different types of put into a class


class student:
    def _init _(self,id):# self is like a handle referring to where the data is being stored
        self.id = id
        self.name = name

    def display(self):
        print(self.id,self.name)

ob1 = Student('id1','Amanda')
ob1.display()
# class usually has data and a function


class student:
    age = 13
    print('Age is',age)
#ob1 = student()
a = 26
print(a)



#task2
class vehicle:
    def __init__(self,mileage,max_speed):
        self.mileage = mileage
        self.max_speed = max_speed

    def display(self):
        print(self.mileage,self.max_speed)

ob1 = vehicle('mileage','56')
ob1.display()
ob2 = vehicle('max_speed','102')
ob2.display()



#task3
class Parrot:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display():
        print(self.name,self.age)
ob1 = parrot('name','Amanda')
ob1.display()
ob2 = parrot('age',14)
ob2.display()