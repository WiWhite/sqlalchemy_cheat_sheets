import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import Customer, Item, Order, OrderLine

user = os.environ['psql_admin']
passwd = os.environ['psql_passwd']
engine = create_engine(
    f'postgresql+psycopg2://{user}:{passwd}@localhost/postgres',
    echo=True,
)

Session = sessionmaker(bind=engine)
session = Session()

customer1 = Customer(
    first_name='Alexandr',
    last_name='Pokrovskiy',
    username='pokrova',
    email='test@gmail.com',
    address='16/1 Azerbaydjanskaya st.',
    town='Kiev',
)
customer2 = Customer(
    first_name='Anatol',
    last_name='Trohimchyk',
    username='trohim',
    email='trohim@gmail.com',
    address='23 Prajskaya st.',
    town='Kiev',
)
customer3 = Customer(
    first_name='Oleg',
    last_name='Grabovschik',
    username='Grab',
    email='grab@gmail.com',
    address='2 Goloseevskaya st.',
    town='Kharkov',
)
customer4 = Customer(
    first_name='Vitaliy',
    last_name='Rakom',
    username='Rak',
    email='rak12@gmail.com',
    address='28/10 Kudry st.',
    town='Kiev',
)
customer5 = Customer(
    first_name='Kora',
    last_name='Himerova',
    username='kora',
    email='kora@gmail.com',
    address='11 Khreshatik st.',
    town='Kharkov',
)
customer6 = Customer(
    first_name='Filip',
    last_name='Kirk',
    username='filya',
    email='filya@gmail.com',
    address='233 Centralnaya st.',
    town='Irpen',
)
customer7 = Customer(
    first_name='Kristina',
    last_name='Kubrak',
    username='kriskris',
    email='kubris@gmail.com',
    address='12 Poltavskaya st.',
    town='Irpen',
)
customers = [customer1, customer2, customer3, customer4, customer5,
             customer6, customer7]
session.add_all(customers)
session.commit()
