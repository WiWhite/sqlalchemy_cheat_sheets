import os

from sqlalchemy import create_engine, insert, select

from create_tables_core import customers, items, orders, order_lines

user = os.environ['psql_admin']
passwd = os.environ['psql_passwd']

engine = create_engine(
    f'postgresql+psycopg2://{user}:{passwd}@localhost/sqlalchemy',
    echo=True,
)

conn = engine.connect()

# the most basic method to insert records into the DB
insert_data = customers.insert().values(
    first_name='Alexandr',
    last_name='Pokrovskiy',
    username='wiwhite',
    email='test@gmail.com',
    address='10 Turhenivska st.',
    town='Kiev',
)

# To view the SQL this code would generate type the following
print(insert_data)

# We can view the values that will replace the bind parameters by compiling
# the insert statement
print(insert_data.compile().params)

# insert data to table customers
conn.execute(insert_data)

# Next way to create insert statement is to use insert() function from
# the sqlalchemy package.
insert_data1 = insert(customers).values(
    first_name='Yulia',
    last_name='Bokeeva',
    username='bokoporova',
    email='bokoporova@gmail.com',
    address='22 Khreschatik st.',
    town='Kiev',
)

conn.execute(insert_data1)

# Multiple Inserts

data = [
    {
        'first_name': 'Larisa',
        'last_name': 'Vasuchenko',
        'username': 'lariska',
        'email': 'lariska@mail.com',
        'address': '21/1 Dritrievsakya st.',
        'town': 'Irpen'
    },
    {
        'first_name': 'Anatol',
        'last_name': 'Popov',
        'username': 'anatol',
        'email': 'anatol@mail.com',
        'address': '16/1 Prajsakaya st.',
        'town': 'Kiev'
    },
]
#
insert_data2 = insert(customers)

conn.execute(insert_data2, data)


items_list = [
    {
        'cost_price': 9.21,
        'name': 'Pen',
        'quantity': 5,
        'selling_price': 10.81,
    },
    {
        'cost_price': 9.11,
        'name': 'Chair',
        'quantity': 8,
        'selling_price': 10.98,
    },
    {
        'cost_price': 350.21,
        'name': 'Monitor',
        'quantity': 11,
        'selling_price': 410.91,
    },
    {
        'cost_price': 126.58,
        'name': 'Touchpad',
        'quantity': 9,
        'selling_price': 198.31,
    },
    {
        'cost_price': 76.78,
        'name': 'Keyboard',
        'quantity': 17,
        'selling_price': 93.11,
    },
    {
        'cost_price': 254.48,
        'name': 'Printer',
        'quantity': 4,
        'selling_price': 288.37,
    },
    {
        'cost_price': 54.68,
        'name': 'Lamp',
        'quantity': 3,
        'selling_price': 79.11,
    },
    {
        'cost_price': 203.18,
        'name': 'Table',
        'quantity': 8,
        'selling_price': 243.31,
    },
]

order_list = [
    {
        'customer_id': 1
    },
    {
        'customer_id': 1
    }
]

order_line_list = [
    {
        'order_id': 1,
        'item_id': 1,
        'quantity': 5
    },
    {
        'order_id': 1,
        'item_id': 2,
        'quantity': 2
    },
    {
        'order_id': 1,
        'item_id': 3,
        'quantity': 1
    },
    {
        'order_id': 2,
        'item_id': 1,
        'quantity': 5
    },
    {
        'order_id': 2,
        'item_id': 2,
        'quantity': 5
    },
]

conn.execute(insert(items), items_list)
conn.execute(insert(orders), order_list)
conn.execute(insert(order_lines), order_line_list)


# select * from customers
# first method:
select_query = customers.select()
result = conn.execute(select_query).fetchall()
# or fetchone() for one record from table;
# fetchmany(size) etch the specified number of rows from the result set;
# first() fetch the first row from the result set;
# rowcount returns the number of rows in the result set;
# keys() returns a list of columns from table.

# second method:
select_query1 = select([customers])
