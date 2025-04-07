from searchModel import buscar_paleobiodb, buscar_wikipedia, buscar_database
import ollama
import re
from dinosaurs_list import dinosaurs_list

options = {
    "temperature": 0.5,
    "stop": None,
    "frequency_penalty": 1,
    "max_tokens": 80,
}

def generate_response(model_name, prompt):
    """ Genera una respuesta utilizando un modelo de Ollama. """
    llm_output = ollama.chat(
        model=model_name,
        messages=[
            {"role": "user", "content": prompt},
            {"role": "system", "content": "Eres un paleontólogo experto que proporciona información precisa sobre dinosaurios, el cual puede brindar la información a detalle en cualquier idioma"}
        ],
        options= options,
        format = "json",        
        )
    return llm_output['message']['content']
    
def generar_respuesta(model_name, nombre_paleontologico, nombre_dino_api):
    """Genera información sobre dinosaurios con el modelo de IA"""

    # Buscar información en distintas fuentes
    info_dino1 = buscar_wikipedia(nombre_dino_api)
    info_dino2 = buscar_database(nombre_dino_api)
    info_dino3 = buscar_paleobiodb(nombre_dino_api)

    # Crear el prompt para el modelo
    prompt_dinosaur = f"""
    Investiga a detalle información sobre el dinosaurio {nombre_paleontologico}. 
    Usa tus conocimientos y la información obtenida de Wikipedia como información adicional:
    - Extracto de Wikipedia: {info_dino1}
    - Extracto de Base de Datos propia: {info_dino2}
    - Extracto de Paleobiodb: {info_dino3}

    Asegúrate de usar la siguiente información para crear una respuesta en formato JSON:
    - Organiza los datos ya sea en español o en inglés, según lo que pida el usuario.
    - Para la longitud y el peso estimado, proporciona tanto el sistema internacional de medidas (metros y kilogramos) como las unidades estadounidenses (pies y libras).
    - 1 pie = 0.3048 metros
    - 1 kilogramo = 2.20 libras

    Devuelve estos datos estructurados en formato JSON:
    {{
        "nombre_cientifico": "",
        "nombre_comun": "",
        "periodo": "Período geológico",
        "habitat": "Descripción del hábitat",
        "dieta": "(carnívoro, herbívoro, etc.)",
        "longitud": "",
        "peso_estimado": "",
        "descripcion": "Descripción detallada incluyendo información de Wikipedia y otras fuentes científicas",
        "clasificacion": {{
            "orden": "",
            "familia": "",
            "genero": "",
            "especie": ""
        }},
        "curiosidades": ["Curiosidad 1", "Curiosidad 2"],
        "recursos": [
            "Procura que los recursos no sean páginas 404 ERROR, brinda enlaces verídicos. Además de brindar como recurso Wikipedia siguiendo la estructura de los siguientes URLs"
            "URL de Wikipedia: https://en.wikipedia.org/wiki/{nombre_dino_api}",
            "URL de summary Wikipedia: https://en.wikipedia.org/api/rest_v1/page/summary/{nombre_dino_api}",
            "Usa recursos como paleobiodb.org que brinda mayor soporte y estructura a tu respuesta, con enlaces validos como: https://paleobiodb.org/data1.2/taxa/single.json?name={nombre_dino_api}&show=full",
            "Recursos científicos adicionales o enlaces (si están disponibles)"
        ],
        "uso_de_wikipedia": "Indica explícitamente si se utilizó Wikipedia {info_dino1} o no como fuente."
        "uso_de_BD_info_dino2": "Indica explícitamente si se utilizó la Base de datos {info_dino2} o no como fuente."
        "uso_paleobiodb": "Indica explícitamente si se utilizó Paleobiodb {info_dino3} o no como fuente."
    }}

    Si no encontraste información detallada en Wikipedia, menciona otros recursos confiables como bases de datos científicas o artículos. Asegúrate de incluir todas las fuentes relevantes.
    """
    respuesta = generate_response(model_name, prompt_dinosaur)
    return respuesta

if __name__ == "__main__":
    # * Modelo de Ollama usado
    model_name = "gemma3:4b"  
    
    # * Usando Regular Expressions para extraer nombre Dino para APIS
    nombre_dino = input("Cuentame que quieres aprender hoy?: ").lower()
    pattern = r"\b(" + "|".join(dino.lower() for dino in dinosaurs_list) + r")\b"
    match = re.search(pattern, nombre_dino)

    if match:
        nombre_dino_api = match.group(0).title()  # Lo devuelve con la primera letra en mayúscula
        print(f"Dinosaurio detectado: {nombre_dino_api}")
    else:
        print("No se encontró un dinosaurio en la oración.")
    
    if nombre_dino_api:
        response = generar_respuesta(model_name, nombre_dino, nombre_dino_api)
        print("Respuesta del modelo:", response)
    else:
        print("No se pudo generar la respuesta.")
    