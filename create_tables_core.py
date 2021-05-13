import os
import datetime

from sqlalchemy import create_engine, Integer, String, DateTime, ForeignKey,\
    Table, Column, MetaData, Numeric


user = os.environ['psql_admin']
passwd = os.environ['psql_passwd']

metadata = MetaData()
engine = create_engine(
    f'postgresql+psycopg2://{user}:{passwd}@localhost/postgres',
    echo=True,
)

customers = Table(
    'customers', metadata,
    Column('id', Integer(), primary_key=True),
    Column('first_name', String(30), nullable=False),
    Column('last_name', String(40), nullable=False),
    Column('username', String(50), unique=True, nullable=False),
    Column('email', String(50), unique=True, nullable=False),
    Column('address', String(100), nullable=False),
    Column('town', String(100), nullable=False),
    Column('created_on', DateTime, default=datetime.datetime.now),
    Column(
        'updated_on',
        DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now
    ),
)

items = Table(
    'items', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(50), nullable=False),
    Column('cost_price', Numeric(10, 2), nullable=False),
    Column('selling_price', Numeric(10, 2), nullable=False),
    Column('quantity', Integer(), nullable=False),
)

orders = Table(
    'orders', metadata,
    Column('id', Integer(), primary_key=True),
    Column('customer_id', ForeignKey('customers.id')),
    Column('date_placed', DateTime(), default=datetime.datetime.now),
    Column('date_shipped', DateTime()),
)

order_lines = Table(
    'order_lines', metadata,
    Column('id', Integer(), primary_key=True),
    Column('order_id', ForeignKey('orders.id')),
    Column('item_id', ForeignKey('items.id')),
    Column('quantity', Integer(), nullable=False),
)

metadata.create_all(engine)
