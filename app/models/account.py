from peewee import (
    Database, SqliteDatabase, Model,
    CharField, DateField, BooleanField,
    ForeignKeyField, TextField, IntegerField)
from dotenv import find_dotenv, load_dotenv
from os import getenv

# Carrega as variáveis de ambiente
load_dotenv(find_dotenv())

# Função para inicializar o banco de dados
def initialize_db() -> Database:
    db_name = getenv('DB_NAME', 'databasetasks.db')
    return SqliteDatabase(db_name)

db: Database = initialize_db()

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True) # Name Users
    email = CharField(unique=True) # Address Users
    password = CharField() # Passwords Users
    created_at = DateField() # Data e hora que foi criado
    update_at = DateField() # Último momento online
    is_active = BooleanField(default=False) # User esta ativo? False=Não, True=Sim
    is_admin = BooleanField(default=False) # User é um admin? False=Não, True=Sim


class Email_Verific(BaseModel):
    user_id = ForeignKeyField(User, backref='users') # Key Estrangeria Users
    verific_code = CharField(unique=True) # Código de verificação
    created_at = DateField() # Data de criação do código
    expires_ate = DateField() # Dta de expiração do código
    is_verified = BooleanField(default=False) # Código verificado ou não? False=Não, True=Sim

class Sessions(BaseModel):
    user_id = ForeignKeyField(User, backref='users') # Key Estrangeria Users
    session_token = CharField(unique=True) # Token único  de sessão gerado no login
    created_at = DateField() # Data de criação da sessão
    expires_ate = DateField() # Dta de expiração do sessão
    is_active = BooleanField(default=False) # User esta ativo? False=Não,True=Sim
    