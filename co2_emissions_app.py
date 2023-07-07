import streamlit as st
import pandas as pd

# Data
fuel_lookup = {
    'Min Tonne': [0, 1, 1.5, 2, 2.5, 3.5, 5, 7, 8, 10.9, 15, 16.5, 18, 19, 22, 28],
    'Max Tonne': [1, 1.5, 2, 2.5, 3.5, 5, 7, 8, 10.9, 15, 16.5, 18, 19, 22, 28, 32],
    'Average Fuel Consumption': [6.5, 7, 8, 9, 10, 11, 12, 14, 16, 24, 26, 28, 29, 29, 30, 30]
}

df = pd.DataFrame(fuel_lookup)

# Calculation

def co2_cal(distance, cargo_weight,truck_weight):
    #write code to filter truck_type_do_rate by truck_weight
    def get_fuel(truck):
        mask = (truck >= df['Min Tonnes']) & (truck <= df['Max Tonnes'])
        if mask.any():
            return df.loc[mask, 'Average Fuel Consumption'].iloc[0]
        return None
    truck_type_do_rate = get_fuel(truck_weight)
    #cargo_do_rate
    cargo_do_rate = cargo_weight * 1.3
    #total_fuel
    total_fuel = (truck_type_do_rate + cargo_do_rate) * distance/100
    co2_emissions = total_fuel * 2.68   
    return co2_emissions

# Call

def main():
    st.title("CO2 Emissions Calculator")
    
    # Input variables
    distance = st.number_input("Distance (in km)", min_value=0.0, step=0.1)
    cargo_weight = st.number_input("Cargo Weight (in kg)", min_value=0.0, step=1.0)
    truck_weight = st.number_input("Truck Weight (in kg)", min_value=0.0, step=1.0)

    # Calculate CO2 emissions
    co2_emissions = co2_cal(distance, cargo_weight, truck_weight)

    # Display the result
    st.subheader("Result")
    st.write("CO2 Emissions:", co2_emissions)

if __name__ == "__main__":
    main()