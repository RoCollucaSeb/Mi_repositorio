# class myclass:#Create a class
#     x=5
# p1=myclass()#Creat an object named p1, and print the calue of x

# print(p1.x)
# #This isn't useful in real life applications

# class person:
#     def __init__(self, name, age):#Functio to assign values to objevt properties
#         self.name=name
#         self.age=age

# p1 = person("Lucas",24)

# print(p1.name)
# print(p1.age)

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):#controls what should be returned when the class object is represented as a string

#         return f"{self.name}({self.age})"

# p1= person("Lucas",24)

# print(p1.name)
# print(p1.age)
# print(p1)

#Object methods
#Methods in objects are functions that belong the object
class persona:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def myfunc(self):
        print("hello my name is " + self.name)
    
p1=persona("lucas",24)
p1.myfunc()  
p1.age =25#modify object properties
print(p1.age)
del p1.age#Delete object properties
del p1#Delete object
class aux:
    pass #If you for some reason have a calss definition with no content, put in the pass statement toa void getting an error

