from core.services import dinosaurs
from apiflask import APIBlueprint, abort
from werkzeug.exceptions import HTTPException
from core.schemas.utils import Message, Pagination
from core.schemas.dinosaurs import DinosaurInUpdate, DinosaurOut, DinosaursOut


bp = APIBlueprint('dinosaurs', __name__)


@bp.get('/')
@bp.input(Pagination, location='query')
@bp.output(DinosaursOut)
def get_dinosaurs(query_data):
    '''Get dinosaurs'''

    try:
        return {'items': dinosaurs.get_dinosaurs(query_data['search'],
                                         query_data['page'],
                                         query_data['per_page'])}
    except Exception as ex:
        abort(500, str(ex))


@bp.get('/<int:dinosaur_id>')
@bp.output(DinosaurOut)
def get_user(dinosaur_id):
    '''Get dinosaur'''

    try:
        return dinosaurs.get_dinosaur_by_id(dinosaur_id)
    except Exception as ex:
        abort(500, str(ex))


@bp.put('/<int:dinosaur_id>')
@bp.input(DinosaurInUpdate)
@bp.output(Message)
def update_dinosaurs(dinosaur_id, json_data):
    '''Update dinosaur'''

    try:
        dinosaurs.update_dinosaur(dinosaur_id, json_data)
        return {'message': 'Dinosaur updated successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(500, str(ex))


@bp.delete('/<int:dinosaur_id>')
@bp.output(Message)
def delete_dinosaurs(dinosaur_id):
    '''Delete dinosaurs'''

    try:
        dinosaurs.delete_dinosaur(dinosaur_id)
        return {'message': 'Dinosaur deleted successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(500, str(ex))
