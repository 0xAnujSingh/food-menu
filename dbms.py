import sqlite3

conn = sqlite3.connect('restaurant-menu.db')

c = conn.cursor()

c. execute("""CREATE TABLE menu(
    menuId integer primary key autoincrement not null,
    title varchar(120) not null unique,
);
""")

c.execute("""CREATE TABLE item(
    id integer primary key autoincrement not null,
    name varchar(120) not null,
    price integer not null,
    menuId integer FOREIGN KEY REFERENCES menu(menuId)
    
);
""")

conn.commit()
conn.close()


