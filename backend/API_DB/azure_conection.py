import pyodbc

server = "dinosaursdb.database.windows.net"
database = "dinosaursDB"
username = "adminuser"
password = "password321."
driver = "{ODBC Driver 18 for SQL Server}"

try:
    conn = pyodbc.connect(
        f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    )
    print("Conexión exitosa")
    cursor = conn.cursor()
    
    # Ejecutar consulta
    databse = cursor.execute("SELECT * FROM dinosaurs")
    rows = cursor.fetchall()
    
    # Mostrar resultados
    for row in rows:
        print(row)

    conn.close()
    
except Exception as e:
    print("Error en la conexión:", e)
