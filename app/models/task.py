from peewee import (
    Database, SqliteDatabase, Model,
    CharField, DateField, BooleanField,
    ForeignKeyField, TextField, IntegerField)
from account import User, BaseModel



class Tasks(BaseModel):
    user_id = ForeignKeyField(User, backref='users') # Chave estrangeira dos Users
    title = CharField(default='Task title') # Titulo da tarefa
    descr = TextField(default='Task description') # Descrição da taréfa
    category = CharField(default='Task') # Categoria da taréfa
    status = IntegerField(default=0) # 0= Pendente, 1= Em andamento, 2= Conclúida
    due_data = DateField() # Data de vencimento da tarefa
    created_at = DateField() # Data de criação da tarefa
    updated_at = DateField() # Data de última modificação da tarefa
    completed_ate = DateField() # Data de conclusão da tarefa (Caso seja concluida)
    recurring = BooleanField(default=0) # 0=Dia, 1=Semana, 2=Mês
    recurring_until = DateField() # Data de limite para tarefa

class Tasks_History(BaseModel):
    task_id = ForeignKeyField(Tasks, backref='tasks') # Key estrangeira Tasks
    user_id = ForeignKeyField(User, backref='users') # Key estrangeria Users
    status_before = IntegerField(default=0) # Status da tarefa antes de ser (0=Pendente,1=Em andamento,2=Concluida)
    status_after = IntegerField(default=0) # Status atual da tarefa (0=Pendente,1=Em andamento,2=Concluida)
    action_type = IntegerField(default=0) # Tipo de ação registrada (0=Pendente,1=Em andamento,2=Concluida)
    timestamp = DateField() # Data e hora da ação registrada
