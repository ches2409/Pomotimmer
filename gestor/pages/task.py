import reflex as rx

from gestor.components.alert_box import alert_box
from gestor.components.modal_edit_form import render_obj
from gestor.states.category_satate import CategoryState
from gestor.states.task_state import TaskState

def create_form()->rx.Component:
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
            on_change=TaskState.set_category_id,
            value=TaskState.category_id,
        ),
        rx.button(
            "Crear tarea",
            on_click=TaskState.create_task
        ),
        rx.text(
            TaskState.message,
        )
    )
def list_tasks()->rx.Component:
    return rx.vstack(
    )
def task_form()->rx.Component:
    return  rx.container(
        rx.vstack(
            # Titulo
            rx.heading(
                "Gestor de Tareas",
                size="7"
            ),

            # Mensajes de informacion
            rx.cond(
                TaskState.message != "",
                alert_box(TaskState.message, status="info", tone=100)
            ),

            # Formulario
            rx.box(
                rx.form(
                    rx.vstack(
                        rx.heading(
                          "Crear Tarea",
                            size="5"
                        ),
                        rx.input(
                            placeholder="Nombre de la categoria",
                            on_change=TaskState.set_title,
                            value=TaskState.title,
                            width="100%",
                        ),
                        rx.text_area(
                            placeholder="Descripcion de la categoria",
                            on_change=TaskState.set_description,
                            value=TaskState.description_task,
                            width="100%",
                        ),
                        rx.hstack(
                            rx.button(
                                "Guardar",
                                # on_click=TaskState.create_category,
                                color_scheme="teal",
                            ),
                            rx.button(
                                "Cancelar",
                                # on_click=TaskState.cancel_delete,
                                color_scheme="gray",
                            ),
                            justify="end",
                            width="100%",
                        )

                    ),
                    width="100%",
                    justify="center",
                ),
                padding=8,
                shadow="md",
                border_radius="1rem",
                border="1px solid #e2e8f0",
                # max_width="300px",
                width="100%",

            ),
            rx.button(
                "🔄 Recargar Categorías",
                on_click=TaskState.get_all_tasks,
                mt="4",
                color_scheme="teal",
            ),
            rx.heading("Tareas registradas", size='5', margin_top=6),
            rx.vstack(
                rx.foreach(
                    TaskState.tasks,
                    render_obj
                ),
                spacing="4"
            ),
            # rx.cond(
            #     TaskState.show_modal,
            #     rx.dialog.root(
            #         rx.dialog.content(
            #             rx.dialog.title("Confirmar eliminación"),
            #             rx.dialog.description(
            #                 rx.text(f"¿Estás seguro de que deseas eliminar la categoría '{TaskState.temp_name}'?")
            #             ),
            #             rx.flex(
            #                 rx.button("Cancelar", on_click=TaskState.cancel_delete, color_scheme="gray"),
            #
            #                 rx.button("Eliminar", on_click=TaskState.delete_category, color_scheme="red"),
            #                 justify="end",
            #                 gap="2rem",
            #                 mt="2rem",
            #                 width="100%",
            #             ),
            #             initial={"opacity": 0, "y": -50},
            #             animate={"opacity": 1, "y": 0},
            #             exit={"opacity": 0, "y": 50},
            #             transition={"duration": 5},
            #         ),
            #         open=TaskState.show_modal,
            #     )
            # ),
            # rx.cond(
            #     TaskState.show_modal_edit,
            #     modalEditForm(
            #         title="Editar categoria",
            #         description="Modifica el nombre o la descripción de una categoria",
            #         show=TaskState.show_modal_edit,
            #         on_cancel=TaskState.cancel_edit,
            #         on_submit=lambda: TaskState.update_category(TaskState.temp_id),
            #         fields=[
            #             rx.input(
            #                 placeholder="Nombre de la categoria",
            #                 value=TaskState.name,
            #                 on_change=TaskState.set_name,
            #                 width="100%",
            #             ),
            #             rx.text_area(
            #                 placeholder="Descripcion de la categoria",
            #                 on_change=TaskState.set_description,
            #                 value=TaskState.description,
            #                 width="100%",
            #             )
            #         ]
            #     ),
            # ),
            spacing="6",
            align="stretch",
        ),
        max_width="500px",
        margin_x="auto",
        padding_y=6

    )
