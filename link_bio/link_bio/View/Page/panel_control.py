import reflex as rx
from link_bio.Components.menu import menu
from link_bio.Components.header import header
from link_bio.Components.footer import footer

def panel_control():
    return rx.vstack(
        # Cabecera de la página
        header(),
        # Contenido principal con menú a la izquierda
        rx.hstack(
            # Menú lateral
            rx.box(
                menu(),
                width="250px",
                # Ajusta el ancho del menú
                height="100vh",  # Ocupa toda la altura de la pantalla
                background="#2D3748",  # Color de fondo oscuro
                padding="1rem"
            ),
            # Sección de contenido
            rx.box(
                rx.vstack(
                    rx.heading(
                        "Panel de Control",
                        size="4",
                        font_size="2.5rem",  # Tamaño de fuente más grande
                        color="#2D3748",  # Color oscuro para el título
                        margin_bottom="1rem",  # Espaciado inferior
                        align_self="center",  # Centrar el título
                    ),
                    rx.text(
                        "Bienvenido al panel de control. Selecciona una opción en la barra lateral.",
                        font_size="1.25rem",
                        color="#4A5568",
                        text_align="center",  # Centrar texto
                    ),
                    spacing="3",
                    align_items="center",
                    justify_content="flex-start",  # Para que esté en la parte superior
                    width="100%",
                ),
                flex=1,
                padding="2rem",
                border_radius="12px",
                background="rgba(255, 255, 255, 0.8)",
                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                height="100vh",  # Ocupa toda la altura de la pantalla
            ),
        ),
        # Pie de página
        footer(),
    )
