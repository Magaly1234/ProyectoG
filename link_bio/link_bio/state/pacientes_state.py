import reflex as rx
from typing import List, Dict, Any
from link_bio.db.db_connection import db

class PacientesState(rx.State):
    """Estado para manejar los datos de pacientes"""
    pacientes: List[Dict[str, Any]] = []
    loading: bool = False
    error: str = ""
    
    async def cargar_pacientes(self):
        """Carga los pacientes desde la base de datos"""
        self.loading = True
        self.error = ""
        yield
        
        try:
            data = db.get_pacientes()
            if not data:
                self.error = "No se encontraron pacientes"
                print("No se encontraron pacientes en la base de datos")
            else:
                print(f"Se encontraron {len(data)} pacientes")
            self.pacientes = data
        except Exception as e:
            self.error = f"Error al cargar pacientes: {str(e)}"
            print(f"Error en cargar_pacientes: {e}")
        finally:
            self.loading = False