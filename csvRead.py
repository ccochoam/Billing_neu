import pandas as pd
import os

def read_csv(csv_file_path):
    try:
        if os.path.exists(csv_file_path):
            return lambda csv_file_path: pd.read_csv(csv_file_path)
        else:
            print("El archivo no existe.")
            return None

    except FileNotFoundError:
        print("El archivo no existe.")
        return None
