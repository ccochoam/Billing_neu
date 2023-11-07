import read_file as rf

def start_services():
    print("run services")
    services_df = rf.read_csv('services.csv').sort_values(by='id_service')    
    consumption_sept_df = rf.read_csv('consumption.csv')
    injection_sept_df = rf.read_csv('injection.csv')
    tariffs_df = rf.read_csv('tariffs.csv')
    records_df = rf.read_csv('records.csv')
    res = []

    for index, row in services_df.iterrows():
        print('-------------------------------------------------')
        record_service = records_df[records_df['id_service'] == row['id_service']]
        cu_tariff, c_tariff = get_tariff(row, tariffs_df)
        print(f'{'cu_tariff: '}{cu_tariff}')
        print(f'{'c_tariff: '}{c_tariff}')
        consumption_sum = get_sum(record_service, consumption_sept_df)
        print(f'{'consumption_sum: '}{consumption_sum}')
        ea = consumption_sum * cu_tariff
        print(f'{'ea: '}{ea}')
        injection_sum = get_sum(record_service, injection_sept_df)
        print(f'{'injection_sum: '}{injection_sum}')
        ec = injection_sum * c_tariff
        print(f'{'ec: '}{ec}')
        ee1 = min(injection_sum, consumption_sum) * -cu_tariff
        print(f'{'ee1: '}{ee1}')
        ee2 = get_ee2(injection_sum, consumption_sum, record_service, consumption_sept_df, injection_sept_df)
        print(f'{'ee2: '}{ee2}')
        data = {'id_service': row['id_service'], 'EA': ea, 'EE1': ee1, 'EE2': ee2, 'EC': ec}
        res.append(data)
        print(f'{'data: '}{data}')
    return res

def get_ee2(injection_sum, consumption_sum, record_service, consumption_sept_df, injection_sept_df):
    if injection_sum <= consumption_sum:
        return 0
    else:
        valcon = (consumption_sum - injection_sum) * get_hourly_rate(record_service, consumption_sept_df, injection_sept_df)
        print('valcon')
        print(valcon)
        return valcon

def get_hourly_rate(record_service, consumption_sept_df, injection_sept_df):
    print("record_service")
    print(record_service)
    xm_data_hourly_per_agent_df = rf.read_csv('xm_data_hourly_per_agent.csv')
    sum = 0
    for index, row in record_service.iterrows():
        dh_value, cons_value, inj_value = 0, 0, 0
        data_hourly_value = xm_data_hourly_per_agent_df[xm_data_hourly_per_agent_df['record_timestamp'] == row['record_timestamp']]
        for index, rowDH in data_hourly_value.iterrows():
            dh_value = rowDH['value']

        consumption_value = consumption_sept_df[consumption_sept_df['id_record'] == row['id_record']]
        for index, rowC in consumption_value.iterrows():
            cons_value = rowC['value']
            #print(f'{'cons_value'}{cons_value}')
            if cons_value == None:
                cons_value = 0

        # injection_value = injection_sept_df[injection_sept_df['id_record'] == row['id_record']]
        # for index, rowI in injection_value.iterrows():
        #     inj_value = rowI['value']
        #     #print(f'{'cons_value'}{cons_value}')
        #     if inj_value == None:
        #         inj_value = 0
        # if inj_value > cons_value:
            sum += dh_value * cons_value
    print(f'{'sum: '}{sum}')
    return sum

def get_tariff(row_service, tariffs_df):
    print("row_service['voltage_level']")
    print(row_service['voltage_level'])
    if row_service['voltage_level'] in (2,3):
        record_value = tariffs_df[tariffs_df['id_market'] == row_service['id_market']]
                                #& (tariffs_df['cdi'] == row_service['cdi'])]
        if record_value.empty:
            return 0, 0
        else:
            for index, row in record_value.iterrows():
                return row['CU'], row['C']
    else:
        record_value = tariffs_df[tariffs_df['id_market'] == row_service['id_market'] 
                                & (tariffs_df['cdi'] == row_service['cdi']) & (tariffs_df['voltage_level'] == row_service['voltage_level'])]        
        for index, row in record_value.iterrows():
            return row['CU'], row['C']

def get_sum(record_service, df):
    sum = 0
    for index, row in record_service.iterrows():
        record_value = df[df['id_record'] == row['id_record']]   
        # print('record_value:')
        # print(record_value)     
        for index, row_record_value in record_value.iterrows():
            sum += row_record_value['value']
    return sum