import reflex as rx
from reflex import Var


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
