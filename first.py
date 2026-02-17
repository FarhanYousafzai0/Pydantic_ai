# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")




# import fibo



# fibo.fib(1000)

# fibo.fib2(100)

# fibo.__name__



# 




# from utils import add, multi

# print(add(2, 3))
# print(multi(4, 5))





# import sys

# for path in sys.path:
#     print(path)




# Type Hints :



# def find_user(user_id: int) -> str | None:
#     if user_id == 1:
#         return "Admin"
#     return None



# find_user(1)



# Union (Also Important) /Means value can be multiple types.
# def process(value: int | str) -> str:
#     return str(value)



# You when function run user can add multiple datatype like if user enter str,or int so its be fine ,it will not give any error:



# Union, so you can combine mutliple data types and so user can enter the datatype you combine.
# from typing import Union 


# def process(vale:Union[int,str]) -> str:
#     print()

# # Any 


# def processs(value:Any) -> None:
#     print(value)






# Mini Excerises:


# First Problems:

# def multi(a:float,b:float) -> float | None:
#     return a * b;




# result = multi(2.5,2.3)
# print(result)



# # Second Problems:

# def get_names(names: list[str]) -> str | None:
#     if names:
#         return names[0]
#     return None






# result = get_names(["Farhan","Ali"]);



# print(result)





# Third Problem :



# def format_id(user_id:str | int) -> str:
#     return user_id;




# print(format_id(888));
# print(format_id("123"));




# def insatncechecking(user_id:str | int) -> str:
#     if not isinstance(user_id,(str,int)):
#         raise TypeError("User id must be string or Number.")

#      return str(user_id)   




# from typing import Literal


# def set_status(status:Literal["success","error","pending"]) -> None:
#     print(status)



# set_status("success")





#  What Problem Do Dataclasses Solve?




# Dataclasea reduced the classes 


from dataclasses import dataclass


# @dataclass
# class User:
#     name: str
#     age: int




# result = User("Farhan",20)


# print(result)





@dataclass

class Person:
    name:str
    age:int


#  Inheritence In Dataclasses:
@dataclass

class Employe(Person):
    salary:int
    employee_id:int





result = Employe("Farhan",20,1000,123)



print(result)



# Immutability In Dataclasses:



@dataclass(frozen=True)

class Point:
   x:int
   y:int



print(Point(1,2))





