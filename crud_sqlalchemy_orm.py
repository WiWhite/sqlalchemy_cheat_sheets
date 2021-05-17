import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, and_, or_, not_

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
# insert records to Customer model
customers = [customer1, customer2, customer3, customer4, customer5,
             customer6, customer7]
# session.add_all(customers)
# session.commit()

item1 = Item(name='Desk', cost_price=99.21, selling_price=100.81, quantity=5)
item2 = Item(name='Pen', cost_price=4.45, selling_price=5.51, quantity=12)
item3 = Item(name='Headphone', cost_price=15.52, selling_price=6.81,
             quantity=50)
item4 = Item(name='Travel Bag', cost_price=20.1, selling_price=24.21,
             quantity=50)
item5 = Item(name='Keyboard', cost_price=20.1, selling_price=22.11,
             quantity=50)
item6 = Item(name='Monitor', cost_price=200.14, selling_price=212.89,
             quantity=50)
item7 = Item(name='Watch', cost_price=100.58, selling_price=104.41,
             quantity=50)
item8 = Item(name='Water Bottle', cost_price=20.89, selling_price=25,
             quantity=50)
# insert records to Item model
# session.add_all([item1, item2, item3, item4, item5, item6, item7, item8])
# session.commit()

order1 = Order(customer=customer1)
order2 = Order(customer=customer2)
order3 = Order(customer=customer3)

line_item1 = OrderLine(order=order1, item=item1, quantity=3)
line_item2 = OrderLine(order=order1, item=item2, quantity=2)
line_item3 = OrderLine(order=order2, item=item1, quantity=1)
line_item4 = OrderLine(order=order2, item=item2, quantity=4)
line_item5 = OrderLine(order=order3, item=item1, quantity=1)
line_item6 = OrderLine(order=order3, item=item2, quantity=4)

# insert records to Order and OrderLine models
# session.add_all([order1, order2, order3])
# session.commit()

# select * from customers
customers_all = session.query(Customer).all()

# select * from items
items = session.query(Item).all()

# select * from orders
orders = session.query(Order).all()

# count records in tables
count_customers = session.query(Customer).count()
count_items = session.query(Item).count()
count_orders = session.query(Order).count()

# select first record from table
first_customer = session.query(Customer).first()

# select record using get(primary key:int)
customer_2 = session.query(Customer).get(2)

# select * from customers where customers.town == 'Kiev'
customers_from_kiev = session.query(Customer).filter(
    Customer.town == 'Kiev'
).all()

# select * from customers where customers.town == 'Kiev' or customers.town == 'Irpen'
cust_from_kiev_irpen = session.query(Customer).filter(or_(
    Customer.town == 'Kiev',
    Customer.town == 'Irpen',
)).all()

# select * from customers where customers.first_name in ('Alexandr', 'Oleg')
customers_in = session.query(Customer).filter(
    Customer.first_name.in_(
        ['Alexandr', 'Oleg']
    )
).all()

# select * from customers where customers.first_name not in ('Alexandr', 'Oleg')
customers_not_in = session.query(Customer).filter(
    Customer.first_name.notin_(
        ['Alexandr', 'Oleg']
    )
).all()

# select first_name, second_name from customers where id between(2, 5)
customers_between = session.query(Customer).filter(
    Customer.id.between(2, 5)
).all()

# select first_name, second_name from customers where id not between(2, 5)
customers_not_between = session.query(Customer).filter(
    not_(Customer.id.between(2, 5))
).all()

# select * from customers where first_name like 'A%'
customers_like = session.query(Customer).filter(
    Customer.first_name.like('A%')
).all()

# select * from items order by items.cost_price
sort_items = session.query(Item).order_by(Item.cost_price).all()

# SELECT * FROM customers JOIN orders ON customers.id = orders.customer_id
inner_join = session.query(Customer).join(Order).all()

# left outer join
outer_join = session.query(
    Customer.first_name,
    Customer.last_name,
    Order.id
).outerjoin(Order).all()
