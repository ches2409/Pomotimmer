import reflex as rx
from sqlalchemy.exc import SQLAlchemyError

from gestor.database.database import SessionLocal
from gestor.database.models import Category
from gestor.db_utils import get_category_by_id

class CategoryState(rx.State):
    name:str=""
    description:str=""
    message:str=""
    categorias:list[Category]=[]
    selected_category_id:int |None=None

    @rx.event
    def set_name(self,value:str):
        self.name=value

    @rx.event
    def set_description(self,value:str):
        self.description=value

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
                self.message=f"✅ La categoria {category.name} fue creada con exito"
                self.name="" # Resetea el input
                self.description=""
        except SQLAlchemyError as e:
            self.message=f"❌ Error al crear la categoria {category.name}: {str(e)}"


    @rx.event
    def load_categories(self):
        with SessionLocal() as db:
            self.categorias=db.query(Category).all()