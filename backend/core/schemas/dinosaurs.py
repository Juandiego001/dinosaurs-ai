from apiflask import fields
from core.schemas.utils import BaseSchema

class Dinosaur(BaseSchema):
    nombre_cientifico = fields.String(data_key='nombreCientifico')
    nombre_comun = fields.String(data_key='nombreComun')
    periodo = fields.String()
    habitat = fields.String()
    dieta = fields.String()
    longitud_metros = fields.String(data_key='longitudMetros')
    longitud_pies = fields.String(data_key='longitudPies')
    peso_kg = fields.String(data_key='pesoKg')
    peso_lb = fields.String(data_key='pesoLb')
    descripcion = fields.String()
    clasificacion_orden = fields.String(data_key='clasificacionOrden')
    clasificacion_familia = fields.String(data_key='clasificacionFamilia')
    clasificacion_genero = fields.String(data_key='clasificacionGenero')
    clasificacion_especie = fields.String(data_key='clasificacionEspecie')
    curiosidades = fields.String()


class DinosaurInUpdate(Dinosaur):
    id = fields.Integer()


class DinosaurOut(Dinosaur):
    id = fields.Integer()


class DinosaursOut(BaseSchema):
    items = fields.List(fields.Nested(DinosaurOut))
    