what is python ?? 

- python is simple, easy & Portable.
- python is free & open sourse.
- python is high level, interpreted language.
- python was developed by Guido van Rosum.


- python is interpreted language means when we write python code its executed the code line by line thats why we called python is interpreted language.

- print is function to give output statement in python. simply we can tell "print" is output function.

character set of python language :- 
1. letter -> A-Z, a-z
2. Digits -> 0 - 9
3. Special character -> -,+,/,* etc..
4. Whitespaces -> Blank Space, Tab, newline 

what is variable in python :- a variable is a name given to a memory location in a program or else we can simply say varibale is a container to store some data.

example - 
name = "shradha" 
age = 23
salary = 23000.56

variable names - name, age, salary
varibale values - "shradha", 23, 23000.56


Rules for Identifires :- 
1. identifires - names of the variable 
2. identifires can be combination of uppercase and lowercase letter, digits or an underscore(_). ex. - myVariable, variable_1
3. an identifires can not start with digit. so while variable1 is valid but 1variable in not valid. 
4. we can not use special character or symbols like !,#,@,% etc...
5. identifires can be of any length. 
6. variables name should be small and meaningful like - when we give our age in that case we take the variable as "myAge".
myAge -> camel case letter 


- 'type' is a operator to show the datatypes name in our varibles like which datatypes we use in our variables.




Data Types :- 

- mainly data types of 5 types in python.
- These data types are unmutable or build-in data types.
1. Integer - +ve value , 0 , -ve value
2. String - "hello", "shradha" etc...
3. Float - 3.91, 4.00 , 9.1 etc..
4. Boolean - True , False
5. None - not assign 



Comments in python :- 

- when we write some code but we dont want to execute it then we give the comment line to that place so that line of code will not executed.
- comments are of 2 type. 
1. single line comment -
   when we give the single line comments. in python we did it on "#".
   ex. 
   # single line comment
   # this is a comment 
2. Multi line comment - 
   when we gibve the multi line comment in python we did it through """-""".
   ex. 
   """
    multi line 
    comments
   """


Types of Operator :- 
- simply we can say operator is a symbol that performs a certain operation between operands.
ex. a + b 
    a,b -> operands
    + -> operator
- there are 4 types of operator are present in python
1. arithmetic operator. - (+,-,/,%,*)
2. Relational operator. - (==, != ,> ,<, >=,<=)
3. assignment operator - (=, +=, -=, *=, /=, %=)
4. logical operator - (and, or, not)


Input in Python :- 

- Input() statement is used to accept values(use keyword) from users.



Task to do for practice - 
1. write a program to input 2 numbers & print their sum
2. Write a program to input side of a square & print its area.
3. write a program to input 2 floating point numbers & print their average.
4. write a program to input 2 int numbers a & b, print True if a is greater then or equal to . if not print false.

Strings :-

- String is datatype that stores a sequence of characters. 


str1 = "this is a good day" 
str2 = 'This is beautiful day'
str3 = """this is a bad day"""


- all these strings are real string because in python, it supports all of these syntax like - "", '',""" """

- \n (new line) - when we want to break our line into a new line then we can give the new line symbol in that place so the line get breaked automatically.


Basic Operation of strings :- 

1. concatenation -> 
     "hello" + "world" = 
2. Length of String -> 
      len(str)


Indexing of string -> 

- webbocket -> 012345678(indexing) 
- Always indexing start from '0'.



Slicing of string -> 

- Accessing parts of a string. 
- ending index is not counting.
- syntax - str[starting_index : ending_index]

str = "webbocket"
str[0:3] - web
str[:3] -  web
str[3:] - bocket





Functions of string -> 

ex- 
str = "i am a coder."
1. str.endswith("er.") - returns true if string ends with substring
2. str.capitalize() - returns 1st char is capital
3. str.replace(old,new) - replace all occurances of old with new 
4. str.find(word) - returns 1st index of 1st occurrence
5. str.count("am") - counts the occurrence of substring in string 


Homework :-
1. write a program to input users first name & print its length.
2. write a program to find the occerrence of '$' in a string.






conditional statement :- 

- used to handle the condition in your program. 
- syntax (if-elif-else)
- elif means else-if

if(condition):
   statement1
elif(condition):
   statement2
else: 
   statement(default)


Homework :-
1. write a program to check if a number entered by the user if odd or even.
2. write a program to find the greatest of 3 numbers entered by the userd.
3. write a program to check if a number is a multiple of 7 or not.



Lists in Python :- 

