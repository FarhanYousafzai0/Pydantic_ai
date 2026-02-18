# from pydantic import BaseModel, model_validator, field_validator

# class UserRegistration(BaseModel):
#     username: str
#     password: str
#     confirm_password: str
#     age: int
#     referral_code: str | None = None

#     @field_validator("password")
#     @classmethod
#     def password_strength(cls, value):
#         if len(value) < 8:
#             raise ValueError("Password must be 8+ characters")
#         return value

#     @model_validator(mode="after")
#     def passwords_must_match(self):
#         # Can only check this AFTER both fields are validated!
#         if self.password != self.confirm_password:
#             raise ValueError("Passwords do not match!")
#         return self

#     @model_validator(mode="after")
#     def adult_needs_no_referral(self):
#         # Cross-field logic — checking age AND referral together
#         if self.age < 18 and self.referral_code is None:
#             raise ValueError("Users under 18 need a referral code")
#         return self


# # ✅ Valid registration
# user = UserRegistration(
#     username="ahmed_dev",
#     password="Secret123",
#     confirm_password="Secret123",
#     age=25
# )
# print("Registration valid!")

# # ❌ Passwords don't match
# UserRegistration(
#     username="sara",
#     password="Secret123",
#     confirm_password="Wrong456",
#     age=22
# )
# # ValidationError: Passwords do not match!

# # ❌ Minor without referral
# UserRegistration(
#     username="young_user",
#     password="Secret123",
#     confirm_password="Secret123",
#     age=15
# )
# ValidationError: Users under 18 need a referral code





# Second Mini Project :

# validator_app.py
# validator_app.py
from pydantic import BaseModel, Field, field_validator, EmailStr
from pydantic import model_validator
from typing import List, Optional
from datetime import datetime

class OrderItem(BaseModel):
    product_name: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)

    @property
    def total_price(self):
        return self.quantity * self.unit_price


class Order(BaseModel):
    order_id: str
    customer_email: str
    items: List[OrderItem]
    discount_percent: float = Field(ge=0, le=100, default=0)
    created_at: datetime = Field(default_factory=datetime.now)

    @field_validator("order_id")
    @classmethod
    def validate_order_id(cls, value):
        if not value.startswith("ORD-"):
            raise ValueError("Order ID must start with 'ORD-'")
        return value

    @model_validator(mode="after")  # runs after all fields validated
    def check_items_not_empty(self):
        if len(self.items) == 0:
            raise ValueError("Order must have at least one item")
        return self

    @property
    def subtotal(self):
        return sum(item.total_price for item in self.items)

    @property
    def final_total(self):
        discount = self.subtotal * (self.discount_percent / 100)
        return self.subtotal - discount


# Test it!
order = Order(
    order_id="ORD-12345",
    customer_email="ahmed@gmail.com",
    items=[
        {"product_name": "Laptop", "quantity": 1, "unit_price": 75000},
        {"product_name": "Mouse", "quantity": 2, "unit_price": 1500},
    ],
    discount_percent=10
)

print(f"Order ID: {order.order_id}")
print(f"Items: {len(order.items)}")
print(f"Subtotal: PKR {order.subtotal:,.0f}")
print(f"Discount: {order.discount_percent}%")
print(f"Final Total: PKR {order.final_total:,.0f}")
print(f"Created: {order.created_at}")
