import requests
from openai import OpenAI
from dotenv import load_dotenv
import io
import cv2
import numpy as np
from PIL import Image
from tkinter import filedialog, messagebox

load_dotenv()

modeloTurbo = OpenAI(api_key="api_key")

def img_or_text_dinosaur():
    """
    Función para seleccionar si se desea buscar información de un dinosaurio por imagen o texto.
    """
    opcion = messagebox.askyesno("Dinosaurios", "¿Deseas buscar información de un dinosaurio por imagen?")
    if opcion:
        analizar_img()
    else:
        busqueda_openAI()

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
    """
    
    response = modeloTurbo.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": "Eres un paleontólogo experto que proporciona información precisa sobre dinosaurios, el cual puede brindar la información a detalle en cualquier idioma"},
            {"role": "user", "content": promptDinosaur}
        ],
        max_tokens = 500,
        temperature = 0.6
    )
    
    if response and hasattr(response.choices[0].message, "content"):
        dinosaurio_response = response.choices[0].message.content
        return dinosaurio_response
    return "No se pudo obtener información detallada del dinosaurio."

def analizar_img():
    """
    Función para analizar la imagen de un dinosaurio y obtener información del mismo.
    """
    img_dino = filedialog.askopenfilename(
        title="Selecciona la imagen del dinosaurio",
        filetypes=[(
            "Archivos de imagen",
            ("*.png", "*.jpg", "*.jpeg")
        )]
    )
    
    if img_dino:
        print(f"Archivo seleccionado {img_dino} analizando...")
        
        try:
            img = Image.open(img_dino)
            img.thumbnail((600, 600))
            
            dinosaurio_detectado = detectar_dinosaurio(img)
            
            if dinosaurio_detectado:
                messagebox.showinfo("Dinosaurio detectado", f"Se detectó el dinosaurio {dinosaurio_detectado} en la imagen.")
            else:
                messagebox.showinfo("Dinosaurio no detectado", "No se detectó ningún dinosaurio en la imagen.")
            
        except Exception as e:
            messagebox.showerror("Error", "No se pudo abrir la imagen seleccionada.")
    else:
        messagebox.showerror("Error", "No se seleccionó ninguna imagen.")
    
    
def detectar_dinosaurio(img):
    """
    Función para detectar el dinosaurio en la imagen.
    """
    api_key = ""
    model_url = ""
    
    dinosaurios_posibles = ["Tyrannosaurus", "Triceratops", "Velociraptor", "Brachiosaurus", "Stegosaurus", "Spinosaurus", "Ankylosaurus", "Diplodocus", "Pteranodon", "Allosaurus", "Achelousaurus", "Aardonyx", "Apatosaurus", "Avaceratops", "Dilophosaurus", "Dryosaurus", "Ceratosaurus", "Kotasaurus", "Allosaurus"]
    
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_bytes = img_byte_arr.getvalue()
    
    headers = {"Authorization": f"Bearer {api_key}"}
    files = {"file": img_bytes}
    data = {"inputs": dinosaurios_posibles}
    
    response = requests.post(model_url, headers=headers, files=files, data=data)
    
    if response.status_code == 200:
        result = response.json()
        print("Resultado del modelo:", result)
        
        nombre_dino = result.get("outputs", [])[0].get("dinosaurio")
        if nombre_dino:
            max_score = np.argmax(nombre_dino)
            nombre_dinosaurio = dinosaurios_posibles[max_score]
            busqueda_openAI(nombre_dinosaurio)
            
        else:
            print("Dinosaurio no detectado.")
            return None

    
print(img_or_text_dinosaur())


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