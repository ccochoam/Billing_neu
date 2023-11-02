from service import start_services

def main():
    print("Bienvenido a Facturación de Energía")
    
    result_billing = start_services()
    
    print("Resultado de la factura de energía:")
    print(result_billing)

if __name__ == "__main__":
    main()
