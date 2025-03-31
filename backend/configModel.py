from searchModel import buscar_paleobiodb, buscar_wikipedia
import ollama

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
    
def generar_respuesta(model_name, nombre_paleontologico):
    """Genera información sobre dinosaurios con el modelo de IA"""

    # Buscar información en distintas fuentes
    info_dino2 = buscar_wikipedia(nombre_paleontologico)

    # Crear el prompt para el modelo
    promptDinosaur = f"""
    Investiga a detalle información sobre el dinosaurio {nombre_paleontologico}.
    Con base en la información obtenida, de tus conocimientos y de lo obtenido en wikipedia:
    - Resultados de wikipedia: {info_dino2}

    Organiza la información en español o inglés, depende de como te pregunte el usuario para todas las respuestas en este formato JSON.
    Para la parte de longitud y peso estimado brinda el Sistema Internacional de Medida estadounidense y colombiano, en el caso de longitud brindar en metros y libras el resultado y para el caso de peso_estimado, brindar en kilogramos y libros. Sus conversiones son así:
    - 1 pie = 0.3048 metros
    - 1 kilogramo = 2.20 libras
    Recuerda, simplemente la información necesaria para completar cada campo del JSON:
    {{
        "nombre_cientifico": "",
        "nombre_comun": "",
        "periodo": "",
        "habitat": "",
        "dieta": "",
        "longitud": "",
        "peso_estimado": "",
        "descripcion": "",
        "clasificacion": {{
            "orden": "",
            "familia": "",
            "genero": "",
            "especie": ""
        }},
        "curiosidades": []
    }}
    """

    # Hacer la consulta al modelo
    respuesta = generate_response(model_name, promptDinosaur)
    return respuesta

if __name__ == "__main__":
    model_name = "gemma3:4b"  
    
    # Generar una respuesta
    nombre_dino = "Me gustaría saber información del Euoplocephalus tutus"
    response = generar_respuesta(model_name, nombre_dino)
    
    print("Respuesta del modelo:", response)
    