from gestor.database.database import SessionLocal

from gestor.database.models import Category, Task


def fetch_all_categories():
    with SessionLocal() as db:
        return db.query(Category).all()

def fetch_all_tasks():
    with SessionLocal() as db:
        return db.query(Task).all()
