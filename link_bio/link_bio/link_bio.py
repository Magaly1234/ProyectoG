import reflex as rx
from link_bio.View.Page.index import index
from link_bio.View.Page.panel_control import panel_control
from link_bio.View.Page.pacientes import pacientes
from link_bio.View.Page.lista_pacientes import lista_pacientes
from link_bio.View.Page.monitoreo import monitoreo
from link_bio.View.Page.reportes import reportes
from link_bio.Api.api import hello

# Definir el estado de la aplicación
class State(rx.State):
    pass  # Aquí puedes definir variables de estado si es necesario

# Crear la aplicación correctamente
app = rx.App()

# Agregar las páginas
app.add_page(index, route="/")
app.add_page(panel_control, route="/panel_control")
app.add_page(pacientes, title="Gestión de Pacientes", route="/pacientes")
app.add_page(lista_pacientes, route="/lista_pacientes")
app.add_page(monitoreo, route="/monitoreo")
app.add_page(reportes, route="/reportes")

# Agregar la API
app.api.add_api_route("/hello", hello)
