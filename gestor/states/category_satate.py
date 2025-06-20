import reflex as rx
from gestor.db_utils import get_category_by_id

class CategoryState(rx.State):
    category_id:int=0
    category_name:str=""
    category_description:str=""
    error:str=""

    def actualizar_id(self,value:str):
        try:
            self.category_id = int(value)
            self.error = ""
        except ValueError:
            self.category_id = 0
            self.error = "❌ ID no valido"

    def buscar_categoria(self):
        categoria = get_category_by_id(self.category_id)
        if categoria is None:
            self.error="❌ No se pudo encontrar la categoria"
        else:
            self.category_name = categoria.name
            self.category_description = categoria.description
            self.error=""
