# def sum(a, b, c): #parameter
#     sum = a + b + c 
#     print(sum)
#     return sum

# sum(10, 20, 40) # 30
# sum(3, 6, 4)
# sum(900, 1000, 40) # argument


# def cal_sum(a,b):
#     sum = a + b
#     print(sum)
#     return sum
# cal_sum(5,10)
# cal_sum(40,200)
# cal_sum(6889, 6676)


# def print_hello():
#     print("hello, are you good ...?")

# print_hello() # function calling
# print_hello()
# print_hello()




# print the average of 3 numbers

def calc_avg(a, b, c, d, e):
    sum = a + b + c + d + e 
    avg = sum / 5
    print(avg)
    return avg

calc_avg(3,7,9,8,5)


# recursive function
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
# show(5)

# return n!

# n! = 1 * 2 * 3 * 4.....* (n-1) * n 
# 4! = 1 * 2 * 3 * 4 = 3! * 4
# 3! = 1 * 2 * 3 = 2! * 3
# 2! = 1 * 2
# n! = (n-1)! * n

# def fact(n):
#     if(n == 0 or n == 1): #base case
#         return 1
#     return fact(n-1) * n  #logic
# print(fact(10))