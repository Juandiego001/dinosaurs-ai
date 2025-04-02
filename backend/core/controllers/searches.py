from apiflask import APIBlueprint


bp = APIBlueprint('searches', __name__)


@bp.get('/')
def get_users():
    '''Get searches'''
    pass


@bp.post('/')
def create_users():
    '''Create searches'''
    pass


@bp.put('/')
def update_users():
    '''Update searches'''
    pass


@bp.delete('/')
def delete_users():
    '''Delete searches'''
    pass