
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Definir el nombre de la base de datos
db_name="task_manager"

# Enrutar: crear ruta relativa al qrchivo actual (carpeta database)
db_path=os.path.join(os.path.dirname(__file__),f"{db_name}.db")

# db_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{db_name}.db")

# URL de conexion
DATABASE_URL=f"sqlite:///{db_path}"

# Crear motor de SQLAlchemy
engine=create_engine(DATABASE_URL, echo=False)

# Sesion local para consultas
SessionLocal=sessionmaker(bind=engine)

# Clase para modelos
class Base(DeclarativeBase):
    pass

# Crear tablas
def init_db():
    """Crea las tablas definidas en Base.metadata.
    Llamar en desarrollo o en test antes de usar el CRUD"""

    # Importar aqui para asegurar que todos los modelos estén registrados
    from gestor.models import Base as ModelsBase
    Base.metadata.create_all(bind=engine)

