from datetime import datetime
import os

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, \
    DateTime, SmallInteger, create_engine

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    address = Column(String(200), nullable=False)
    town = Column(String(50), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
    orders = relationship('Order', backref='customer')

    def __repr__(self):
        return f'Customer({self.id}, {self.first_name}, {self.last_name})'


class OrderLine(Base):
    __tablename__ = 'order_lines'
    order_id = Column(Integer(), ForeignKey('orders.id'), primary_key=True)
    item_id = Column(Integer(), ForeignKey('items.id'), primary_key=True)
    quantity = Column(SmallInteger())
    order = relationship('Order', backref='items')
    item = relationship('Item', backref='orders')


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    date_placed = Column(DateTime(), default=datetime.now)
    line_items = relationship('OrderLine', backref='orders')

    def __repr__(self):
        return f'Order({self.customer_id})'


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price = Column(Numeric(10, 2), nullable=False)
    selling_price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(SmallInteger())
    line_items = relationship('OrderLine', backref='items')

    def __repr__(self):
        return f'Item({self.id}, {self.name})'


if __name__ == '__main__':
    user = os.environ['psql_admin']
    passwd = os.environ['psql_passwd']
    engine = create_engine(
        f'postgresql+psycopg2://{user}:{passwd}@localhost/postgres',
        echo=True,
    )
    Base.metadata.create_all(engine)
