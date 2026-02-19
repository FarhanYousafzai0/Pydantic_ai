


from pydantic import BaseModel,Field,field_validator ,model_validator ,computed_field # type:ignore
from typing import List,Optional


class User(BaseModel):
    username:str = Field(min_length=3,max_length=20)
    email:str = Field(min_length=3,max_length=20)
    password:str = Field(min_length=3,max_length=20)
    age:int = Field(gt=0,lt=100)
    friends:List[str] = Field(default=[])
    



class SignUp(BaseModel):
    username:str = Field(min_length=3,max_length=20)
    password:str = Field(min_length=3,max_length=20)
    confirm_password:str = Field(min_length=3,max_length=20)


    @field_validator("password")
    def validate_password(cls,v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return v
    
    @field_validator("confirm_password")
    def validate_confirm_password(cls,v,info):
        if v != info.data["password"]:
            raise ValueError("Passwords do not match")
        return v

    @field_validator("username")
    def validate_username(cls,v):
        if " " in v:
            raise ValueError("Username cannot contain spaces")
        return v


@model_validator(mode="after")
def validate_password(cls,values):
    if values.password != values.confirm_password:
        raise ValueError("Passwords do not match")
    return values



# Assiggment :


class Booking(BaseModel):
    user_id:int = Field(gt=0)
    room_id:int = Field(gt=0)
    nights:int = Field(...,ge=1,le=30)
    rate_per_night:float = Field(...,gt=0)


@computed_field
@property
def total_price(self) -> float:
    return self.nights * self.rate_per_night

    @field_validator("nights")
    def validate_nights(cls,v):
        if v < 1 or v > 30:
            raise ValueError("Nights must be between 1 and 30")
        return v







# Nesting Models:


class Lesson(BaseModel):
    lesson_id:int = Field(gt=0)
    lesson_name:str = Field(min_length=3,max_length=20)



class Modules(BaseModel):
    module_id:int = Field(gt=0)
    module_name:str = Field(min_length=3,max_length=20)
    lessons:List[Lesson] = Field(default=[])


class Course(BaseModel):
    course_id:int = Field(gt=0)
    course_name:str = Field(min_length=3,max_length=20)
    modules:List[Modules] = Field(default=[])   

def main():
    print("Hello from new!")


if __name__ == "__main__":
    main()
