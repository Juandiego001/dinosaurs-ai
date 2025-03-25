import requests
from openai import OpenAI

modeloTurbo = OpenAI(api_key="API_KEY")

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
  
# ! No es una API, no devuelve JSON. Pensar en web scrapping  
# def buscar_naturalmuseum(nombre_dinosaurio):
#     """
#     Función para encontrar información del dinosaruio en el Museo Natural de Historia Londres 
#     """
#     url = f"https://www.nhm.ac.uk/discover/dino-directory/{nombre_dinosaurio}.html"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         return data.get("description", "No se encontró información en el Museo de Historia Natural.")
#     return "No se encontró información en el Museo de Historia Natural."

def busqueda_openAI(nombre_paleontologico):
    """
    Configuración del modelo AI para brindar la respuesta al usuario con la información detallada del dinosaurio.
    """
    info_dinof1 = buscar_paleobiodb(nombre_paleontologico)
    info_dinof2 = buscar_wikipedia(nombre_paleontologico)
    
    promptDinosaur = f"""
    Investiga a detalle información sobre el dinosaurio {nombre_paleontologico}.
    Con base la siguiente información obtenida de 3 fuentes:
    Descripción de Paleobiology Database: {info_dinof1},
    Descripción de wikipedia: {info_dinof2}, 
    
    Con base en la información detallada del dinosaurio, 
    organizalá en la siguiente estructura:
    {{
        "nombre_cientifico": "",
        "nombre_comun": "",
        "periodo": "",
        "habitat": "",
        "dieta": "",
        "longitud en metros y pies": "",
        "peso_estimado en kilogramos y libras": "",
        "descripcion": "",
        "clasificacion": {{
            "orden": "",
            "familia": "",
            "genero": "",
            "especie": "",
        }},
        "curiosidades": []
    }}
    """;
    
    response = modeloTurbo.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": "Eres un paleontólogo experto que proporciona información precisa sobre dinosaurios, el cual puede brindar la información a detalle en cualquier idioma"},
            {"role": "user", "content": promptDinosaur}
        ],
        max_tokens = 700,
        temperature = 0.7
    )
    
    if response and hasattr(response.choices[0].message, "content"):
        dinosaurio_response = response.choices[0].message.content
        return dinosaurio_response
    return "No se pudo obtener información detallada del dinosaurio."
    
print(busqueda_openAI("Tyrannosaurus"))
    
# from google.cloud import vision

# # Crea un cliente de Vision API
# client = vision.ImageAnnotatorClient()

# # Carga una imagen
# with open("imagen.jpg", "rb") as image_file:
#     content = image_file.read()

# image = vision.Image(content=content)

# # Analiza la imagen y obtiene etiquetas
# response = client.label_detection(image=image)
# labels = response.label_annotations

# # Muestra las etiquetas detectadas
# for label in labels:
#     print(label.description, label.score)