- List is a built-in data type that stores set of values.
- it can store elements of different types like integer, float & string etc..
- in list we can make indexing.
- in list we can find length of the list also.
- in list we can also do the slicing activity.

ex-
marks = [87, 45, 67, 83, 45] - array and list
student = ["hitesh", 85, "bhubaneswar"] - list



List Slicing :- 

- it similar to string slicing.
- syntax :- list_name[starting_idx : ending_idx]
- ending index is not included.

marks = [23,25,67,78,98]
marks[1:4] -> [25,67,78]
marks[:3] -> [23,25,67]
marks[2:] -> [67,78,98]




List Methods :- 

list = [9,4,7,8,1]
list.append(6) - adds one element at the end of the list - [9,4,7,8,1,6]
list.sort() - sort the elements in assending order - [1,4,7,8,9]
list.sort(reverse=True) - sorts the element in decending order - [9,8,7,4,1]
list.reverse() - reversing the list - [1,8,7,4,9]
list.insert(idx,el) - insert the element at index 
list.remove(1) - remove the firt occurrance of element - [9,7,8,1]
list.pop(idx) - remove element at index


git :- 

- git is a open source repository system where we can save, manipulate, colaborate our code with any one else. 
- in our software era, everyone can use git system for their software development.
- we also called git is a version control system.
- git provides some tools to use their functionality and features ex - github, gitlab etc.. 




Tuple in Python :- 

