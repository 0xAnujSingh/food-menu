import sqlite3

conn = sqlite3.connect('restaurant-menu.db')

c = conn.cursor()
try:

    c.execute("DROP TABLE IF EXISTS restaurant;")
    c.execute("""
    CREATE TABLE restaurant (
        rId integer primary key autoincrement not null,
        title varchar(120) not null unique
    );
    """)

    c.execute("DROP TABLE IF EXISTS menu;")
    c.execute("""
    CREATE TABLE menu (
        menuId integer primary key autoincrement not null,
        rId integer not null,
        title varchar(120) not null,
        FOREIGN KEY (rId) REFERENCES restaurant(rId),
        UNIQUE(rId, title)
    );
    """)

    c.execute("DROP TABLE IF EXISTS item;")
    c.execute("""
    CREATE TABLE item (
        id integer primary key autoincrement not null,
        name varchar(120) not null,
        price integer not null,
        menuId integer,
        FOREIGN KEY (menuId) REFERENCES menu(menuId)
    );
    """)
    conn.commit()
    conn.close()
except sqlite3.OperationalError as e:
    raise 
