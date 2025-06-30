import reflex as rx
from reflex import Var

from gestor.states.category_satate import CategoryState
from gestor.states.task_state import TaskState


def modalEditForm(
        title:str,
        description:str,
        show:Var[bool],
        on_cancel:rx.EventHandler,
        on_submit:rx.EventHandler,
        fields:list[rx.Component], # Lista de inputs dinamicos
)->rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(title),
            rx.dialog.description(description),
            rx.vstack(
                *fields,
                spacing="4",
                align="stretch",
            ),
            rx.flex(
                rx.button(
                    "Cancelar",
                    on_click=on_cancel,
                    color_scheme="gray"
                ),
                rx.button(
                    "Guardar",
                    on_click=on_submit,
                    color_scheme="green"
                ),
                justify="end",
                gap="8"
            )
        ),
        open=show
    )

def action_buttom(obj,is_category=True):
    if is_category:
        return rx.hstack(
            rx.button(
                "🗑️ Eliminar",
                color_scheme="red",
                on_click=lambda: CategoryState.ask_delete_category(obj["id"]),
            ),
            rx.button(
                "📝 Editar",
                color_scheme="blue",
                on_click=lambda: CategoryState.open_edit_modal(obj["id"]),
            ),
        )
    else:
        return rx.hstack(
            rx.button(
                "🗑️ Borrar",
                color_scheme="orange",
                # on_click=lambda: TaskState.ask_delete_task(obj["id"]),
            ),
            rx.button(
                "📝 Editar",
                color_scheme="blue",
                # on_click=lambda: TaskState.open_edit_modal(obj["id"]),
            ),
        )

def render_obj(obj: dict) -> rx.Component:

    is_task=obj.contains('categoria_id')

    return rx.card(
        rx.vstack(
            rx.heading(
                obj['name'],
                size="5"
            ),
            rx.text(obj["description"], font_size="2"),
            rx.cond(
                # obj["categoria_id"],
                is_task,
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "Categoria:",
                            font_size="4"
                        ),
                        rx.text(obj["categoria_id"], font_size="2"),

                    ),
                    action_buttom(obj,is_category=False),
                ),
                action_buttom(obj),
            ),

        ),
        shadow="lg",
        border="1px solid #aaa",
        border_radius="lg",
        my="2",
        width="100%",

    )

