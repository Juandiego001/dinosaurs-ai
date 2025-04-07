""" 
Módulo para buscar información en fuentes adicionales sobre dinosaurios para el modelo Ollama
"""

import requests
from api_config.azure_conection import search_dinosaur_info

def buscar_paleobiodb(nombre_dinosaurio):
    """
    Función para encontrar información del dinosaurio en Paleobiology Database. 
    """
    url = f"https://paleobiodb.org/data1.2/taxa/single.json?name={nombre_dinosaurio}&show=full"
    response = requests.get(url, timeout=8)
    
    if response.status_code == 200:
        data = response.json()
        return data
    return f"No se encontró información de {nombre_dinosaurio} en Paleobiology Database."

def buscar_wikipedia(nombre_dinosaurio):
    """
    Función para encontrar información del dinosaruio en Wikipedia 
    """
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{nombre_dinosaurio}"
    response = requests.get(url, timeout=8)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("extract", "No se encontró información en Wikipedia.")
    return "No se encontró información en Wikipedia."

def buscar_database(nombre_dinosaurio):
    """
    Función para encontrar información del dinosaurio en la base de datos
    """
    dinosaur_info = search_dinosaur_info(nombre_dinosaurio)
    
    if dinosaur_info:
        return dinosaur_info
    return f"Información de {nombre_dinosaurio} no disponible en la Base de Datos."
