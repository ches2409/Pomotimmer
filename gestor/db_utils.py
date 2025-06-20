from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from sqlalchemy.orm import Session

from gestor.database.database import SessionLocal
from gestor.models import Category

def get_category_by_id(id:int=None) -> Category|None:
    # with SessionLocal() as db:
    #     return db.query(Category).get(id)

    try:
        if id is None:
            raise ValueError("El ID no puede estar vacio")

        with SessionLocal() as db:
            category=db.get(Category, id)
            if category is None:
                raise NoResultFound("No se encontró la categoria con el ID proporcionado")
            return category

    except NoResultFound as e:
        print(f"⚠️ {type(e).__name__}:e")
        return None
    except SQLAlchemyError as e:
        print(f"⚙️ Error en la base de datos {type(e).__name__} - e")
        return None
    except Exception as e:
        print(f" ❌ Error inseperado: {type(e).__name__} - e")
        return None


