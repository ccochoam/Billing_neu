import os
import datetime
import json

def write_txt(res):
    res_list = list(res)
    print('res')
    print(res['EA'])
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    path = 'neu_billing/logs/'
    nombre_archivo = f'{path}mi_archivo_{timestamp}.txt'
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("res['EA']")
        json.dump(res['EA'].to_dict(), archivo)
        archivo.write("\n")
        archivo.write("res['EE1']")
        json.dump(res['EE1'].to_dict(), archivo)
        archivo.write("\n")
        archivo.write("res['EE2']")
        json.dump(res['EE2'], archivo)
        archivo.write("\n")
        archivo.write("res['EC']")
        json.dump(res['EC'].to_dict(), archivo)
        archivo.write("\n")