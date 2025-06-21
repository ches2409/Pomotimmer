import reflex as rx
from reflex.components.radix.themes.layout.stack import vstack

from gestor.crud import get_category_by_id
from gestor.states.category_satate import CategoryState

def category_list_view():
    return rx.vstack(
        rx.heading(
            "Listar caategorias",
            size="7"
        ),
        rx.button(
            "Cargar categorias",
            on_click=CategoryState.get_all_categories
        ),
        rx.foreach(
            CategoryState.categories,
            lambda cat: rx.card(
                rx.text(
                    f"ID: {cat.id}",
                ),
                rx.text(
                    f"Nombre: {cat.name}",
                ),
                rx.text(
                    f"Descripcion: {cat.description}",
                ),
                shadow="md",
                p="4",
                m="2"
            )
        ),
    )


def category_details()->rx.Component:
    return rx.box(
        rx.heading(
            "Detalles de la categoria",
            size="7"
        ),
        rx.cond(
            CategoryState.selected_category["id"] !=None,
            rx.vstack(
                rx.text(
                    f"ID: {CategoryState.selected_category['id']}",
                ),
                rx.text(
                    f"Nombre: {CategoryState.selected_category['name']}",
                ),
                rx.text(
                    f"Descripción: {CategoryState.selected_category['description']}",
                )
            ),
            rx.text(
                "Selecciona una categoria para ver detalles."
            )
        )
    )

def category_lookup()->rx.Component:
    return rx.vstack(
        rx.heading(
            "Ver una categoria",
            size="7"
        ),
        rx.input(
            placeholder="Introduce el ID de la categoria",
            on_change=CategoryState.set_temp_id,
        ),
        rx.button(
            "Buscar categoria",
            on_click=CategoryState.get_category_by_id(CategoryState.temp_id)
        ),
        category_details()
    )

def category_form():
    return  vstack(
        rx.heading(
            "Crear una nueva categoria",
            size="7"
        ),
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
            color=rx.cond(
                CategoryState.message.contains("✅"),
                "green",
                "red"
            )
        )
    )

def prueba():
    return vstack(
        rx.heading(
            "Prueba para ver el id"
        ),
        rx.input(
            placeholder="Introduce el ID de la categoria",
            on_change=CategoryState.set_temp_id,
        ),
        rx.input(
            placeholder="Nuevo nombre de la categoria",
            on_change=CategoryState.set_name,
            value=CategoryState.name
        ),
        rx.input(
            placeholder="Nueva descripcion de la categoria",
            on_change=CategoryState.set_description,
            value=CategoryState.description
        ),
        rx.button(
            "Guardar cambios",
            on_click=CategoryState.update_category(CategoryState.temp_id)

        ),
    )
