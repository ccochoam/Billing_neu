from services import start_services

def main():
    print("Bienvenido a ProyectoEnergia")
    
    resultado_factura = start_services()
    
    print("Resultado de la factura de energía:")
    print(resultado_factura)

if __name__ == "__main__":
    main()
