
import reflex as rx
import link_bio.Styles.styles as styles

def button(text: str, url: str) -> rx.Component:
    return rx.link(
    rx.button(
    text,
    size="4",  # Cambia '5' por un valor válido como '4'
    color_scheme="blue",
    border_radius="8px",
    box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
    padding="0.8rem 1.5rem",  # Corrige unidades de padding
    font_weight="bold",
    _hover={
        "transform": "translateY(-2px)",
        "box_shadow": "0 6px 8px rgba(0, 0, 0, 0.15)",
    },
    transition="all 0.3s ease",
),       
        href=url,
        is_external=True,
    )