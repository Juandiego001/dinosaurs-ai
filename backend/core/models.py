from core.app import db
from bcrypt import checkpw
from sqlalchemy import BigInteger, Float, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(450), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String(20), 
                                        nullable=False,
                                        default='ACTIVE')
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now(),
        onupdate=lambda: datetime.now())
    user_groups = relationship('UserGroup', back_populates='user')

    def check_password(self, in_pw, db_pw):
        return checkpw(in_pw, db_pw)


class Group(db.Model):
    __tablename__ = 'groups'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    status: Mapped[str] = mapped_column(String(20), 
                                        nullable=False,
                                        default='ACTIVE')
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now(),
        onupdate=lambda: datetime.now())
    user_groups = relationship('UserGroup', back_populates='group')


class UserGroup(db.Model):
    __tablename__ = 'user_groups'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id'))
    user = relationship('User', back_populates='user_groups')
    group = relationship('Group', back_populates='user_groups')


class Module(db.Model):
    __tablename__ = 'modules'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    status: Mapped[str] = mapped_column(String(20), 
                                        nullable=False,
                                        default='ACTIVE')
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now(),
        onupdate=lambda: datetime.now())


class Permission(db.Model):
    __tablename__ = 'permissions'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id'), nullable=False)
    module_id: Mapped[int] = mapped_column(ForeignKey('modules.id'), nullable=False)
    read: Mapped[bool] = mapped_column()
    create: Mapped[bool]
    update: Mapped[bool]
    delete: Mapped[bool]
    status: Mapped[str] = mapped_column(String(20), 
                                        nullable=False,
                                        default='ACTIVE')
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now(),
        onupdate=lambda: datetime.now())

class Dinosaur(db.Model):
    __bind_key__ = 'mssql'
    __tablename__ = 'dinosaurs'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    nombre_cientifico: Mapped[str] = mapped_column(String(255))
    nombre_comun: Mapped[str] = mapped_column(String(255))
    periodo: Mapped[str] = mapped_column(String(100))
    habitat: Mapped[str] = mapped_column(String)
    dieta: Mapped[str] = mapped_column(String)
    longitud_metros: Mapped[float] = mapped_column(Float)
    longitud_pies: Mapped[float] = mapped_column(Float)
    peso_kg: Mapped[float] = mapped_column(Float)
    peso_lb: Mapped[float] = mapped_column(Float)
    descripcion: Mapped[str] = mapped_column(String)
    clasificacion_orden: Mapped[str] = mapped_column(String(100))
    clasificacion_familia: Mapped[str] = mapped_column(String(100))
    clasificacion_genero: Mapped[str] = mapped_column(String(100))
    clasificacion_especie: Mapped[str] = mapped_column(String(100))
    curiosidades: Mapped[str] = mapped_column(String)

class Search(db.Model):
    __tablename__ = 'searches'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    dinosaur: Mapped[str] = mapped_column(String(255), nullable=True)
    img_path: Mapped[str] = mapped_column(String(255), nullable=True)
    prediction: Mapped[str] = mapped_column(String, nullable=True)
    status: Mapped[str] = mapped_column(String(20), 
                                        nullable=False,
                                        default='ACTIVE')
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now(),
        onupdate=lambda: datetime.now())