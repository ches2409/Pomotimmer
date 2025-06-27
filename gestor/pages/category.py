import reflex as rx

from gestor.components.alert_box import alert_box
from gestor.components.modal_edit_form import modalEditForm
from gestor.states.category_satate import CategoryState



def render_category(cat:dict)->rx.Component:
    is_default=cat["id"]==1

    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.heading(
                    cat['name'],
                    size="5"
                ),
                rx.cond(
                    is_default,
                    rx.badge("Por defecto", color_scheme='purple')
                ),
            ),
            rx.text(cat["description"], font_size="2"),
            rx.hstack(
                rx.button(
                    "🗑️ Eliminar",
                    color_scheme="red",
                    on_click=lambda: CategoryState.ask_delete_category(cat["id"]),
                    # size="2",
                    # mt="2"
                ),
                rx.button(
                    "📝 Editar",
                    color_scheme="blue",
                    on_click=lambda:CategoryState.open_edit_modal(cat["id"]),
                ),
            ),
        ),
        shadow="lg",
        border="1px solid #aaa",
        border_radius="lg",
        my="2",
        width="100%",
    )

def category_form()->rx.Component:
    return  rx.container(
        rx.vstack(
            # Titulo
            rx.heading(
                "Gestor de categorias",
                size="7"
            ),

            # Mensajes de informacion
            rx.cond(
                CategoryState.message!="",
                alert_box(CategoryState.message, status="info")
            ),

            # Formulario
            rx.box(
                rx.form(
                    rx.vstack(
                        rx.heading(
                          "Crear categoria",
                            size="5"
                        ),
                        rx.input(
                            placeholder="Nombre de la categoria",
                            on_change=CategoryState.set_name,
                            value=CategoryState.name,
                            width="100%",
                        ),
                        rx.text_area(
                            placeholder="Descripcion de la categoria",
                            on_change=CategoryState.set_description,
                            value=CategoryState.description,
                            width="100%",
                        ),
                        rx.hstack(
                            rx.button(
                                "Guardar",
                                on_click=CategoryState.create_category,
                                color_scheme="teal",
                            ),
                            rx.button(
                                "Cancelar",
                                on_click=CategoryState.cancel_delete,
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
                on_click=CategoryState.get_all_categories,
                mt="4",
                color_scheme="teal",
            ),
            rx.heading("Categorías registradas", size='5', margin_top=6),
            rx.vstack(
                rx.foreach(
                    CategoryState.categories,
                    render_category
                ),
                spacing="4"
            ),
            rx.cond(
                CategoryState.show_modal,
                rx.dialog.root(
                    rx.dialog.content(
                        rx.dialog.title("Confirmar eliminación"),
                        rx.dialog.description(
                            rx.text(f"¿Estás seguro de que deseas eliminar la categoría '{CategoryState.temp_name}'?")
                        ),
                        rx.flex(
                            rx.button("Cancelar", on_click=CategoryState.cancel_delete, color_scheme="gray"),

                            rx.button("Eliminar", on_click=CategoryState.delete_category, color_scheme="red"),
                            justify="end",
                            gap="2rem",
                            mt="2rem",
                            width="100%",
                        ),
                        initial={"opacity": 0, "y": -50},
                        animate={"opacity": 1, "y": 0},
                        exit={"opacity": 0, "y": 50},
                        transition={"duration": 5},
                    ),
                    open=CategoryState.show_modal,
                )
            ),
            rx.cond(
                CategoryState.show_modal_edit,
                modalEditForm(
                    title="Editar categoria",
                    description="Modifica el nombre o la descripción de una categoria",
                    show=CategoryState.show_modal_edit,
                    on_cancel=CategoryState.cancel_edit,
                    on_submit=lambda: CategoryState.update_category(CategoryState.temp_id),
                    fields=[
                        rx.input(
                            placeholder="Nombre de la categoria",
                            value=CategoryState.name,
                            on_change=CategoryState.set_name,
                            width="100%",
                        ),
                        rx.text_area(
                            placeholder="Descripcion de la categoria",
                            on_change=CategoryState.set_description,
                            value=CategoryState.description,
                            width="100%",
                        )
                    ]
                ),
            ),
            spacing="6",
            align="stretch",
        ),
        max_width="500px",
        margin_x="auto",
        padding_y=6

    )