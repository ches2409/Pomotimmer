import reflex as rx

from gestor.pages.category import category_form, category_list_view, category_details, category_lookup, prueba
from gestor.pages.task import task_form
from gestor.states.category_satate import CategoryState
from rxconfig import config


# class State(rx.State):
#     """The app state."""


def index() -> rx.Component:
    return rx.hstack(
        task_form()
    )


app = rx.App()
app.add_page(index)
