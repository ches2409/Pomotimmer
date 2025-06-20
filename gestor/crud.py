from typing import List

from sqlalchemy.orm import Session

from gestor.database.database import SessionLocal
from gestor.database.models import Category

# --------------------------------
# Utils
# --------------------------------

def get_session()->Session:
    return SessionLocal()
# --------------------------------
# CRUD - Category
# --------------------------------
def create_category(name:str,description:str)->Category:
    """
    Crea una nueva categoria.
    :param name: Nombre del categoria
    :param description: Descripcion del categoria
    :return: Category object
    """
    with SessionLocal() as db:
        category=Category(name=name,description=description)
        db.add(category)
        db.commit()
        db.refresh(category)
        print(f"✅ Categoria creada - {category.name}")
        return category

# def get_all_categories():
#     with SessionLocal() as db:
#         categories=db.query(Category).all()
#         return categories

def get_all_categories()->List[Category]:
    """Obtiene todos las categorias en la base de datos
    :return: Lista de categorias
    """
    with SessionLocal() as db:
        return db.query(Category).all()

def get_category_by_id(id:int=None):
    if id is None:
        print(f"❌ no puede estar vacio")
        return None

    with SessionLocal() as db:
        category=db.get(Category,id)
        if not category:
            print(f"❌ Error: No se encuentra la categoria con ID {id}")
            return None

        print(f"La categoria ({category.id}) es: {category.name}")
        return category
