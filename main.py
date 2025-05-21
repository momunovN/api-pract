from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI(
    title="Название",
    description="API",
    version="1.0.0"
)

# Data models
class User(BaseModel):
    id: int
    FIO: str
    email: str
    birthday: date
    INN: int
    citizenship: str
    password: str

class Order(BaseModel):
    id: int
    The_beginning_of_the_lease: date
    end_of_lease: date
    place: str
    final_price: float
    user_id: int
    cars_id: int

class Car(BaseModel):
    id: int
    name_car: str
    price: float
    year: int
    box: str
    body_type: str
    salon: str
    tank_capacity: float
    cruise_control: bool  # Changed from Boolean to bool
    maximum_speed: float
    fuel_consumption: float
    colors_id: int
    engines_id: int
    drives_id: int
    fuels_id: int

# In-memory storage
users = []
orders = []
cars = []

@app.get("/users")
def get_users():
    return users

@app.post("/users")
def add_user(user: User):
    users.append(user)
    return {"message": "Пользователь добавлен"}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    for index, existing_user in enumerate(users):
        if existing_user.id == user_id:
            users[index] = user
            return {"message": "Пользователь обновлен", "item": user}
    return {"message": "Пользователь не найден"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, existing_user in enumerate(users):
        if existing_user.id == user_id:
            removed_user = users.pop(index)
            return {"message": "Пользователь удален", "item": removed_user}
    return {"message": "Пользователь не найден"}

# Similar endpoints for orders and cars can be created using the same pattern

@app.get("/contacts")
def get_contacts():
    return {
        "tel": "977 159 16 90",
        "email": "asdasd@afa.asd",
        "VK": "auto"
    }
