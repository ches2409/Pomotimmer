from sqlalchemy import Integer, String, Text, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column


from gestor.database.database import Base


class Category(Base):
    __tablename__ = 'categories'
    __table_args__ = {'sqlite_autoincrement': True}

    id:Mapped[int]=mapped_column(Integer, primary_key=True)
    name:Mapped[str]=mapped_column(String(50), nullable=False)
    description:Mapped[str]=mapped_column(String(100))

    # Relacion 1:N => una categoria tiene muchas tareas
    tasks:Mapped[list["Task"]]=relationship(
        "Task",
        back_populates="category"
    )

    def __repr__(self):
        return f"<Category id={self.id} name={self.name}>"