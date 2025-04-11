from link_bio.db.db_operation import obtener_pacientes

def main():
    print("🔍 Probando conexión a la base de datos...")
    pacientes = obtener_pacientes()
    
    if pacientes is None:
        print("\n❌ Error: No se pudo conectar a la base de datos o hubo un error en la consulta")
    elif not pacientes:
        print("\n✅ Conexión exitosa pero no hay pacientes registrados")
    else:
        
        
        print("\n✅ Conexión exitosa. Pacientes encontrados:")
        print("-" * 50)
        for idx, paciente in enumerate(pacientes, 1):
            print(f"{idx}. ID: {paciente['id']}")
            print(f"   Nombre: {paciente['nombre']}")
            print(f"   Edad: {paciente['edad']}")
            print(f"   Lesión: {paciente['lesion']}")
            print("-" * 50)

if __name__ == "__main__":
    main()