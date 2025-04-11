import reflex as rx
from link_bio.Components.menu import menu
from link_bio.Components.header import header
from link_bio.Components.footer import footer
import asyncio
import websockets
import json

# Estado global para manejar los datos en tiempo real
class Estado(rx.State):
    dorsiflexion: float = 0.0
    abduccion: float = 0.0
    inversion: float = 0.0
    conectado: bool = False
    datos_guardados: bool = False
    contador_guardados: int = 0
    # Añadimos una referencia al websocket
    _websocket = None
    _task = None
    

    # Función para recibir datos en tiempo real desde el WebSocket
    async def recibir_datos(self):
        if self.conectado:
            return  # Evita múltiples conexiones

        self.conectado = True
        self.datos_guardados = False
        self.contador_guardados = 0
        
        yield 
        uri = "ws://127.0.0.1:8000/ws/datos"  # WebSocket de la API

        try:
            async with websockets.connect(uri) as websocket:
                # Guardamos la referencia al websocket
                Estado._websocket = websocket

                # Enviar mensaje para iniciar el streaming de datos
                await websocket.send("Iniciar Streaming")
                print("Conexión abierta y streaming iniciado")

                while self.conectado:
                    mensaje = await websocket.recv()
                    print("Mensaje recibido:", mensaje)
                    
                    #data = await websocket.recv()
                    datos_json = json.loads(mensaje)
                    angulos = datos_json.get("angulos", {})

                    # Actualizar el estado con los nuevos ángulos
                    self.dorsiflexion = angulos.get("dorsiflexion", 0.0)
                    self.abduccion = angulos.get("abduccion", 0.0)
                    self.inversion = angulos.get("inversion", 0.0)

# Indicar que los datos se han guardado (la API los guarda automáticamente)
                    self.datos_guardados = True
                    self.contador_guardados += 1
                    
                    yield

                    # Notificar a Reflex que el estado ha cambiado
                    
                    await asyncio.sleep(0.3) # Controla la frecuencia de actualización de datos
        
        except websockets.exceptions.ConnectionClosed as e:
            print("Conexión WebSocket cerrada:", e)
            yield
        
        except Exception as e:
            print(f"Error en WebSocket: {e}")
            yield
            
        finally:
            self.conectado = False
            Estado._websocket = None
            
            
            yield

    # Función para detener el streaming de datos
    def detener_streaming(self):
        self.conectado = False
        
        print("Streaming detenido")

