from apiflask import Schema, fields
from marshmallow import post_load
from core.models import Search
from core.schemas.utils import BaseSchema

class PhotoIn(BaseSchema):
    photo = fields.String()

class ImageIn(BaseSchema):
    image = fields.File()

class SearchInCreate(BaseSchema):
    dinasour = fields.String(required=False)
    prediction = fields.String()
    image_path = fields.String(required=False)

    @post_load
    def make_object(self, data, **kwargs):
        return Search(**data)


class ImageOut(BaseSchema):
    prediction = fields.String()
    img_path = fields.String(data_key='imgPath')


class SearchInUpdate(BaseSchema):
    id = fields.Integer()
    full_name = fields.String(data_key='fullName')
    email = fields.String()
    password = fields.String()
    status = fields.String(load_default='ACTIVE')

class SearchOut(BaseSchema):
    id = fields.Integer()
    full_name = fields.String(data_key='fullName')
    email = fields.String()
    status = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class SearchesOut(Schema):
    items = fields.List(fields.Nested(SearchOut))
