import reflex as rx

def header():
    return rx.box(
        rx.image(src="/logo.png", height="40px"),  # Logo de la universidad
        rx.text(" Universidad Mayor De San Andrés ", font_size="0.8rem", font_weight="bold"), 
        rx.spacer(                     ), 
        rx.text(" SMRET ", font_size="0.8rem", font_weight="bold"), # Nombre de la universidad
        display="flex",
        align_items="center",
        padding="0.5rem",
        width="100%",
        background_color="#253776",  # Color de fondo
        color="white",
        top="0",  # Posicionar en la parte superior
        left="0",  # Posicionar en la parte izquierda
        z_index="1000" # Asegurar que esté por encima de otros elementos# Color del texto
    )