import sqlite3

conn = sqlite3.connect('hw_6_DB.sqlite')


cur = conn.cursor()

cur.execute(
    '''CREATE TABLE IF NOT EXISTS categories(
        category integer PRIMARY KEY,
        category_name text NOT NULL,
        category_description text NOT NULL
    );'''
)

cur.execute(
    '''CREATE TABLE IF NOT EXISTS units(
        unit text PRIMARY KEY
    );'''
)

cur.execute(
    '''CREATE TABLE IF NOT EXISTS positions(
        position text PRIMARY KEY
    );'''
)

cur.execute(
    '''CREATE TABLE IF NOT EXISTS goods(
        good_id integer PRIMARY KEY,
        good_name text NOT NULL,
        good_unit text NOT NULL,
        good_cat integer NOT NULL,
        FOREIGN KEY (good_unit) REFERENCES units (unit),
        FOREIGN KEY (good_cat) REFERENCES categories (category)
    );'''
)

cur.execute(
    '''CREATE TABLE IF NOT EXISTS employees(
        employee_id integer PRIMARY KEY,
        employee_fio text NOT NULL,
        employee_position text NOT NULL,
        FOREIGN KEY (employee_position) REFERENCES positions (position)
    );'''
)

cur.execute(
    '''CREATE TABLE IF NOT EXISTS vendors(
        vendor_id integer PRIMARY KEY,
        vendor_name text NOT NULL,
        vendor_ownerchipform text NOT NULL,
        vendor_address text NOT NULL,
        vendor_phone text NOT NULL,
        vendor_email text NOT NULL
    );'''
)

conn.commit()

conn.close()