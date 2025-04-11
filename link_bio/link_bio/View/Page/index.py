import reflex as rx
from link_bio.Components.header import header
from link_bio.Components.footer import footer

def index():
    return rx.vstack(
        header(),

        rx.center(
            rx.vstack(
                rx.image(
                    src="pie.png", 
                    width="140px",
                    height="auto",
                    border_radius="50%",
                    box_shadow="0 4px 8px rgba(0,0,0,0.15)",
                    margin_bottom="0.5rem"
                ),

                rx.hstack(
                    rx.icon(tag="activity", size=22, color="#0d47a1"),  
                    rx.text("SMRET", 
                            font_size="1.8rem", 
                            font_weight="bold",
                            color="#0d47a1",
                            letter_spacing="-0.03em"
                    ),
                    align_items="center",
                    spacing="1",
                ),

                rx.heading(
                    "Monitoreo de Rehabilitación de Esguinces",
                    size="5",
                    text_align="center",
                    color="#333",
                    margin_top="0.2rem"
                ),

                rx.box(
                    rx.vstack(
                        rx.text("Bienvenido", font_size="1.3rem", font_weight="bold", color="white"),
                        rx.text(
                            "Plataforma para el monitoreo de rehabilitación con sensores MPU6050.",
                            font_size="0.9rem",
                            color="white",
                            text_align="center",
                            padding_x="0.5rem",
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.text("Iniciar"),  
                                    rx.icon(tag="arrow-right", size=14, color="white"),
                                    spacing="1",
                                ),
                                background_color="#1a237e",
                                color="white",
                                size="2",
                                border_radius="6px",
                                _hover={"background_color": "#3949ab"},
                                padding_x="1rem",
                                padding_y="0.5rem"
                            ),
                            href="/panel_control",
                        ),
                        align_items="center",
                        spacing="2",
                    ),
                    background_color="#3949ab",
                    padding="1rem",
                    border_radius="10px",
                    box_shadow="0px 4px 10px rgba(0, 0, 0, 0.2)",
                    width="300px",
                    margin_top="0.5rem",
                ),

                spacing="3",
                align_items="center",
                width="100%",
            ),
            height="95vh",  
            background="linear-gradient(180deg, #ffffff, #a8c6fa)",  
            padding="0",
            width="100%",
        ),

        footer(),
    )
