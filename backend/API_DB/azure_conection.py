import pyodbc
import keys


try:
    conn = pyodbc.connect(
        f"DRIVER={keys.driver};SERVER={keys.server};DATABASE={keys.database};UID={keys.username};PWD={keys.password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
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
