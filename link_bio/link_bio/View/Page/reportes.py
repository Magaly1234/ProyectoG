import reflex as rx
from link_bio.Components.menu import menu
from link_bio.Components.header import header
from link_bio.Components.footer import footer

def reportes():
    return rx.vstack(
        # Cabecera de la página
        header(),
        menu(),
        footer()
    )