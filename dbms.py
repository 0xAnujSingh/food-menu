import sqlite3

conn = sqlite3.connect('restaurant-menu.db')

c = conn.cursor()
try:
    c.execute("""CREATE TABLE menu10(
        menuId integer primary key autoincrement not null,
        title varchar(120) not null unique
    );
    """)



    c.execute("""CREATE TABLE item11(
        id integer primary key autoincrement not null,
        name varchar(120) not null,
        price integer not null,
        menuId int,
        FOREIGN KEY (menuId) REFERENCES menu(menuId)
    
    );
    """)
    conn.commit()
    conn.close()
except sqlite3.OperationalError as e:
    raise 
