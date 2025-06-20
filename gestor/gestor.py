import reflex as rx

from gestor.states.category_satate import CategoryState
from rxconfig import config


# class State(rx.State):
#     """The app state."""


def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Prueba de gestor"),
            rx.input(
                placeholder="ID categoria",
                on_change=CategoryState.actualizar_id
            ),
            rx.button(
                "Buscar",
                on_click=CategoryState.buscar_categoria
            ),
            rx.hstack(
                rx.text(
                    CategoryState.category_name, color="green"
                ),
                rx.spacer(),
                rx.text(
                    CategoryState.category_description, color="darkseagreen"
                )
            ),
            rx.text(
                CategoryState.error, color="red"
            )
        )
    )


app = rx.App()
app.add_page(index)
