import pyodbc
from decimal import Decimal
import api_config.secret_keys as keys

def get_db_access():
    conn = pyodbc.connect(
        f"""DRIVER={keys.driver};
        SERVER={keys.server};
        DATABASE={keys.database};
        UID={keys.username};
        PWD={keys.password};
        Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"""
    )
    return conn
    
def search_dinosaur_info(nombre_dinosaurio):
    conn = get_db_access()
    print("Conexión Exitosa")
    cursor = conn.cursor()
    
    query = """
    SELECT * FROM dinosaurs WHERE 
    TRIM(nombre_comun) = TRIM(?) OR TRIM(nombre_cientifico) = TRIM(?)
    """
    cursor.execute(query, (nombre_dinosaurio.strip(), nombre_dinosaurio.strip()))
    
    row = cursor.fetchone()
    print(f"Buscando en la BD: '{nombre_dinosaurio.strip()}'")
    
    if row:
        columns = [column[0] for column in cursor.description]  # Obtener los nombres de las columnas
        dinosaur_info = dict(zip(columns, row))  # Convertir la fila en diccionario

       # Convertir Decimals a float
        for key, value in dinosaur_info.items():
            if isinstance(value, Decimal):
                dinosaur_info[key] = float(value)

        conn.close()
        return dinosaur_info
    else:
        conn.close()
        print("Dinosaurio No encontrado")
        return None
    