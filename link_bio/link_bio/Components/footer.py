import reflex as rx
def footer() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("© 2025 INGENIERÍA MECÁNICA Y ELECTROMECÁNICA", font_size="0.5rem", font_weight="bold"),  # Texto a la izquierda
            rx.spacer(),  # Espacio flexible para empujar el texto a la derecha
            rx.text("Contacto: magalyhuancasalgueiro@gmail.com", font_size="0.5rem", font_weight="bold"),  # Texto a la derecha
            align_items="center",  # Alinear elementos verticalmente
            width="100%",  # Ocupar el 100% del ancho
        ),
        padding="0.5rem",
        background_color="#253776",  # Color de fondo
        color="white",  # Color del texto
        width="100%",  # Ocupar el 100% del ancho de la pantalla
        position="fixed",  # Fijar el pie de página en la parte inferior
        bottom="0",  # Posicionar en la parte inferior
        left="0",  # Posicionar en la parte izquierda
        z_index="1000",  # Asegurar que esté por encima de otros elementos
    )