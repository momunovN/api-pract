from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from fastapi import FastAPI

# Создание базы данных и моделей
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    FIO = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    birthday = Column(date, index=True)
    INN = Column(Integer, unique=True, index=True)
    citizenship = Column(String, index=True)
    password = Column(String, index=True)

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    The_beginning_of_the_lease = Column(date, index=True)
    end_of_lease = Column(date, index=True)
    place = Column(String, index=True)
    final_price = Column(Float, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    cars_id = Column(Integer, ForeignKey("cars.id"))

    user = relationship("User ")
    cars = relationship("Cars")

class Cars(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    name_car = Column(String, index=True)
    price = Column(Float, index=True)
    year = Column(Integer, index=True)
    box = Column(String, index=True)
    body_type = Column(String, index=True)
    salon = Column(String, index=True)
    tank_capacity = Column(Float, index=True)
    cruise_control = Column(Boolean, index=True)
    maximum_speed = Column(Float, index=True)
    fuel_consumption = Column(Float, index=True)
    colors_id = Column(Integer, ForeignKey("colors.id"))
    engines_id = Column(Integer, ForeignKey("engines.id"))
    drives_id = Column(Integer, ForeignKey("drives.id"))
    fuels_id = Column(Integer, ForeignKey("fuels.id"))

    colors = relationship("Colors")
    engines = relationship("Engines")
    drives = relationship("Drives")
    fuels = relationship("Fuels")

class Fuels(Base):
    __tablename__ = "fuels"

    id = Column(Integer, primary_key=True, index=True)
    fuel = Column(String, index=True)

class Colors(Base):
    __tablename__ = "colors"

    id = Column(Integer, primary_key=True, index=True)
    Color = Column(String, index=True)

class Drives(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    drive = Column(String, index=True)

class Engines(Base):
    __tablename__ = "engines"

    id = Column(Integer, primary_key=True, index=True)
    engine = Column(String, index=True)

# Создание FastAPI приложения
app = FastAPI(
    title="Название",
    description="API",
    version="1.0.0"
)

users = []

@app.get("/users")
def get_users():
    return users

@app.post("/users")
def add_user(user: str):
    users.append(user)
    return {"message": "Задача добавлена"}

@app.put("/users")
def update_item(old: str, new: str, id: int, FIO: str, email: str, birthday: date, INN: int, citizenship: str, password: str):
    if old in users:
        index = users.index(old)
        users[index] = new
        return {"message": "Обновлено", "item": new}

@app.delete("/users")
def delete_item(item: str):
    if item in users:
        users.remove(item)
        return {"message": "Удалено", "item": item}

order = []

@app.get("/order")
def get_order():
    return order

@app.post("/order")
def add_order(order: str):
    order.append(order)
    return {"message": "Задача добавлена"}

@app.put("/order")
def update_order(old: str, new: str, id: int, The_beginning_of_the_lease: date, end_of_lease: date, place: str, final_price: float, user_id: int, cars_id: int):
    if old in order:
        index = order.index(old)
        order[index] = new
        return {"message": "Обновлено", "item": new}

@app.delete("/order")
def delete_order(item: str):
    if item in order:
        order.remove(item)
        return {"message": "Удалено", "item": item}

cars = []

@app.get("/cars")
def get_cars():
    return cars

@app.post("/cars")
def add_cars(car: str):
    cars.append(car)
    return {"message": "Задача добавлена"}

@app.put("/cars")
def update_cars(old: str, new: str, id: int, name_car: str, price: float, year: int, box: str, body_type: str, salon: str, tank_capacity: float, cruise_control: bool, maximum_speed: float, fuel_consumption: float, colors_id: int, engines_id: int, drives_id: int, fuels_id: int):
    if old in cars:
        index = cars.index(old)
        cars[index] = new
        return {"message": "Обновлено", "item": new}

@app.delete("/cars")
def delete_cars(item: str):
    if item in cars:
        cars.remove(item)
        return {"message": "Удалено", "item": item}

fuels = []

@app.get("/fuels")
def get_fuels():
    return fuels

@app.post("/fuels")
def add_fuel(fuel: str):
    fuels.append(fuel)
    return {"message": "Задача добавлена"}

@app.put("/fuels")
def update_fuel(old: str, new: str, id: int, fuel: str):
    if old in fuels:
        index = fuels.index(old)
        fuels[index] = new
        return {"message": "Обновлено", "item": new}

@app.delete("/fuels")
def delete_fuel(item: str):
    if item in fuels:
        fuels.remove(item)
        return {"message": "Удалено", "item": item}

colors = []

@app.get("/colors")
def get_colors():
    return colors

@app.post("/colors")
def add_color(color: str):
    colors.append(color)
    return {"message": "Задача добавлена"}

@app.put("/colors")
def update_color(old: str, new: str, id: int, color: str):
    if old in colors:
        index = colors.index(old)
        colors[index] = new
        return {"message": "Обновлено", "item": new}

@app.delete("/colors")
def delete_color(item: str):
    if item in colors:
        colors.remove(item)
        return {"message": "Удалено", "item": item}

drivers = []

@app.get("/drivers")
def get_drivers():
    return drivers

@app.post("/drivers")
def add_driver(driver: str):
    drivers.append(driver)
    return {"message": "Задача добавлена"}

@app.put("/drivers")
def update_driver(old: str, new: str, id: int, drive: str):
    if old in drivers:
        index = drivers.index(old)
        drivers[index] = new
        return {"message": "Обновлено", "item": new}

@app.delete("/drivers")
def delete_driver(item: str):
    if item in drivers:
        drivers.remove(item)
        return {"message": "Удалено", "item": item}

engines = []

@app.get("/engines")
def get_engines():
    return engines

@app.post("/engines")
def add_engine(engine: str):
    engines.append(engine)
    return {"message": "Задача добавлена"}

@app.put("/engines")
def update_engine(old: str, new: str, id: int, engine: str):
    if old in engines:
        index = engines.index(old)
        engines[index] = new
        return {"message": "Обновлено", "item": new}

@app.delete("/engines")
def delete_engine(item: str):
    if item in engines:
        engines.remove(item)
        return {"message": "Удалено", "item": item}

@app.get("/contacts")
def get_contacts():
    return {
        "tel": "8 800 555 35 34",
        "email": "aaa@aaa.aaa",
        "VK": "auto"
    }

# Настройка базы данных
DATABASE_URL = "sqlite:///./example.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
