import base64
from io import BytesIO
from core.app import db
from core.models import Search
from sqlalchemy import or_, and_
from werkzeug.exceptions import HTTPException
from extract_dino_name.google_vision import detect_dinosaurs
from configModel import generar_respuesta
import random
import string


def get_searches(search: str, page: int, per_page: int):
    '''Get searches'''

    query = Search.status == 'ACTIVE'
    if search:
        query = and_(Search.status == 'ACTIVE',
                     or_(Search.prediction.ilike(f'%{search}%'),
                         Search.dinosaur.ilike(f'%{search}%')))

    return db.paginate(db.session.query(Search).filter(query),
                       page=page, per_page=per_page)


def get_search_by_id(search_id: int):
    '''Get search by search id'''

    return db.session.query(Search).filter(Search.id == search_id).first()


def check_search_exists(search_id: int):
    '''Check if search exists'''

    return db.session.query(Search).filter(Search.id == search_id).first()


def update_search(search_id: int, search_load):
    '''Update search'''

    if not check_search_exists(search_id):
        raise HTTPException('Search not found')

    db.session.merge(search_load)
    db.session.commit()


def delete_search(search_id: int):
    '''Delete search'''

    db.session.merge(Search(id=search_id, status='INACTIVE'))
    db.session.commit()


def generar_nombre_archivo(extension='png', longitud=12):
    caracteres = string.ascii_letters + string.digits  # a-zA-Z0-9
    nombre = ''.join(random.choices(caracteres, k=longitud))
    return f"{nombre}.{extension}"


def save_img(content):
    '''Save IMG'''

    filename = generar_nombre_archivo()
    try:
        with open(f'uploads/{filename}', 'wb+') as f:
            f.write(content.getbuffer())
    except Exception as ex:
        print('Error al intentar guardar la imagen')
        print(str(ex))

    return f'uploads/{filename}'


def process_photo(photo: str):
    '''Process photo'''

    img_bytes = BytesIO(base64.b64decode(photo))
    top_dinos = detect_dinosaurs(None, img_bytes)

    if top_dinos:
        print("Top 3 dinosaurios detectados")
        for i, dino in enumerate(top_dinos, start=1):
            tipos = ', '.join(dino['types'])
            print(
                f"{i}. {dino['name']} - Score: {dino['score']:.2f} (Tipos: {tipos})")

        dino_principal = top_dinos[0]['name']
        dino_score = top_dinos[0]['score']
        print(
            f"\nEl dinosaurio principal es: {dino_principal} con un score de {dino_score:.2f}\n")

        model_name = "gemma3:4b"
        prompt_global = f"Quiero información sobre el dinosaurio {dino_principal}"
        nombre_dino_api = dino_principal.title()

        response = generar_respuesta(
            model_name, prompt_global, nombre_dino_api, None)
        
        img_path = save_img(img_bytes)
        return response, img_path
    else:
        return "No se detectaron dinosaurios en la imagen.", None
