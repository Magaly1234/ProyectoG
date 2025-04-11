import reflex as rx

def menu():
    return rx.box(
        rx.spacer(), 
        rx.vstack(
            #Logo y título del menú
            rx.box(
                #rx.image(src="/logo.png", width="50px", height="50px"),  # Agrega tu logo aquí
                rx.spacer(), 
                rx.text("Menú Principal", font_size="1.2rem", font_weight="bold", color="#2D3748"),
                align_items="center",
                #spacing="2rem",
                #padding="1rem",
                margin_top="4rem"  
                
            ),
            
            # Enlaces del menú con íconos
            rx.link(
                rx.hstack(rx.icon("users"), rx.text("Pacientes")),
                href="/pacientes",
                padding="1rem",
                width="100%",
                background_color="#ffffff",
                color="#2D3748",
                border_radius="8px",
                _hover={"background_color": "#6EA1F9", "color": "#ffffff"},
                transition="all 0.2s ease-in-out",
            ),
            rx.link(
                rx.hstack(rx.icon("list"), rx.text("Lista de Pacientes")),
                href="/lista_pacientes",
                padding="1rem",
                width="100%",
                background_color="#ffffff",
                color="#2D3748",
                border_radius="8px",
                _hover={"background_color": "#6EA1F9", "color": "#ffffff"},
                transition="all 0.2s ease-in-out",
            ),
            rx.link(
                rx.hstack(rx.icon("monitor"), rx.text("Monitoreo en Vivo")),
                href="/monitoreo",
                padding="1rem",
                width="100%",
                background_color="#ffffff",
                color="#2D3748",
                border_radius="8px",
                _hover={"background_color": "#6EA1F9", "color": "#ffffff"},
                transition="all 0.2s ease-in-out",
            ),
            rx.link(
                rx.hstack(rx.icon("bar-chart"), rx.text("Reportes")),
                href="/reportes",
                padding="1rem",
                width="100%",
                background_color="#ffffff",
                color="#2D3748",
                border_radius="8px",
                _hover={"background_color": "#6EA1F9", "color": "#ffffff"},
                transition="all 0.2s ease-in-out",
            ),
            
            rx.spacer(),  # Empuja la opción de cerrar sesión al final
            
            # Cerrar sesión
            rx.link(
                rx.hstack(rx.icon("log-out"), rx.text("Cerrar Sesión")),
                href="/",
                padding="1rem",
                width="100%",
                background_color="#ffffff",
                color="#E53E3E",
                border_radius="8px",
                _hover={"background_color": "#F56565", "color": "#ffffff"},
                transition="all 0.2s ease-in-out",
            ),
            
            spacing="2",
            align_items="stretch",
        ),
        width="260px",
        height="100vh",
        position="fixed",
        top="0",
        left="0",
        padding="1rem",
        background_color="#f0f4f8",
        border_radius="0 12px 12px 0",
        box_shadow="4px 0 6px -1px rgba(0, 0, 0, 0.1)",
    )
