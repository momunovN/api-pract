from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI(
    title="Момунов",
    description="Апи на практике",
    version="0.5.2"
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
    cruise_control: bool
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

# User endpoints
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

# Car endpoints
@app.get("/cars")
def get_cars():
    return cars

@app.post("/cars")
def add_car(car: Car):
    cars.append(car)
    return {"message": "Автомобиль добавлен"}

@app.put("/cars/{car_id}")
def update_car(car_id: int, car: Car):
    for index, existing_car in enumerate(cars):
        if existing_car.id == car_id:
            cars[index] = car
            return {"message": "Автомобиль обновлен", "item": car}
    return {"message": "Автомобиль не найден"}

@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    for index, existing_car in enumerate(cars):
        if existing_car.id == car_id:
            removed_car = cars.pop(index)
            return {"message": "Автомобиль удален", "item": removed_car}
    return {"message": "Автомобиль не найден"}

@app.get("/contacts")
def get_contacts():
    return {
        "tel": "977 159 16 90",
        "email": "asdasd@afa.asd",
        "VK": "auto"
    }
