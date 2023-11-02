import psycopg2 as ps

db_params = {
    'database': 'BillingNeuDB',
    'user': 'postgres',
    'password': '[Agregar clave]',
    'host': 'localhost',
    'port': '5432'
}

def get_data_db(query):
    try:
        connection = ps.connect(**db_params)
        cursor = connection.cursor()
        cursor.execute(query)
        
        results = cursor.fetchall()

        cursor.close()
        connection.close()
        
        return results

    except (Exception, ps.Error) as error:
        print("Error al conectarse a la base de datos:", error)