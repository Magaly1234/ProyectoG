import reflex as rx
from link_bio.Components.menu import menu
from link_bio.Components.header import header
from link_bio.Components.footer import footer
from link_bio.db.db_operation import obtener_pacientes, insertar_paciente

class PacienteState(rx.State):
    id:  str =""
    nombre: str = ""
    edad: str = ""
    observaciones: str = ""
    deporte: str = "Fútbol"
    estado_tratamiento: str = "En progreso"
    fecha_ultima_consulta: str = ""
    error_msg: str = ""  # Inicializado correctamente

    def set_id(self, id: str):
        self.id = id
        self.error_msg = "" 
    
    def set_nombre(self, nombre: str):
        self.nombre = nombre
        self.error_msg = ""  # Limpiar mensaje de error

    def set_edad(self, edad: str):
        self.edad = edad
        self.error_msg = ""  # Limpiar mensaje de error

    def set_observaciones(self, observaciones: str):
        self.observaciones = observaciones
        self.error_msg = ""  # Limpiar mensaje de error

    def set_estado_tratamiento(self, estado: str):
        self.estado_tratamiento = estado
        self.error_msg = ""  # Limpiar mensaje de error
    
    def set_deporte(self, estado: str):
        self.deporte = estado
        self.error_msg = ""  # Limpiar mensaje de error

    def set_fecha_ultima_consulta(self, fecha: str):
        self.fecha_ultima_consulta = fecha
        self.error_msg = ""  # Limpiar mensaje de error

    def agregar_paciente(self):
        if not self.id:
            self.error_msg = "CI es obligatorio"
            return
        # Validaciones
        if not self.nombre:
            self.error_msg = "Nombre es obligatorio"
            return
        
        if not self.edad:
            self.error_msg = "Edad es obligatoria"
            return
        
        if not self.edad.isdigit():
            self.error_msg = "La edad debe ser un número válido"
            return
        
        if int(self.edad) <= 0:
            self.error_msg = "Edad inválida"
            return
        
        if not self.observaciones:
            self.error_msg = "Observaciones es obligatoria"
            return
        
        if not self.fecha_ultima_consulta:
            self.error_msg = "Fecha de última consulta es obligatoria"
            return

        try:
            # Insertar paciente en la base de datos
            insertar_paciente(
                id=int(self.id),
                nombre=self.nombre,
                edad=int(self.edad),
                observaciones=self.observaciones,
                deporte=self.deporte,
                estado_tratamiento=self.estado_tratamiento,
                fecha_ultima_consulta=self.fecha_ultima_consulta
            )

            # Reiniciar los valores después de agregar el paciente
            self.id=""
            self.nombre = ""
            self.edad = ""
            self.observaciones = ""
            self.estado_tratamiento = "Iniciando"
            self.deporte = "Futbol"
            self.fecha_ultima_consulta = ""
            
            self.error_msg = ""
            return rx.window_alert("Paciente agregado exitosamente")
        
        except Exception as e:
            self.error_msg = f"Error al agregar paciente: {str(e)}"
            return

def pacientes() -> rx.Component:
    lista_pacientes = obtener_pacientes()

    return rx.vstack(
        header(),
        menu(),
        rx.center(
            rx.vstack(
                rx.heading("Registro de Pacientes", size="7", color="blue.600"),
                rx.form(
                    rx.vstack(
                        rx.input(
                            value=PacienteState.id, 
                            placeholder="Carnet de Identidad del paciente", 
                            on_change=PacienteState.set_id,
                            width="100%",
                            variant="soft",
                            color_scheme="blue"
                        ),
                        rx.input(
                            value=PacienteState.nombre, 
                            placeholder="Nombre del paciente", 
                            on_change=PacienteState.set_nombre,
                            width="100%",
                            variant="soft",
                            color_scheme="blue"
                        ),
                        rx.input(
                            value=PacienteState.edad, 
                            placeholder="Edad", 
                            type="text",  # Cambiado de number a text para manejar validaciones personalizadas
                            on_change=PacienteState.set_edad,
                            width="100%",
                            variant="soft",
                            color_scheme="blue"
                        ),
                        rx.input(
                            value=PacienteState.observaciones, 
                            placeholder="Observaciones", 
                            on_change=PacienteState.set_observaciones,
                            width="100%",
                            variant="soft",
                            color_scheme="blue"
                        ),
                        rx.select(
                            ["Iniciando","En progreso", "Finalizado", "Pendiente"],
                            value=PacienteState.estado_tratamiento,
                            placeholder="Estado del tratamiento",
                            on_change=PacienteState.set_estado_tratamiento,
                            width="100%",
                            variant="soft",
                            color_scheme="blue"
                        ),
                        rx.select(
                            ["Básquetbol", "Fútbol", "Tenis","Trail running","Voleibol", "Otros"],
                            value=PacienteState.deporte,
                            placeholder="Deporte",
                            on_change=PacienteState.set_deporte,
                            width="100%",
                            variant="soft",
                            color_scheme="blue"
                        ),
                        rx.input(
                            value=PacienteState.fecha_ultima_consulta, 
                            type="date", 
                            on_change=PacienteState.set_fecha_ultima_consulta,
                            width="100%",
                            variant="soft",
                            color_scheme="blue"
                        ),
                        # Reemplazo del alert por un text con estilo de error
                        rx.cond(
                            PacienteState.error_msg != "",
                            rx.text(
                                PacienteState.error_msg, 
                                color="red.500", 
                                font_weight="bold"
                            )
                        ),                 
                        
                        rx.button(
                            "Agregar Paciente", 
                            on_click=PacienteState.agregar_paciente,
                            color_scheme="blue",
                            size="3",
                            width="100%"
                        ),
                        spacing="4",
                        width="100%",
                        align="center"
                    ),
                ),
                rx.divider(
                    margin_y="2rem",
                    color_scheme="blue"
                ),
                spacing="4",
                width="100%",
                align="center",
                padding_x="8rem",
                margin_top="2rem"
            ),
            columns=[1, 1, 1], 
            width="100%",
            padding_x="10rem"
        ),
        footer(),
        spacing="0",
        background="gray.50",
        min_height="100vh",
        width="100%",
        align="center"
    )

# Ejecutar la aplicación Reflex
if __name__ == "__main__":
    app = rx.App()
    app.add_page(pacientes)
    app.compile()