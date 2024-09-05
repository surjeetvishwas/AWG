# import libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# =============================================================================
steamTable=pd.read_excel(r'H2O_TempSat.xls')

data = steamTable.drop(steamTable.index[[0,1,51,52]], axis = 0)
relevant_data = data[['Water Saturation Properties  - Temperature Table', 'Unnamed: 1']]
col_name = relevant_data.columns


# function to estimate saturate vapor pressure for given temperature
# =============================================================================
def sat_vap_p(t, df = relevant_data):
    p_table = df[df.columns[1]]
    t_table = df[df.columns[0]]

    if (t >= 0.01) & (t < 373.95):
        # do interpolation
        y1 = p_table[t_table <= t].iloc[-1]
        y2 = p_table[t_table > t].iloc[0]
        x1 = t_table[t_table <= t].iloc[-1]
        x2 = t_table[t_table > t].iloc[0]

        y = ((t-x1) * ((y2-y1)/(x2-x1))) + y1
        return y*7500.62

    elif t >= 373.95:
        # do exterpolation
        y = ((t-379.95) * ((22.064-21.044)/(373.95-370))) + 22.064
        return y*7500.62
    elif t < 0.01:
        # do exterpolation
        y = ((t-.01) * ((0.00087258-0.00061165)/(5-0.01))) + 0.00061165
        y = y if y > 0 else 0
        return y*7500.62

# =============================================================================
# function to estimate flow rate
# =============================================================================
def flow_calc(p1,v1,t1,rh,t2, p2,p,v,t):
    # convert temperature in Kelvin
    t1_K = t1 + 273.15
    t2_K = t2 + 273.15
    t_K = t + 273.15

    # mole fractions (inlet air)
    y1_wat_vap = rh * sat_vap_p(t1) / p1  # mole fraction of water vapour in inlet air
    y1_dry_air = 1 - y1_wat_vap  # mole fraction of dry air (in inlet air)

    # volumetric flow rate
    m1 = (p1*v1/t1_K) / (p*v/t_K)  # volumetric flow rate of dry air at inlet (kmol/min)

    # mole fractions (outlet air)
    y2_wat_vap = sat_vap_p(t2) / p2  # mole fraction of water vapour in outlet air
    y2_dry_air = 1 - y2_wat_vap  # mole fraction of dry air (in outlet air)

    # volumetric flow rate (using dry air balance)
    m2 = (y1_dry_air * m1) / y2_dry_air # volumetric flow rate of dry air at outlet (kmol/min)

    # water balance
    m3 = (m1*y1_wat_vap) - (m2*y2_wat_vap)  # volumetric flow rate of condensed water (in kmol/min)
    m3 = m3 if m3 > 0 else 0

    # flow rate of condensed water
    water_flow_rate = m3 * 1000 * 18  # (in g/min)
    water_condensed_per_hour = water_flow_rate * 60 / 1000  # (in kg)

    return (y1_wat_vap, y1_dry_air, y2_wat_vap, y2_dry_air, m1, m2, m3, \
            water_flow_rate, water_condensed_per_hour, p1,v1,t1,rh,t2,p2)

