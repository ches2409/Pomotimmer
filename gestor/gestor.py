import reflex as rx

from gestor.pages.category import category_form
from gestor.states.category_satate import CategoryState
from rxconfig import config


# class State(rx.State):
#     """The app state."""


def index() -> rx.Component:
    return rx.container(
        category_form()
    )


app = rx.App()
app.add_page(index)
