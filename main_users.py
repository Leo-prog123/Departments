from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


# Добавляем капитана
def main():
    db_session.global_init("db/mars_explorer_.db")
    session = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Weir"
    user.name = "Andy"
    user.age = 18
    user.position = "chief scientist"
    user.speciality = "geologist"
    user.address = "module_1"
    user.email = "andy_chief@mars.org"
    user.hashed_password = "sci"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Watny"
    user.name = "Mark"
    user.age = 25
    user.position = "middle scientist"
    user.speciality = "biologist"
    user.address = "module_2"
    user.email = "mark@mars.org"
    user.hashed_password = "bio"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Kapoor"
    user.name = "Venkat"
    user.age = 15
    user.position = "pilot"
    user.speciality = "pilot, navigator"
    user.address = "module_2"
    user.email = "kapoor@mars.org"
    user.hashed_password = "pilot"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Sanders"
    user.name = "Teddy"
    user.age = 27
    user.position = "programmer"
    user.speciality = "IT specialist"
    user.address = "module_2"
    user.email = "sanders@mars.org"
    user.hashed_password = "comp"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Bean"
    user.name = "Sean"
    user.age = 17
    user.position = "chief engineer"
    user.speciality = "builder"
    user.address = "module_1"
    user.email = "bean@mars.org"
    user.hashed_password = "build"

    user.set_password(user.hashed_password)
    session.add(user)
    session.commit()


if __name__ == '__main__':
    main()
