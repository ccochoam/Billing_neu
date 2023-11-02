import pandas as pd
import os

def calculate_energy_bill(consumption_sept_df, injection_sept_df):
    # Calcular EA (Energía Activa)
    ea, consumption_total, cu_negative = calculate_ea(consumption_sept_df)

    # Calcular EC (Comercialización de Excedentes de Energía)
    ec, injection_total = calculate_ec(injection_sept_df)

    # Calcular EE1 (Excedentes de Energía Tipo 1)
    ee1 = min(injection_total, consumption_total) * cu_negative
    print(f"La ee1 es: {ee1}")

    # Calcular EE2 (Excedentes de Energía Tipo 2)
    ee2 = calculate_ee2(injection_total, consumption_total, consumption_sept_df, injection_sept_df)

    return {
        'EA': ea,
        'EE1': ee1,
        'EE2': ee2,
        'EC': ec
    }

def calculate_ea(consumption_sept_df):
    ea = consumption_sept_df['result']
    print(f"El ea es: {ea}")
    consumption_total = sum(consumption_sept_df['value'])
    print(f"La consumption_total es: {consumption_total}")
    cu_negative = -consumption_sept_df['cu']
    print(f"La cu_negativo es: {cu_negative}")
    return ea, consumption_total, cu_negative

def calculate_ec(injection_sept_df):
    ec = injection_sept_df['result']
    print(f"El ec es: {ec}")
    injection_total = sum(injection_sept_df['value'])
    print(f"La injection_total es: {injection_total}")
    return ec, injection_total

def calculate_ee2(injection_total, consumption_total, consumption_sept_df, injection_sept_df):
    if injection_total <= consumption_total:
        return 0
    else:
        return (consumption_total - injection_total) * get_hourly_rate(consumption_sept_df, consumption_total, injection_sept_df, injection_total)
    print(f"La ee2 es: {ee2}")

def get_hourly_rate(injection_sept_df, injection_total, consumption_total):
    tariff_hour = []
    for index, row in injection_sept_df.iterrows():
        tariff_hour.append(row['data_hourly'])

    return sum(tariff_hour)