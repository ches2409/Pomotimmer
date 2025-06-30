import reflex as rx

from gestor.pages.category import category_form
from gestor.pages.task import task_form
from gestor.states.category_satate import CategoryState
from rxconfig import config


# class State(rx.State):
#     """The app state."""


def index() -> rx.Component:
    return rx.hstack(
        category_form(),
        task_form(),
    )


app = rx.App()
app.add_page(index)
