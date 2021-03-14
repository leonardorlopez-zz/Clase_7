import sqlite3

print("Creando base de datos...")
conn = sqlite3.connect("shop.db")
cursor = conn.cursor()
cursor.execute("""\
    CREATE TABLE remeras (
        marca TEXT,
        talle NUMERIC,
        color TEXT,
        lisa BOOLEAN,
        genero NUMERIC
    );
""")
conn.commit()
conn.close()
print("¡Listo!")
