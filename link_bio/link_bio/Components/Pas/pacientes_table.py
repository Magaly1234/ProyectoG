import reflex as rx
from typing import Dict
from link_bio.state.pacientes_state import PacientesState

def paciente_row(paciente: Dict) -> rx.Component:
    """Componente para una fila de la tabla de pacientes"""
    return rx.tr(
        rx.td(paciente.get("id", "")),
        rx.td(paciente.get("nombre", "")),
        rx.td(paciente.get("edad", "")),
        rx.td(paciente.get("lesion", ""))
    )
def pacientes_table() -> rx.Component:
    """Tabla de pacientes"""
    return rx.box(
        rx.cond(
            PacientesState.error,
            rx.text(
                PacientesState.error,
                color="red.500",
                margin_bottom="1rem"
            ),
        ),
        rx.box(  # Cambiado de rx.table_container a rx.box
            rx.table(
                rx.thead(
                    rx.tr(
                        rx.th("ID"),
                        rx.th("Nombre"),
                        rx.th("Edad"),
                        rx.th("Lesión"),
                    )
                ),
                rx.tbody(
                    rx.cond(
                        len(PacientesState.pacientes) > 0,
                        rx.foreach(
                            PacientesState.pacientes,
                            paciente_row
                        ),
                        rx.tr(
                            rx.td(
                                rx.text("No hay pacientes registrados", color="gray.500"),
                                colspan=4,
                                text_align="center",
                                padding_y="2rem",
                            )
                        )
                    )
                ),
                variant="striped",
                size="3",
                width="100%",
            ),
            margin_y="1rem",
        ),
    )
