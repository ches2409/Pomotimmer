import reflex as rx
from reflex.components.radix.themes.layout.stack import vstack

from gestor.states.category_satate import CategoryState

def category_form():
    return  vstack(
        rx.input(
            placeholder="Nombre de la categoria",
            on_change=CategoryState.set_name,
            value=CategoryState.name
        ),
        rx.text_area(
            placeholder="Descripcion de la categoria",
            on_change=CategoryState.set_description,
            value=CategoryState.description
        ),
        rx.button(
            "Crear categoria",
            on_click=CategoryState.create_category
        ),
        rx.text(
            CategoryState.message,
            color="green"
        )
    )
