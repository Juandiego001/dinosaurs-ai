import requests
import json
import os
from openai import OpenAI

modeloTurbo = OpenAI(api_key="API_KEY")

def busqueda_openAI(nombre_paleontologico):
    
    promptDinosaur = f"""
    Investiga a detalle información sobre el dinosaurio {nombre_paleontologico}.
    Con base en tú busqueda, genera información detallada sobre el dinosaurio {nombre_paleontologico} siguiendo de apoyo esta estructura:
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
    else:
        return "No se pudo obtener información detallada del dinosaurio."
    
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