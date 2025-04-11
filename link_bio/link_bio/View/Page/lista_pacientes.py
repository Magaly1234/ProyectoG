import reflex as rx
from typing import List, Dict, Any
from link_bio.Components.menu import menu
from link_bio.Components.header import header
from link_bio.Components.footer import footer
from link_bio.db.db_operation import obtener_pacientes

class Paciente(rx.Base):
    """Modelo de datos para un paciente"""
    id: str
    nombre: str
    edad: str
    deporte: str
    estado_tratamiento: str
    fecha_ultima_consulta: str
    observaciones: str

class PacientesState(rx.State):
    """Estado para manejar la lista de pacientes"""
    pacientes: List[Paciente] = []
    
    def cargar_pacientes(self):
        """Método para cargar/actualizar la lista de pacientes"""
        # Convierte los diccionarios a objetos Paciente
        datos_raw = obtener_pacientes() or []
        self.pacientes = [
            Paciente(
                id=str(p.get('id', 'N/A')),
                nombre=p.get('nombre', 'Desconocido'),
                edad=str(p.get('edad', 'No especificada')),
                deporte=p.get('deporte', 'No especificada'),
                estado_tratamiento=p.get('estado_tratamiento', 'Desconocido'),
                fecha_ultima_consulta=self.format_date(p.get('fecha_ultima_consulta')),
                observaciones=p.get('observaciones', 'Desconocido')
            ) for p in datos_raw
        ]
    
    @staticmethod
    def format_date(date):
        """Convierte la fecha a una cadena de texto legible"""
        if not date:
            return "No especificada"
        try:
            return date.strftime("%d-%m-%Y")
        except:
            return str(date)
        
def menu_desplegable() -> rx.Component:
        """Menú desplegable para seleccionar un paciente"""
        return rx.select(
            options=[rx.option(value=p.id, children=p.id) for p in PacientesState.pacientes],
            placeholder="Selecciona un paciente",
            id="paciente_select"
        )

def lista_pacientes() -> rx.Component:
    """Página principal de pacientes con tabla organizada"""

    def create_patient_table() -> rx.Component:
        """Crea una tabla organizada de pacientes"""
        return rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("ID"),
                    rx.table.column_header_cell("Nombre"),
                    rx.table.column_header_cell("Edad"),
                    rx.table.column_header_cell("Deporte"),
                    rx.table.column_header_cell("Estado del Tratamiento"),
                    rx.table.column_header_cell("Fecha Última Consulta"),
                    rx.table.column_header_cell("Observaciones"),
                )
            ),
            rx.table.body(
                rx.foreach(
                    PacientesState.pacientes,
                    lambda p: rx.table.row(
                        rx.table.cell(p.id),
                        rx.table.cell(p.nombre),
                        rx.table.cell(p.edad),
                        rx.table.cell(p.deporte),
                        rx.table.cell(p.estado_tratamiento),
                        rx.table.cell(p.fecha_ultima_consulta),
                        rx.table.cell(p.observaciones)
                    )
                )
            ),
            variant="surface",
            size="2",
            width="100%",
            max_width="900px"
        )

    return rx.vstack(
        header(),
        rx.hstack(  # Sección de menú + contenido en dos columnas
            rx.box(
                menu(),
                width="250px",  
                min_width="250px",
                background="white",
                height="100vh",
                overflow="hidden",
                box_shadow="md"
            ),
            rx.box(
                rx.vstack(
                    rx.heading("Lista de Pacientes", size="6"),
                    create_patient_table(),
                    rx.button(
                        "Actualizar Lista", 
                        on_click=PacientesState.cargar_pacientes,
                        color_scheme="blue",
                        variant="solid"
                    ),
                    spacing="4",
                    width="100%",
                    max_width="900px",  
                    align="center",
                    padding="2rem"
                ),
                width="100%",
                padding_left="2rem",
                padding_right="2rem"
            ),
            align="start",
            width="100%",
        ),
        footer(),
        spacing="0",
        background="gray.50",
        min_height="100vh",
        width="100%",
        align="center",
        padding_bottom="2rem"
    )

# Ejecuta la aplicación Reflex
if __name__ == "__main__":
    app = rx.App(state=PacientesState)
    app.add_page(lista_pacientes)
    app.compile()
