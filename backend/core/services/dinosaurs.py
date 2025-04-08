from core.app import db
from core.models import Dinosaur
from sqlalchemy import or_, and_, asc
from werkzeug.exceptions import HTTPException


def get_dinosaurs(search: str, page: int, per_page: int):
    '''Get dinosaurs'''

    if search:
        query = or_(Dinosaur.nombre_cientifico.ilike(f'%{search}%'),
                    Dinosaur.nombre_comun.ilike(f'%{search}%'),
                    Dinosaur.clasificacion_familia.ilike(f'%{search}%'),
                    Dinosaur.clasificacion_genero.ilike(f'%{search}%'),
                    Dinosaur.clasificacion_especie.ilike(f'%{search}%'))

        return db.paginate(db.session.query(Dinosaur).filter(query).order_by(asc(Dinosaur.id)),
                       page=page, per_page=per_page)

    return db.paginate(db.session.query(Dinosaur).order_by(asc(Dinosaur.id)),
                    page=page, per_page=per_page)


def get_dinosaur_by_id(dinosaur_id: int):
    '''Get dinosaur by dinosaur id'''

    return db.session.query(Dinosaur).filter(Dinosaur.id == dinosaur_id).first()


def check_dinosaur_exists(dinosaur_id: int):
    '''Check if dinosaur exists'''

    return db.session.query(Dinosaur).filter(Dinosaur.id == dinosaur_id).first()


def update_dinosaur(dinosaur_id: int, dinosaur_load):
    '''Update dinosaur'''

    if not check_dinosaur_exists(dinosaur_id):
        raise HTTPException('Dinosaur not found')

    db.session.merge(dinosaur_load)
    db.session.commit()


def delete_dinosaur(dinosaur_id: int):
    '''Delete dinosaur'''

    db.session.merge(Dinosaur(id=dinosaur_id, status='INACTIVE'))
    db.session.commit()
