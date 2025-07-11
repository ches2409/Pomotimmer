from sqlalchemy import Integer, String, Text, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from gestor.database.database import Base
class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'sqlite_autoincrement': True}

    id_task:Mapped[int]=mapped_column(Integer, primary_key=True)
    title:Mapped[str]=mapped_column(String(50), nullable=False)
    description:Mapped[str]=mapped_column(Text, nullable=False)
    completed:Mapped[bool]=mapped_column(Boolean, default=False)
    created_at:Mapped[DateTime]=mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    # FK hacia categories.id
    category_id:Mapped[int]=mapped_column(
        ForeignKey('categories.id', ondelete='RESTRICT'),
        nullable=False,
    )

    # Relacion inversa N:1
    category:Mapped["Category"]=relationship(
        "Category",
        back_populates="tasks",
    )