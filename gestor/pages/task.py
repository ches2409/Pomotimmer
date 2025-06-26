import reflex as rx

from gestor.states.category_satate import CategoryState
from gestor.states.task_state import TaskState

def task_form()->rx.Component:
    return rx.vstack(
        rx.heading(
            "Crear una tarea"
        ),
        rx.input(
            placeholder="Nombre de la tarea",
            on_change=TaskState.set_title,
            value=TaskState.title,
        ),
        rx.input(
            placeholder="Descripcion de la tarea",
            on_change=TaskState.set_description,
            value=TaskState.description_task,
        ),
        rx.input(
            placeholder="ID de la categoria",
            on_change=TaskState.set_temp_id,
            value=TaskState.temp_id,
        ),
        rx.button(
            "Crear tarea",
            on_click=TaskState.create_task
        ),
        rx.text(
            TaskState.message,
        )
    )

