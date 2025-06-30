
import reflex as rx
from gestor.logger import logger

from gestor.database.database import SessionLocal
from gestor.database.models import Task
from gestor.utils import fetch_all_categories, fetch_all_tasks


class TaskState(rx.State):
    # Inputs del fomulario
    title:str=""
    description_task:str=""
    completed:bool=False
    category_id:int=0
    temp_id:int=0

    message:str=""

    #Listado de tareas
    tasks:list[dict]=[]

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
    def set_category_id(self,value:str):
        self.category_id=int(value) if value.isdigit() else 0

    @rx.event
    def set_temp_id(self,value:str):
        self.temp_id = int(value) if value.isdigit() else 0


    @rx.event
    def create_task(self):
        """
        Crea una nueva tarea con su respectiva categoria.

        Valida que el titulo, la descripcion y la categoria no esten vacios.
        Comprueba que el id de la categoria exista en la tabla de categorias.
        Si la validacion falla, asigna un mensaje de error a self.message y registra el error.
        si la tarea se crea correctamente, limpia los campos del formulario y asigna un mensaje de exito.

        :return: None
        Side Effects:
            - Modifica self.message con el resultado de la operacion.
            - Limpia self.title, self.description_task, y self.category_id si la tarea se crea correctamente.
            - Registra eventos en el logger.
        """

        if not self.title.strip():
            self.message="El campo del nombre de la tarea no debe estar vacio"
            logger.error("Se intento crear una tarea sin titulo")
            return
        if not self.description_task.strip():
            self.message="Completa el campo de la descripcion"
            logger.error("Tarea sin descripcion al crear")
            return
        if self.category_id == 0:
            self.message="Es obligatorio que la tarea pertenezca a una categoria"
            logger.error("Se intento crear una tarea sin ID de categoria")
            return

        all_categories = fetch_all_categories()

        existst_category = next(
            (c for c in all_categories if c.id == self.category_id),
            None
        )
        if existst_category:

            with SessionLocal() as session:
                task=Task(title=self.title.strip(), description=self.description_task, category_id=self.category_id)


                if self.category_id:

                    session.add(task)
                    session.commit()
                    session.refresh(task)

                    logger.info(f"Se ha creado una tarea: {self.title} - {self.description_task}")
                    self.message=f"Has creado la tarea: {self.title} - {self.description_task}, con éxito"

                    self.title=""
                    self.description_task=""
                    self.category_id=0
        else:
            logger.warning(f"No se creo la tarea, ID de categoria ({self.category_id}) no existe")
            self.message=f"No se creo la tarea, La categoria ({self.category_id}) no existe"
            self.category_id=0

    @rx.event
    def get_all_tasks(self):
        all_tasks=fetch_all_tasks()

        self.tasks=[
            {"id":t.id_task, "name":t.title, "description":t.description,"categoria_id":t.category_id}
            for t in all_tasks
        ]