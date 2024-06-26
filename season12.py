# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no # public attributes
#         self.__acc_pass = acc_pass # private attributes

#     def reset_pass(self):
#         print(self.__acc_pass) 
#         #we can't access private attributes or methpods
#         #directly so we take a another method to pass these value and execute it.

# acc1 = Account("12345", "abcde")
# print(acc1.acc_no)
# print(acc1.reset_pass())



# class Person:
#     __name = "rohit" # private attributes

#     def __hello(self): # private method
#         print("hello person!") 

#     def welcome(self): # a method to pass our private method
#         self.__hello()

# p1 = Person()
# print(p1.welcome()) 

# hello person 
# none




# example of single inheritance 
# class Car:
#     @staticmethod # decorator
#     def start():
#         print("car strated..")

#     @staticmethod # decorator
#     def stop():
#         print("car stopped..")
    
# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Legender")
# print(car1.stop())
# print(car2.start())


# example of multilevel inheritance
# class Car:
#     # @staticmethod # decorator
#     # def start():
#     #     print("car strated..")

#     @staticmethod # decorator
#     def stop():
#         print("car stopped..")
    
# class ToyotaCar(Car):
#     @staticmethod # decorator
#     def start():
#         print("car strated..")

#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type = type

# car1 = Fortuner("disel")
# car1.start()

# example of multiple inheritance
# class A:
#     varA = "welcome to class A"
# class B:
#     varB = "welcome to class B"
# class C(A,B):
#     varC = "welcome to class C"

# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)





# example of polymorphism


class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def add(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)


num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()








# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i +", self.img,"j")

#     def __add__(self,num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

# num1 = Complex(1,3)
# num1.showNumber()

# num2 = Complex(4,6)
# num2.showNumber()

# num3 = num1 + num2
# num3.showNumber()