# Definir la interfaz de monitoreo en tiempo real
def monitoreo():
    return rx.vstack(
        header(),
        # Menú lateral fijo
        menu(),
        
        rx.vstack(
            # Contenido principal con fondo de gradiente sutil
            rx.vstack(
                rx.center(
                    rx.heading(
                        "Monitoreo en Tiempo Real", 
                        size="6", 
                        color="blue.700", 
                        margin_bottom="1rem",
                        font_weight="bold",
                        background="linear-gradient(90deg, #2b6cb0 0%, #3182ce 100%)",
                        background_clip="text",
                        text_shadow="0px 2px 4px rgba(0, 0, 0, 0.1)"
                    ),
                    width="100%",
                    margin_top="0rem"
                ),
                rx.hstack(
                    # Gráfico de Movimiento mejorado
                    rx.card(
                        rx.vstack(
                            rx.heading(
                                "Gráfico de Movimiento", 
                                size="4", 
                                margin_bottom="1.5rem",
                                color="blue.800"
                            ),
                            rx.text(
                                "Visualización de datos en tiempo real...", 
                                color="gray.600",
                                font_style="italic"
                            ),
                            # Espacio para el gráfico
                            rx.box(
                                height="350px",
                                width="100%",
                                border_radius="md",
                                background="linear-gradient(180deg, #f7fafc 0%, #edf2f7 100%)",
                                border="1px dashed",
                                border_color="blue.200"
                            )
                        ),
                        padding="2rem",
                        width="100%",
                        max_width="500px",
                        shadow="xl",
                        border_radius="xl",
                        background="white",
                        border="1px solid",
                        border_color="blue.100",
                        align_self="start",
                    ),
                    
                    # Tarjetas de métricas mejoradas
                    rx.vstack(
                        rx.vstack(
                            # Dorsiflexión - Flexion Palmar
                            rx.card(
                                rx.vstack(
                                    rx.text(
                                        "Dorsiflexión - Flexion Palmar", 
                                        size="3", 
                                        color="gray.700",
                                        font_weight="medium"
                                    ),
                                    rx.heading(
                                        f"{Estado.dorsiflexion :.2f}°", 
                                        size="2", 
                                        color="blue.600", 
                                        align="center",
                                        font_weight="bold",
                                        background="linear-gradient(90deg, #3182ce 0%, #2c5282 100%)",
                                        background_clip="text"
                                    ),
                                    # Indicador visual
                                    rx.box(
                                        height="6px",
                                        width="80%",
                                        background="linear-gradient(90deg, #ebf8ff 0%, #3182ce 100%)",
                                        border_radius="full",
                                        margin_top="0.5rem"
                                    )
                                ),
                                align="center",
                                padding="1.5rem",
                                width="100%",
                                max_width="320px",
                                shadow="lg",
                                border_radius="xl",
                                background="white",
                                border="1px solid",
                                border_color="blue.100",
                                transition="all 0.3s"
                            ),
                            
                            # Abducción - Aducción
                            rx.card(
                                rx.vstack(
                                    rx.text(
                                        "Abducción - Aducción", 
                                        size="3", 
                                        color="gray.700",
                                        font_weight="medium"
                                    ),
                                    rx.heading(
                                        f"{Estado.abduccion:.2f}°", 
                                        size="2", 
                                        color="blue.600",
                                        align="center",
                                        font_weight="bold",
                                        background="linear-gradient(90deg, #3182ce 0%, #2c5282 100%)",
                                        background_clip="text"
                                    ),
                                    # Indicador visual
                                    rx.box(
                                        height="6px",
                                        width="80%",
                                        background="linear-gradient(90deg, #ebf8ff 0%, #3182ce 100%)",
                                        border_radius="full",
                                        margin_top="0.5rem"
                                    )
                                ),
                                padding="1.5rem",
                                width="100%",
                                max_width="320px",
                                shadow="lg",
                                border_radius="xl",
                                background="white",
                                border="1px solid",
                                border_color="blue.100",
                                align="center",
                                transition="all 0.3s"
                            ),
                            
                            # Inversión - Eversión
                            rx.card(
                                rx.vstack(
                                    rx.text(
                                        "Inversión - Eversión", 
                                        size="3", 
                                        color="gray.700",
                                        font_weight="medium"
                                    ),
                                    rx.heading(
                                        f"{Estado.inversion:.2f}°", 
                                        size="2", 
                                        color="blue.600",
                                        align="center",
                                        font_weight="bold",
                                        background="linear-gradient(90deg, #3182ce 0%, #2c5282 100%)",
                                        background_clip="text"
                                    ),
                                    # Indicador visual
                                    rx.box(
                                        height="6px",
                                        width="80%",
                                        background="linear-gradient(90deg, #ebf8ff 0%, #3182ce 100%)",
                                        border_radius="full",
                                        margin_top="0.5rem"
                                    )
                                ),
                                padding="0.75srem",
                                width="100%",
                                max_width="320px",
                                shadow="lg",
                                border_radius="xl",
                                background="white",
                                border="1px solid",
                                border_color="blue.100",
                                align="center",
                                transition="all 0.3s"
                            ),
                            spacing="3",
                            justify="end",
                        ),
                        align="end",
                        width="100%",
                        padding_right="2rem",
                    ),
                    spacing="4",
                    width="100%",
                    justify="center", 
                    padding_x="2rem",
                    align="center",
                    margin_bottom="2rem"
                ),
                
                # Botones de streaming mejorados
                rx.center(
                    rx.hstack(
                        rx.button(
                            rx.hstack(
                                rx.icon("play", color="white"),
                                rx.text("Iniciar ", font_weight="bold"),
                                spacing="0"
                            ),
                            on_click=Estado.recibir_datos,
                            color_scheme="blue",
                            size="4",
                            shadow="md",
                            border_radius="lg",
                            background="linear-gradient(90deg, #2b6cb0 0%, #3182ce 100%)",
                            _hover={"background": "linear-gradient(90deg, #2c5282 0%, #2b6cb0 100%)"},
                            padding_x="4",
                            margin_bottom="3rem"
                        ),
                        
                        rx.button(
                            rx.hstack(
                                rx.icon("stop", color="red.600"),
                                rx.text("Detener", font_weight="bold"),
                                spacing="1"
                            ),
                            on_click=Estado.detener_streaming,
                            variant="outline",
                            color_scheme="red",
                            size="4",
                            shadow="md",
                            border_radius="lg",
                            _hover={"background": "red.50"},
                            padding_x="4",
                            margin_bottom="3rem"
                        ),
                        spacing="4",
                        margin_y="1rem"
                    ),
                
                    width="100%",
                    margin_bottom="2rem"
                ),
                
                footer(),
                spacing="0",
                width="100%",
                align="start",
                height="calc(100vh - 60px)",
                background="linear-gradient(180deg, #f7fafc 0%, #edf2f7 100%)",
                min_height="100vh",
                margin_left="250px",
                border_left="1px solid",
                border_color="gray.200",
                padding_bottom="1rem",
                overflow="hidden",
                margin_bottom="2rem"
                
            ),
            align_items="flex-start",
            height="100vh",
            margin_bottom="2rem"
            
        ), 
        spacing="1"
    )

# Crear la aplicación Reflex y agregar la página de monitoreo
app = rx.App()
app.add_page(monitoreo)
