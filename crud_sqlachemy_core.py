import os

from sqlalchemy import create_engine, insert

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
        'first_name': 'Olga',
        'last_name': 'Pavluchenko',
        'username': 'pavlik_o',
        'email': 'pavliko@mail.com',
        'address': '21/1 Makarenko st.',
        'town': 'Kiev'
    },
    {
        'first_name': 'Mikhail',
        'last_name': 'Levanov',
        'username': 'leva',
        'email': 'leva@mail.com',
        'address': '16/1 Azerbaydjanskaya st.',
        'town': 'Irpen'
    },
]

insert_data2 = insert(customers)

conn.execute(insert_data2, data)
