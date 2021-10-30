import psycopg2

def create_table():
    cony= psycopg2.connect("dbname='database1' user='postgres' password='Rishi@postgres1969' host='localhost' port='5432'")
    cur = cony.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store ( item TEXT, quantity INTEGER, price REAL)")
    cony.commit()
    cony.close()

def insert(name, quan, price):
    cony= psycopg2.connect("dbname='database1' user='postgres' password='Rishi@postgres1969' host='localhost' port='5432'")
    cur = cony.cursor()
    # cur.execute("INSERT INTO store VALUES(?,?,?)",(name, quan, price))
    cur.execute("INSERT INTO store VALUES( %s, %s, %s)",(name, quan, price))
    cony.commit()
    cony.close()

def view():
    cony= psycopg2.connect("dbname='database1' user='postgres' password='Rishi@postgres1969' host='localhost' port='5432'")
    cur = cony.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    cony.close()
    return rows

def delete(name):
    cony= psycopg2.connect("dbname='database1' user='postgres' password='Rishi@postgres1969' host='localhost' port='5432'")
    cur = cony.cursor()
    cur.execute("DELETE FROM store WHERE item = %s", (name,))
    cony.commit()
    cony.close()

def update(name, quan, price):
    cony= psycopg2.connect("dbname='database1' user='postgres' password='Rishi@postgres1969' host='localhost' port='5432'")
    cur = cony.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item = %s", (quan, price, name))
    cony.commit()
    cony.close()

create_table()
update('Mac', 1, 120)
insert('iphone13', 1, 140)
print(view())