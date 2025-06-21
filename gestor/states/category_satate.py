import reflex as rx
from sqlalchemy.exc import SQLAlchemyError

from gestor.database.database import SessionLocal
from gestor.database.models import Category

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
                print(f"❌ Error al obtener la categoria: {str(e)}")
                self.selected_category={}

    @rx.event
    def update_category(self,category_id:int):
        self.name=""
        self.description=""
        with SessionLocal() as db:

            try:
                category = db.get(Category, category_id)
                if category:
                    if self.name.strip():
                        category.name=self.name.strip()
                        print(f"Nombre de categoria cambiado: {category.name}")
                    if self.description.strip():
                        category.description=self.description.strip()
                        print(f"Descripcion de categoria cambiada: {category.description}")
                db.commit()
            except Exception as e:
                self.message=f"❌ Error al obtener la categoria: {str(e)}"


