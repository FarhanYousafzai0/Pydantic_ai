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


# from dataclasses import dataclass


# @dataclass
# class User:
#     name: str
#     age: int




# result = User("Farhan",20)


# print(result)





# @dataclass

# class Person:
#     name:str
#     age:int


#  Inheritence In Dataclasses:
# @dataclass

# class Employe(Person):
#     salary:int
#     employee_id:int





# result = Employe("Farhan",20,1000,123)



# print(result)



# Immutability In Dataclasses:



# @dataclass(frozen=True)

# class Point:
#    x:int
#    y:int



# print(Point(1,2))

# # 
# @dataclass
# class Product:
#     name: str
#     price: float
#     in_stock: bool = True



# print(Product("Laptop",1000.0))


# 

    # from dataclasses import field,dataclass

    # @dataclass

    # class User:
    #     name: str
    #     age: int

    #     def __post_init__(self):
    #         if self.age <= 18:
    #             raise ValueError("Age cannot be less than 18")

        
        
        
        




    # print(User("Farhan",15))







# Asyncio:



import asyncio


# async def Greeting():

#     print("Hello, World!")

#     await asyncio.sleep(3)

#     print("Hello, World! 2")



# asyncio.run(Greeting())




# So there are some difference between time.sleep() and ayncio.sleep()

# So the first one froze everything while ther other one not froze everything ,just wait to exeucte from the awiat task ,
# and the other task work as same.






# async def Task1():
#     await asyncio.sleep(2)
#     print("Task 1")




# async def Task2():   
#     await asyncio.sleep(2)
#     print("Task 2")




# async def main():
#     await asyncio.gather(Task1(),Task2())



# asyncio.run(main())





# 



# async def wait_and_print():

#     print("Waiting.....");

#     await asyncio.sleep(3)

#     print("Finished Waiting.....");





# asyncio.run(wait_and_print())


# import requests



# async def image1():

#     URL = "https://cdn.wallpapersafari.com/9/81/yaqGvs.jpg"
#     response = requests.get(URL)
#     if response.status_code == 200:
#         with open("image1.jpg","wb") as file:
#             file.write(response.content)







# async def image2():
#     URL = "https://images8.alphacoders.com/119/thumb-1920-1195441.jpg"

#     response = requests.get(URL)

#     if response.status_code == 200:
#         with open("image2.jpg","wb") as file:
#             file.write(response.content)




# async def image3():

#     URL = "https://play-lh.googleusercontent.com/BpZW3-Loxcv_DY3RX8bmVGzPl6d4NXPe5gOUg2MgYa8WJWD8vd1Y9T2EsQvDVuqvpTQM"
#     response = requests.get(URL)
#     if response.status_code == 200:
#         with open("image3.jpg","wb") as file:
#             file.write(response.content)




# async def main():
#     await asyncio.gather(image1(),image2(),image3())


# asyncio.run(main())








# import time


# def blocking_task():
#     print("Blocking Start")
#     time.sleep(3)
#     print("Blocking End")


# async def async_task():
#     print("Async Start")
#     await asyncio.sleep(3)
#     print("Async End")



# async def main():
#     await async_task()
#     blocking_task()

# asyncio.run(main())






# 
# import asyncio

# async def func1():

#     await asyncio.sleep(2)
#     print("I am the first function")




# async def func2():
#     await asyncio.sleep(2)
#     print("I am the second function")




# async def main():
#     await asyncio.gather(func1(),func2())




# asyncio.run(main())






#  Evironment Variables :


# import os 

# from dotenv import load_dotenv



# load_dotenv()


# api_key = os.getenv("API_KEY")
# print(api_key)







# Logging :



# import logging


# logging.basicConfig(level=logging.INFO);



# logging.info("This is an info message");
# logging.warning("This is a warning message");
# logging.error("This is an error message");
# logging.critical("This is a critical message");






# Pydantic Ai 





# class User(BaseModel):
#     name:str = Field(...,description="The name of the user.")
#     age:int = Field(...,description="The age of the user.")
#     email:EmailStr = Field(...,description="The email of the user.")



# user = User(name="Farhan",age=20,email="farhan@example.com")
# print(user)




# Validation:1. BaseModel — The Foundation for Validation
# 2. Field — Defines the structure of the model
# 3. EmailStr — A validator for email addresses
# 4. Validation Errors — Handling validation errors
# 5. Custom Validation — Adding custom validation
# 6. Pydantic AI — AI-powered validation
# 7. Pydantic Settings — Configuration for Pydantic
# 8. Pydantic Models — Creating reusable models
# 9. Pydantic Validators — Custom validation functions
# 10. Pydantic Types — Built-in types for validation
# 11. Pydantic Extensions — Extending Pydantic functionality



