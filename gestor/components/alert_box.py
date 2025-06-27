import reflex as rx

# Asignar colres en variables
green100="#c8e6c9"
green800="#2e7d32"
red100="#ffcdd2"
red800="#c62828"
blue100="#bbdefb"
blue800="#1565c0"
yellow100="#fff9c4"
yellow800="#f9a825"
gray100="#f5f5f5"
gray800="#424242"

def alert_box(message: str, status: str = "success"):
    color_map = {
        "success": (green100, green800),
        "error": (red100, red800),
        "info": (blue100, blue800),
        "warning": (yellow100, yellow800),
    }
    bg, color = color_map.get(status, (gray100, gray800))
    return rx.box(
        rx.text(message),
        bg=bg,
        color=color,
        padding_x=6,
        padding_y=4,
        border_radius=".5rem",
        font_weight="medium",
        box_shadow="md"
    )