import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='Rishi@postgres1969' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store ( item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(name, quan, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='Rishi@postgres1969' host='localhost' port='5432'")
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES(?,?,?)",(name, quan, price))
    cur.execute("INSERT INTO store VALUES( %s, %s, %s)",(name, quan, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='Rishi@postgres1969' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(name):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='Rishi@postgres1969' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s", (name,))
    conn.commit()
    conn.close()

def update(name, quan, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='Rishi@postgres1969' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item = %s", (quan, price, name))
    conn.commit()
    conn.close()

create_table()
update('Mac', 1, 120)
insert('iphone13', 1, 140)
print(view())