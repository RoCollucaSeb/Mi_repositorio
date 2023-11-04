#Python Inheritance
#Inheritance allows us to define a class that inherits all the methods and properties from another class.

# class person:#Parent class
#     def __init__(self, fname,lname):
#         self.firstname = fname
#         self.lastname = lname
#     def printname(self):
#         print(self.firstname,self.lastname)
    
# # p=person("Lucas","Romero")
# # p.printname()

# # class student(person):#child class
# #     pass

# # s=student("Pepe","Peréz")
# # s.printname()

# #Add the __init__() function
# class student(person):
#     def __init__(self,fname,lname):
#     #add properties etc.

# #Note: The child's __init__() function overrides(anula) the inheritance of the parent's __init__() function.
# #To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

# class student(person):
#     def __init__(self,fname,lname):
#         person.__init__(self,fname,lname)
#         #We are ready to add functionality in the __init__() function

#Use the super() Function
#Python also has a super() function that will make the child calss inherit
#all the methods and properties from ist parent:

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
