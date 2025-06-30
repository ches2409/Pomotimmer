
import reflex as rx

# Paleta Material completa (solo algunos tonos por color)
red50 = "#ffebee"
red100 = "#ffcdd2"
red200 = "#ef9a9a"
red300 = "#e57373"
red400 = "#ef5350"
red500 = "#f44336"
red600 = "#e53935"
red700 = "#d32f2f"
red800 = "#c62828"
red900 = "#b71c1c"

green50 = "#e8f5e9"
green100 = "#c8e6c9"
green200 = "#a5d6a7"
green300 = "#81c784"
green400 = "#66bb6a"
green500 = "#4caf50"
green600 = "#43a047"
green700 = "#388e3c"
green800 = "#2e7d32"
green900 = "#1b5e20"

blue50 = "#e3f2fd"
blue100 = "#bbdefb"
blue200 = "#90caf9"
blue300 = "#64b5f6"
blue400 = "#42a5f5"
blue500 = "#2196f3"
blue600 = "#1e88e5"
blue700 = "#1976d2"
blue800 = "#1565c0"
blue900 = "#0d47a1"

yellow50 = "#fffde7"
yellow100 = "#fff9c4"
yellow200 = "#fff59d"
yellow300 = "#fff176"
yellow400 = "#ffee58"
yellow500 = "#ffeb3b"
yellow600 = "#fdd835"
yellow700 = "#fbc02d"
yellow800 = "#f9a825"
yellow900 = "#f57f17"

gray50 = "#fafafa"
gray100 = "#f5f5f5"
gray200 = "#eeeeee"
gray300 = "#e0e0e0"
gray400 = "#bdbdbd"
gray500 = "#9e9e9e"
gray600 = "#757575"
gray700 = "#616161"
gray800 = "#424242"
gray900 = "#212121"

def alert_box(message: str, status: str = "success", tone: int = 200) -> rx.Component:
    # color_map = {
    #     "success": (green100, green800),
    #     "error": (red100, red800),
    #     "info": (blue100, blue800),
    #     "warning": (yellow100, yellow800),
    # }
    # bg, color = color_map.get(status, (gray100, gray800))  # Original line retained for context
    # Mapear el color base según el estado
    color_base = {
        "success": "green",
        "error": "red",
        "info": "blue",
        "warning": "yellow",
    }.get(status, "gray")

    # Obtener variables de color dinámicamente
    bg = globals().get(f"{color_base}{tone}", gray100)
    color = globals().get(f"{color_base}800", gray800)

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