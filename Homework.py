# 1- write a program to input 2 numbers & print their sum.

# first = int(input("enter first : "))
# second = int(input("enter second : "))

# print("sum =", first + second)

# 2- Write a program to input side of a square & print its area.

# side = int(input("enter square side : "))
# print("area =", side * side)

# 3- write a program to input 2 floating point numbers & print their average.

# a = float(input("enter first : "))
# b = float(input("enter second : "))

# print("average =", (a+b)/2)

# 4- write a program to input 2 int numbers a & b, print True if a is greater then or equal to . if not print false.

# a = int(input("enter first : "))
# b = int(input("enter second : "))

# print(a >= b) 

# 5- write a program to input users first name & print its length.

# name = input("enter your name : ")
# print("length of your name: ", len(name)) # 6 

# 6- write a program to count the occerrence of '$' in a string.

# str = "hi i am the $ symbol $99.0"
# print(str.count("$")) #2

# for loop task:- 
# 1. print the element of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]

# nums = [1,4,9,16,25,36,49,64,81,100]

# for val in nums:
#     print(val)

# 2. search for a number x in this tuple using loop.
#    (1,4,9,16,25,36,49,64,81,100)

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 49
# idx = 0
# for ele in nums:
#     if(ele == x):
#         print("number found at idx", idx)
#     idx = idx + 1



# print numbers from 1 to 100
# for i in range(1, 101):
#     print(i)

# print numbers from 100 to 1
# for i in range(100, 0, -1):
#     print(i)

# print the multiplication table of a number n
# n = int(input("enter a number: "))
# for i in range(1,11):
#     print(n * i)

# python function
# write a function to print the length of a list(list is the parameter)

# cities = ["delhi", "BBSR", "Cuttack", "Pune", "chennai", "mumbai"]
# heros = ["fghj","dfghj","fghjk","dfghj"]
# def print_len(list):
#     print(len(list))

# print_len(heros)

# write a function to print the element of a list in a single line(list is the paraneter)

# cities = ["delhi", "BBSR", "Cuttack", "Pune", "chennai", "mumbai"]

# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end=" ")
# print_list(cities)

# write a function to find the factorial of n (n is the parameter)

# def cal_func(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i 
#         print(fact)
# cal_func(5)
    
# Initially, fact = 1.
# Iteration 1: i = 1
# fact = 1 * 1 = 1
# Print: 1

# Iteration 2: i = 2
# fact = 1 * 2 = 2
# Print: 2

# Iteration 3: i = 3
# fact = 2 * 3 = 6
# Print: 6

# Iteration 4: i = 4
# fact = 6 * 4 = 24
# Print: 24

# Iteration 5: i = 5
# fact = 24 * 5 = 120
# Print: 120
# write a function to convert USD to INR.

# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD = ", inr_val, "INR")

# converter(100000)

# create Account class with 2 attributes - balance & account no. & create methods for debit, 
# credit & printing the total balance.


class Account:
    def __init__(self, bal, acc):
        self.balance = bal 
        self.account = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(450000)