- Tuple is a build in data type that lets us create immutable(the value can't be changeble) sequence of values.
- ex. tup = (87,67,98,34,45)
- tup[0] -> 87
- tup[1] -> 67
- we can do the tuple as 
1. tup1 = () -> empty tuple
2. tup2 = (1,) -> tuple
3. tup3 = (34,67,89,20) -> tuple
- tuple has also satisfy the slicing property. 


tuple methods:- 

- tup.index(element) -> returns index of first occurrence
- tup.count(element) -> returns the count total occurrence 

ex. tup = (2,1,3,1,3,3) 
    tup.index(2) -> 3     
    tup.count(3) -> 3

Homework :- 

1. write a program to ask the user to enter names of their 3 favorite movies & store them in a list.
2. write a program if a list contains a palindrome of elements.
3. write a program to count the number of students with the "A" grade in the following tuples. ex. ("c","D","A","A","B","B","A"). store the above value in a list & sort them from "a" to "D".

Dictionary in Python :- 

- Dictionary are used to store the data values in key:value pair.
- They are unordered, mutable(changeable) & don't allow duplicate keys.
- ex- 
dict = {
   "name" : "shradha",
   "cgpa" : 9.8,
   "marks": [98,96,95],
}
- the left part of the dictionary are the keys & right side part in their values so dictionary contains key:value pair structure.



Nested Dictionary in python :-

- Dictionary also satisfy the nested property.
- Dictionaru under dictionary is called nested dictionary.
- ex. 
student = {
   "name" : "mithun",
   "score": {
      "chem" : 98,
      "math" : 87,
      "phy"  : 79
   }
}



Dictionary Methods :- 

1. myDict.keys() - it returns all keys.
2. myDict.values() - it returna all values
3. myDict.items() - it will returns all key:value pair as tuple.
4. myDict.get("key") - returns the key according to values.
5. myDict.update(newDict) - insert the specified items to the dictionary.


set in python :- 

- set is the collection of the unordered items.
- Each element in the set must be unique & immutable(can't change).
- ex.
nums = {1,2,3,4,5}
set2 = {5,8,9,4} 

set method :- 
1. set.add(element) -> adds an element
2. set.remove(element) -> remove an element
3. set.clear() -> clear all elements
4. set.pop() -> remove a random value of set
5. set.union(set2) -> combine both set values & returns a new set
6. set.intersection(set2) -> combines the common value & returns a new set.

ex. 
set1 = {1,2,3,2,4}
set2 = {3,7,2,6,4}
set1.union(set2) -> {1,2,3,4,6,7}
set1.intersection(set2) -> {2,3,4}


Loops in Python:- 

- Loops are used to repeat instruction.
- In python there are 2 loops - While loop, For loop
1. while loop:-
   syntax - 
   intialization
   while condition:
      statement
      increament/decrement.





office-works :- 

1. print numbers from 1 to 100
2. print numbers from 100 to 1
3. print the multiplication table of number n.
4. print the elements of the following list using a loop.
   [1,4,9,16,25,36,49,64,81,100]
5. search for a number x in this tuple using loop
   (1,4,9,16,25,36,49,64,81,100)




Break & Continue :- 

- break: break is used to terminate the loop when encountered.
- continue: terminates execution in the current iteration & continue execution of the loop with the next iteration. 


2. For Loop:-

- For loop are used for sequential traversal. for traversing list, string, tuple etc.
- syntax:- 
   for val in list:
      statement..



Homeworks :- (using for loop)
1. print the element of the following list using a loop:
   [1,4,9,16,25,36,49,64,81,100]
2. search for a number x in this tuple using loop.
   (1,4,9,16,25,36,49,64,81,100)

Range() :- 
- range function returns a sequence of numbers, starting from 0 by default, and increaments by 1 (by default), and stops before a specified number.

- syntax -> range(start , stop, step)


office-work :- (using for & range)
1. print numbers from 1 to 100
2. print numbers from 100 to 1
3. print the multiplication table of a number n



Functions in Python:- 
- Function is a block of statements that performs a specific task. 
- syntax :- 
def func_name(parameter 1, parameter 2..):
some statement
returns val

func_name(arg1, arg2..) #function call  

- Functions are of 2 types in python
1. Built-in function - print(), len(), type(), range() ... etc
2. user defined function - user can develop the function. 



office Work :- 
1. write a function to print the length of a list(list is the parameter)
2. write a function to print the element of a list in a single line(list is the paraneter)
3. write a function to find the factorial of n (n is the parameter)
   factorial means - 
   suppose i want to get the factorial of 5, 
   5! = 5 * 4 * 3 * 2 * 1
   syntax of factorial -> n! = 1 * 2 * 3 ... n * (n-1)
   4! = 4 * 3 * 2 * 1
   3! = 3 * 2 * 1
4. write a function to convert USD to INR. 


Recursion in python :- 

- when the function calls itself repeatedly is called recursion and this process we called recurance relation. 
- ex. print n to 1 backword
      
      def show(n):
         if(n == 0): #base case, where our program stopped their working
            return
         print(n)
         show(n-1)

      show(5)

      suppose i take n = 5 then it will print, 5,4,3,2,1

Object Oriented programming in Python :- 

- To map with real world scenarios, we strated using objects in code. This is called object oriented programming(OOP).

1st concept-> procedural programming
2nd concept-> functional programming
3rd concept-> object orientd programming


Class & Object in python :-

- class is a blueprint for creating objects.
ex.-> creating a class
class Student: 
   name = "web bocket"

ex.-> creating a object(instance)
s1 = Student()
print(s1.name) #web bocket


__init__ Function (constructor) :- 

- All class have a function called __init__(), which is always executed when the class is being initiated. 

ex. -> creating a class
class Student:
   def __init__(self, fullname):
      self.name = fullname

ex. -> creating a object
s1 = Student("web bocket")
print(s1.name)

Note:- The self parameter is a reference to the current instance of the class, and is used to access variable that belongs to the class.



class & instance Attributes:- 

university -> college1, college2, college3 , college4
              student1, student2, student3,  student4

- colleges and students are the attributes of university. 


methods in python :- 
- Methods are function that belongs to objects.

ex. -> creating class
class Student:
   def __init__(self, fullname):
      self.name = fullname
   def hello(self):
      print("hello", self.name)

ex. -> creating object
s1 = Student("rohan")
s1.hello()

Abstraction:- 
- Hiding the implementation details of a class and only showing the essential features to the user. 



Encapsulation:- 
- Wrapping data and function into a single unit(object). 


practice question - 
 - create Account class with 2 attributes - balance & account no. & create methods for debit, credit & printing the total balance.





Private(like) Attributes & Methods :- 
- private attributes & methods are meant to be used only within the class and are not accessible from outside the class.
- the private class attributes are written in __(attributes) so that we call it private attributes of a class.




Inheritance :- 

- when one class(child class) derives the properties & methods of another class(parent class). 
- syntax :- 
class car: 
   ----------
class ToyotaCar(car):
   ----------

- in python inheritance are of 3 types.
1. single inheritance
2. Multi-level inheritance
3. Multiple inheritance




Polymorphism: Operator Overloading:-

- when the same operator is allowed to have different meaning accordingly to the context.
- In that polymorphism we can use Dunder functions. 
1. a + b -> __add__
2. a - b -> __sub__
3. a * b -> __mul__
4. a / b -> __truediv__
5. a % b -> __mod__

ex - (+)
print(1 + 2) #3 (addition)
print("web" + "bocket") #web bocket (concatination)
print([1,2,3] + [4,5,6]) #[1,2,3,4,5,6] (merged)