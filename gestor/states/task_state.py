import uuid

import reflex as rx
from sqlalchemy.exc import SQLAlchemyError

from gestor.logger import logger

from gestor.database.database import SessionLocal
from gestor.database.models import Task

class TaskState(rx.State):
    # Inputs del fomulario
    title:str=""
    description_task:str=""
    completed:bool=False
    temp_id:int=0

    message:str=""

    # Asignacion de valores
    @rx.event
    def set_title(self,value:str):
        self.title = value

    @rx.event
    def set_description(self,value:str):
        self.description_task=value

    @rx.event
    def set_completed(self,value:bool):
        self.completed = value

    @rx.event
    def set_temp_id(self,value:str):
        self.temp_id = int(value) if value.isdigit() else 0


    @rx.event
    def create_task(self):

        if not self.title.strip():
            self.message="El campo del nombre de la tarea no debe estar vacio"
            logger.error("Se intento crear una tarea sin titulo")
            return
        if not self.description_task.strip():
            self.message="Completa el campo de la descripcion"
            logger.error("Tarea sin descripcion al crear")
            return
        if self.temp_id == 0:
            self.message="Es obligatorio que la tarea pertenezca a una categoria"
            logger.error("Se intento crear una tarea sin ID de categoria")
            return



        with SessionLocal() as session:
            task=Task(title=self.title.strip(), description=self.description_task, category_id=self.temp_id)
            session.add(task)
            session.commit()
            session.refresh(task)

            logger.info(f"Se ha creado una tarea: {self.title} - {self.description_task}")
            self.message=f"Has creado la tarea: {self.title} - {self.description_task}, con exito"