# BASIC MODEL .

# class CustomUser(BaseModel):
#     name:str = Field(...,description="The name of the user.")
#     age:int = Field(...,description="The age of the user.")
#     email:EmailStr = Field(...,description="The email of the user.")
#     is_active:bool = Field(default=True,description="Whether the user is active.")
#     nickname:str | None = Field(default=None,description="The nickname of the user.")





# user = CustomUser(name="Farhan",age=20,email="farhan@example.com",is_active=True,nickname="Farhan")

# print(user)

# from pydantic import BaseModel, field_validator

# class User(BaseModel):
#     name: str
#     age: int
#     email: str
#     password: str

#     @field_validator("age")
#     @classmethod
#     def age_must_be_positive(cls, value):
#         if value < 0:
#             raise ValueError("Age cannot be negative")
#         if value > 150:
#             raise ValueError("Age seems unrealistic")
#         return value

#     @field_validator("name")
#     @classmethod
#     def name_must_not_be_empty(cls, value):
#         if len(value.strip()) == 0:
#             raise ValueError("Name cannot be empty")
#         return value.strip().title()   # auto clean + capitalize

#     @field_validator("password")
#     @classmethod
#     def password_strength(cls, value):
#         if len(value) < 8:
#             raise ValueError("Password must be at least 8 characters")
#         if not any(c.isupper() for c in value):
#             raise ValueError("Password must have uppercase letter")
#         return value


# # Test
# user = User(name="  ahmed  ", age=25, email="a@b.com", password="Secret123")
# print(user.name)   # "Ahmed" ← auto cleaned and capitalized!

# # ❌ Bad age
# User(name="Ali", age=-5, email="a@b.com", password="Secret123")
# ValidationError: Age cannot be negative






# 3. Model Nesting — Models Inside Models


# from pydantic import BaseModel
# from typing import List

# class Address(BaseModel):
#     street: str
#     city: str
#     country: str
#     zip_code: str

# class SocialMedia(BaseModel):
#     platform: str
#     username: str
#     followers: int = 0

# class User(BaseModel):
#     name: str
#     age: int
#     address: Address             # nested model!
#     social_accounts: List[SocialMedia] = []  # list of nested models!

# # Create nested data
# user = User(
#     name="Ahmed",
#     age=28,
#     address={                    # dict auto converts to Address model!
#         "street": "123 Main St",
#         "city": "Peshawar",
#         "country": "Pakistan",
#         "zip_code": "25000"
#     },
#     social_accounts=[
#         {"platform": "GitHub", "username": "ahmed_dev", "followers": 500},
#         {"platform": "LinkedIn", "username": "ahmed_pk", "followers": 1200},
#     ]
# )

# print(user.address.city)                      # Peshawar
# print(user.social_accounts[0].platform)      # GitHub
# print(user.social_accounts[1].followers)     # 1200




# 4. Serialization — Model ↔ Dict ↔ JSON


from pydantic import BaseModel

# class Product(BaseModel):
#     name: str
#     price: float
#     in_stock: bool = True



# product = Product(name="Laptop",price=1000.0,in_stock=True)


# # Model To Dictionary:

# data_dic = product.model_dump()
# print(data_dic)



# # Model To Json :


# data_json = product.model_dump_json()

# print(data_json)


# # Json To Model :

# raw_data = {"name": "Phone", "price": 30000.0}


# product = Product.model_validate(raw_data)

# print(product)



# # 
# json_str = '{"name": "Tablet", "price": 45000.0}'


# tablet = Product.model_validate_json(json_str)
# print(tablet.name)




# 5. Field() — Advanced Field Configuration


from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
        description="Product name"
    )
    price: float = Field(
        gt=0,           # greater than 0
        lt=1_000_000,   # less than 1 million
        description="Price in PKR"
    )
    quantity: int = Field(
        ge=0,           # greater than or equal to 0
        default=0
    )
    discount: float = Field(
        ge=0.0,
        le=1.0,         # between 0 and 1 (0% to 100%)
        default=0.0
    )
    tags: list[str] = Field(
        default_factory=list,   # mutable default!
        max_length=10
    )


# ✅ Valid
p = Product(name="Laptop", price=75000, quantity=5, discount=0.1)

# ❌ Price <= 0
Product(name="Phone", price=100)
# ValidationError: price: Input should be greater than 0

# ❌ Name too short
Product(name="Still", price=100)
# ValidationError: name: String should have at least 2 characters

print(p)