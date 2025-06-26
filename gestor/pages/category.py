import reflex as rx

from gestor.components.alert_box import alert_box
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
                ),
            ),
        ),
        shadow="lg",
        border="1px solid #aaa",
        border_radius="lg",
        my="2",
        width="100%",
    )

def category_list_view()->rx.Component:
    return rx.vstack(
        rx.heading(
            "Listar categorias",
            size="7"
        ),
        rx.button(
            "Cargar categorias",
            on_click=CategoryState.get_all_categories
        ),
        rx.foreach(CategoryState.categories,render_category),
        rx.button(
            "🔄 Recargar Categorías",
            on_click=CategoryState.get_all_categories,
            mt="4",
            color_scheme="teal",
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
                    initial={"opacity": 0,"y":-50},
                    animate={"opacity": 1,"y":0},
                    exit={"opacity": 0,"y":50},
                    transition={"duration": 5},
                ),
                open=CategoryState.show_modal,
            )
        ),
        spacing="4",
        align="stretch",
        p="6",
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
            spacing="6",
            align="stretch",
        ),
        max_width="500px",
        margin_x="auto",
        padding_y=6

    )

def prueba():
    return vstack(
        rx.heading(
            "Actualizar una categoria",
        ),
        rx.input(
            placeholder="Introduce el ID de la categoria",
            on_change=CategoryState.set_temp_id,
        ),
        # rx.input(
        #     placeholder="Nuevo nombre de la categoria",
        #     on_change=CategoryState.set_name,
        #     value=CategoryState.name
        # ),
        # rx.input(
        #     placeholder="Nueva descripcion de la categoria",
        #     on_change=CategoryState.set_description,
        #     value=CategoryState.description
        # ),
        rx.button(
            "Guardar cambios",
            on_click=CategoryState.delete_category(CategoryState.temp_id)

        ),
        rx.text(
            CategoryState.message,
        )
    )
