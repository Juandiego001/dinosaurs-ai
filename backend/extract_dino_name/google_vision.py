import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from google.cloud import vision
import os
from configModel import generar_respuesta
from dinosaurs_list import dinosaurs_list

# Configurar credenciales
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "regal-bonito-455502-e9-08bbdf4eebc3.json"

# Pesos para cada tipo de detección
TYPE_WEIGHTS = {
    'object': 1.3,
    'label': 1.0,
    'web_entity': 1.1
}

# Lista ampliada de términos relacionados con dinosaurios
DINOSAUR_TERMS = dinosaurs_list

DINOSAUR_TERMS_SET = set(name.lower() for name in DINOSAUR_TERMS)

def is_dinosaur(obj_name):
    """Verifica si el nombre detectado es un dinosaurio conocido"""
    lower_name = obj_name.lower()
    return any(term.lower() in lower_name for term in DINOSAUR_TERMS)


def detect_dinosaurs(image_path, image_bin=False):
    """Detecta dinosaurios y calcula puntuación ponderada"""
    client = vision.ImageAnnotatorClient()
    
    if image_path:
        with open(image_path, "rb") as image_file:
            content = image_file.read()
    elif image_bin:
        content = image_bin.read()
    
    image = vision.Image(content=content)
    
    response = client.annotate_image({
        'image': image,
        'features': [
            {'type_': vision.Feature.Type.OBJECT_LOCALIZATION},
            {'type_': vision.Feature.Type.LABEL_DETECTION},
            {'type_': vision.Feature.Type.WEB_DETECTION}
        ]
    })
    
    dinosaurs = []

    # 1. Objetos
    for obj in response.localized_object_annotations:
        if is_dinosaur(obj.name):
            dinosaurs.append({
                'type': 'object',
                'name': obj.name,
                'confidence': obj.score
            })

    # 2. Etiquetas
    for label in response.label_annotations:
        if is_dinosaur(label.description) and label.score > 0.7:
            dinosaurs.append({
                'type': 'label',
                'name': label.description,
                'confidence': label.score
            })

    # 3. Web entities
    if response.web_detection:
        for entity in response.web_detection.web_entities:
            if is_dinosaur(entity.description) and entity.score > 0.7:
                dinosaurs.append({
                    'type': 'web_entity',
                    'name': entity.description,
                    'confidence': entity.score
                })

    # Calcular puntaje ponderado
    for dino in dinosaurs:
        weight = TYPE_WEIGHTS.get(dino['type'], 1.0)
        dino['weighted_score'] = dino['confidence'] * weight

    # Agrupar por nombre y sumar scores si hay repeticiones
    aggregated = {}
    for dino in dinosaurs:
        name = dino['name'].lower()
        if name not in aggregated:
            aggregated[name] = {
                'name': dino['name'],
                'score': dino['weighted_score'],
                'types': {dino['type']}
            }
        else:
            aggregated[name]['score'] += dino['weighted_score']
            aggregated[name]['types'].add(dino['type'])

    # Convertir y ordenar
    sorted_dinos = sorted(aggregated.values(), key=lambda x: x['score'], reverse=True)

    return sorted_dinos[:3]

# Ejemplo de uso
if __name__ == "__main__":
    image_path = "backend/extract_dino_name/spinosaurus2.jpg"
    top_dinos = detect_dinosaurs(image_path)
    
    if top_dinos:
        print("Top 3 dinosaurios detectados")
        for i, dino in enumerate(top_dinos, start=1):
            tipos = ', '.join(dino['types'])
            print(f"{i}. {dino['name']} - Score: {dino['score']:.2f} (Tipos: {tipos})")
        
        dino_principal = top_dinos[0]['name']
        dino_score = top_dinos[0]['score']
        print(f"\nEl dinosaurio principal es: {dino_principal} con un score de {dino_score:.2f}\n")
        
        model_name = "gemma3:4b"
        prompt_global = f"Quiero información sobre el dinosaurio {dino_principal}"
        nombre_dino_api = dino_principal.title()
        ruta_img = image_path
        
        response = generar_respuesta(model_name, prompt_global, nombre_dino_api, image_path)
        print(f"Respuesta modelo: {response}")
    else:
        print("No se detectaron dinosaurios en la imagen.")



