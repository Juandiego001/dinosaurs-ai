from core.app import db
from flask_jwt_extended import get_jwt_identity, jwt_required
from core.services import searches
from apiflask import APIBlueprint, abort
from core.schemas.utils import Message, Pagination
from core.schemas.searches import ImageOut, SearchInCreate, SearchInUpdate, SearchOut, SearchesOut, PhotoIn, ImageIn


bp = APIBlueprint('searches', __name__)


@bp.get('/')
@bp.input(Pagination, location='query')
@bp.output(SearchesOut)
def get_searches(query_data):
    '''Get searches'''

    try:
        return {'items': searches.get_searches(query_data['search'],
                                         query_data['page'],
                                         query_data['per_page'])}
    except Exception as ex:
        abort(500, str(ex))


@bp.get('/<int:search_id>')
@bp.output(SearchOut)
def get_search(search_id):
    '''Get search'''

    try:
        return searches.get_search_by_id(search_id)
    except Exception as ex:
        abort(500, str(ex))


@bp.post('/photo')
@bp.input(PhotoIn)
@bp.output(ImageOut)
def process_photo(json_data):
    '''Validate photo'''

    try:
        prediction, img_path = searches.process_photo(json_data['photo'].split(',')[1])
        return {'prediction': prediction, 'img_path': img_path}
    except Exception as ex:
        print(str(ex))
        abort(500, str(ex))


@bp.post('/save')
@jwt_required()
@bp.input(SearchInCreate, arg_name='search')
@bp.output(Message)
def create_search(search):
    '''Create search'''

    try:
        user_id = get_jwt_identity()
        search.user_id = user_id
        db.session.add(search)
        db.session.commit()
        return {'message': 'Search created successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(500, str(ex))


@bp.put('/<int:search_id>')
@bp.input(SearchInUpdate)
@bp.output(Message)
def update_searches(search_id, json_data):
    '''Update search'''
    try:
        searches.update_search(search_id, json_data)
        return {'message': 'search updated successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(500, str(ex))


@bp.delete('/<int:search_id>')
@bp.output(Message)
def delete_searches(search_id):
    '''Delete searches'''

    try:
        searches.delete_search(search_id)
        return {'message': 'search deleted successfuly'}
    except Exception as ex:
        print(str(ex))
        abort(500, str(ex))
