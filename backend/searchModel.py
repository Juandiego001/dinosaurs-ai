import requests

def buscar_paleobiodb(nombre_dinosaurio):
    """
    Función para encontrar información del dinosaurio en Paleobiology Database. 
    """
    url = f"https://paleobiodb.org/data1.2/taxa/single.json?name={nombre_dinosaurio}&show=full"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    return f"No se encontró información de {nombre_dinosaurio} en Paleobiology Database."


def buscar_wikipedia(nombre_dinosaurio):
    """
    Función para encontrar información del dinosaruio en Wikipedia 
    """
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{nombre_dinosaurio}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("extract", "No se encontró información en Wikipedia.")
    return "No se encontró información en Wikipedia."

## * Agregar la BD a partir de la información del Museo
def buscar_DB(nombre_dinosaurio):
    """
    Función para encontrar información del dinosaurio en la base de datos
    """
    url = f""
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("información", "No se encontró información en la base de datos.")
    
    return f"Información de {nombre_dinosaurio} no disponible en la base de datos."