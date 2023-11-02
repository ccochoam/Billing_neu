import pandas as pd
from dbConexion import get_data_db
from calculate import calculate_energy_bill
import addLog

def start_services():
    print("run service")
    consumption_sept_df = get_data('GetTotalEA()', ['id_record','value','cu','record_timestamp','data_hourly','result'])
    injection_sept_df = get_data('GetTotalEC()', ['id_record','value','cu','result'])
    
    result_billing = calculate_energy_bill(consumption_sept_df, injection_sept_df)
    addLog.write_txt(result_billing) #log para seguimiento de respuesta
    return result_billing
    
def get_data(function_name, column_names):
    query = 'select * from ' + function_name
    data = get_data_db(query)
    df = pd.DataFrame(data, columns=column_names)
    return df