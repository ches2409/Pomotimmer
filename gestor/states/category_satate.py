import reflex as rx
from sqlalchemy.exc import SQLAlchemyError

from gestor.logger import logger

from gestor.database.database import SessionLocal
from gestor.database.models import Category,Task


class CategoryState(rx.State):
    # Inputs del formulario
    name:str=""
    description:str=""
    temp_id:int=0

    # Mensaje de feedback
    message:str=""

    # Listado de categorias
    categories:list[dict]=[]

    # Diccionario con los datos de la categoria
    selected_category:dict={} #Crea una variable de estado para almacenar resultados de un objeto

    #Asignacion de valores
    @rx.event
    def set_name(self,value:str):
        self.name=value

    @rx.event
    def set_description(self,value:str):
        self.description=value

    @rx.event
    def set_temp_id(self,value:str):
        self.temp_id=int(value) if value.isdigit() else 0

    # CRUD de categorias

    @rx.event
    def create_category(self):
        if not self.name.strip():
            self.message="❌ El nombre no puede estar vacio"
            return
        try:
            with SessionLocal() as db:
                category = Category(name=self.name.strip(),description=self.description)
                db.add(category)
                db.commit()
                db.refresh(category)

                # Limpiar inputs y mostrar mensaje
                self.message=f"✅ La categoria {category.name} fue creada con exito"
                logger.info(f"Se creo una categoria: {category.name}")

                self.name="" # Resetea el input
                self.description=""

                # Opcional: refrescar la lista
                self.get_all_categories()

        except SQLAlchemyError as e:
            self.message=f"❌ Error al crear la categoria {category.name}: {str(e)}"


    @rx.event
    def get_all_categories(self):
        with SessionLocal() as db:
            result=db.query(Category).all()

            self.categories=[
                {"id":cat.id, "name":cat.name, "description":cat.description}
                for cat in result
            ]

    @rx.event
    def get_category_by_id(self,category_id:int):
        with SessionLocal() as db:
            try:
                category=db.get(Category,category_id)
                if category:
                    self.selected_category={
                        "id":category.id,
                        "name":category.name,
                        "description":category.description
                    }
                else:
                    self.selected_category={}
            except Exception as e:
                logger.error(f"❌ Error al obtener la categoria: {str(e)}")
                self.selected_category={}

    @rx.event
    def update_category(self,category_id:int):
        with SessionLocal() as db:

            try:
                category = db.get(Category, category_id)
                if category:

                    self.categories=[
                        {"id":cat.id,"name":cat.name,"description":cat.description}
                        for cat in db.query(Category).all()
                    ]
                    categories_names=[]
                    for c in self.categories:
                        categories_names.append(c["name"])

                    if self.name not in categories_names:
                        if self.name.strip():
                            category.name=self.name.strip()
                            logger.info(f"Nombre de categoria cambiado: {category.name}")
                        if self.description.strip():
                            category.description=self.description.strip()
                            logger.info(f"Descripcion de categoria cambiada: {category.description}")
                        db.commit()
                        db.refresh(category)

                        self.message = f"✅ La categoria {category.name} fue Actualizada con exito"
                    else:
                        self.message=f"❌ La categoria {self.name} ya existe, no se guardan cambios"
                        logger.warning(f"Duplicado detectado: {self.name}")

                # Limpiar inputs
                self.name = ""  # Resetea el input
                self.description = ""
            except Exception as e:
                self.message=f"❌ Error al obtener la categoria: {type(e).__name__}"
                logger.error(f"Error al obtener la categoria: {str(e)}")

    @rx.event
    def delete_category(self, category_id:int):
        with SessionLocal() as db:

            try:
                # Buscar categoria
                category = db.get(Category, category_id)

                if not category:
                    self.message = f"❌ No se encuentra {category_id}"
                    logger.warning(f"categoria: {category_id} no encontrada para borrar")
                    return

                # Verificar si existen tareas asociadas
                has_tasks=db.query(Task).filter_by(category_id=category_id).first()

                if has_tasks:
                    self.message=f"No se puede eliminar la categoria {category.name} porque tiene tareas asociadas"
                    logger.warning(f"intento de borrado de categoria '{category.name}' con tareas asociadas")
                    return

                # Eliminar categoria
                db.delete(category)
                db.commit()

                self.message = f"✅ Se ha borrado la categoria ({category.name}) exitosamente"
                logger.info(f"categoria {category_id} - {category.name} borrada")

                # Actualizar la lista
                self.get_all_categories()

            except SQLAlchemyError as e:
                self.message=("❌ Error de la base de datos al eliminar")
                logger.error(f"Error en la BD al eliminar '{category_id}': {type(e).__name__} - {str(e)}")
            except Exception as e:
                self.message="❌ Error inesperado al Eliminar categoria"
                logger.error(f"Error inseperado en delete_category: {e}")


