import os

from sqlalchemy import create_engine, insert, select, or_, and_, not_

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
# conn.execute(insert_data)

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

# conn.execute(insert_data1)

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

insert_data2 = insert(customers)

# conn.execute(insert_data2, data)

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

# conn.execute(insert(items), items_list)
# conn.execute(insert(orders), order_list)
# conn.execute(insert(order_lines), order_line_list)


# select * from customers
# first method:
select_query = customers.select()
result = conn.execute(select_query).fetchall()
# fetchone() for one record from table;
# fetchmany(size) etch the specified number of rows from the result set;
# first() fetch the first row from the result set;
# rowcount returns the number of rows in the result set;
# keys() returns a list of columns from table.

# second method:
select_query1 = select([customers])
result1 = conn.execute(select_query1).fetchall()

# filtering records
select_filter = select([items]).where(items.c.cost_price > 60)
result_filter = conn.execute(select_filter).fetchall()

# Bitwise Operators &(and_), |(or_) and ~(not_) allow us to connect conditions
# with SQL AND, OR and NOT operators respectively.

# AND
filter_select = select([items]).where(
    items.c.selling_price - items.c.cost_price > 20
).where(
    items.c.quantity > 9
)
# or
filter_select1 = select([items]).where(
    (items.c.selling_price - items.c.cost_price > 20) &
    (items.c.quantity > 9)
)
# or
filter_select2 = select([items]).where(
    and_(
        items.c.selling_price - items.c.cost_price > 20,
        items.c.quantity > 9,
    )
)

# OR
select_or = select([items]).where(
    (items.c.quantity > 5) | (items.c.cost_price > 100)
)
# or
select_or1 = select([items]).where(
    or_(
        items.c.quantity > 5,
        items.c.cost_price > 100,
    )
)

# NOT
select_not = select([items]).where(
    items.c.cost_price > 100,
    ~(items.c.quantity >= 9),
)
# or
select_not1 = select([items]).where(
    items.c.cost_price > 100,
    not_(items.c.quantity >= 9),
)

# select with IN
customers_select = select([customers]).where(
    customers.c.first_name.in_(['Alexandr', 'Larisa'])
)
# select with NOT IN
customers_select1 = select([customers]).where(
    customers.c.last_name.notin_(['Pokrovskiy', 'Vasuchenko'])
)
# select with BETWEEN
select_between = select([items]).where(
    items.c.cost_price.between(50, 120)
)
# select with NOT BETWEEN
select_notbetween = select([items]).where(
    not_(items.c.selling_price.between(50, 120))
)
# select with LIKE
select_name_a = select([customers]).where(
    customers.c.first_name.like('A%')
)  # can use ilike() for case-insensitive match
# select with NOT LIKE
select_name_another = select([customers]).where(
    not_(customers.c.first_name.ilike('a%'))
)
# select with ORDER BY
order_by = select([items]).order_by(items.c.cost_price)  # can using asc() or
# desc() from sqlalchemy core inside order_by

# limit select
limit_select = select([customers]).limit(3)

# limit columns
limit_columns = select([
    customers.c.first_name,
    customers.c.last_name
]).where(
    customers.c.first_name.ilike('a%')
)

# can assign a label to a column or expression using the label() method
sale_price = select([
    items.c.name,
    items.c.cost_price,
    items.c.selling_price,
    (items.c.selling_price * 0.9).label('new_price')
]).where(
    items.c.quantity > 5
)
