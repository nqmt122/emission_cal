import streamlit as st
import pandas as pd

# Create an empty DataFrame to store the records
record_df = pd.DataFrame(columns=["Start", "Destination", "Distance (km)", "Cargo Weight (kg)", "Truck Weight (kg)", "CO2 Emissions"])

# Data
fuel_lookup = {
    'min_ton': [0, 1, 1.5, 2, 2.5, 3.5, 5, 7, 8, 10.9, 15, 16.5, 18, 19, 22, 28],
    'max_ton': [1, 1.5, 2, 2.5, 3.5, 5, 7, 8, 10.9, 15, 16.5, 18, 19, 22, 28, 32],
    'avg_fuel': [6.5, 7, 8, 9, 10, 11, 12, 14, 16, 24, 26, 28, 29, 29, 30, 30]
}

df = pd.DataFrame(fuel_lookup)

# Calculation
def co2_cal(distance, cargo_weight, truck_weight):
    def get_fuel(truck):
        mask = (truck >= df['min_ton']) & (truck <= df['max_ton'])
        if mask.any():
            return df.loc[mask, 'avg_fuel'].iloc[0]
        return None

    truck_type_do_rate = get_fuel(truck_weight)
    cargo_do_rate = cargo_weight * 1.3
    total_fuel = (truck_type_do_rate + cargo_do_rate) * distance / 100
    co2_emissions = total_fuel * 2.68

    return co2_emissions

# Call
def main():
    st.title("CO2 Emissions Calculator")

    # Input variables
    start = st.text_input("Start Location")
    destination = st.text_input("Destination Location")
    distance = st.number_input("Distance (in km)", min_value=0.0, step=0.1)
    cargo_weight = st.number_input("Cargo Weight (in kg)", min_value=0.0, step=1.0)
    truck_weight = st.number_input("Truck Weight (in kg)", min_value=0.0, step=1.0)

    # Calculate CO2 emissions
    co2_emissions = co2_cal(distance, cargo_weight, truck_weight)

    # Display the result
    st.subheader("Result")
    st.write("Start:", start)
    st.write("Destination:", destination)
    st.write("Distance:", distance, "km")
    st.write("CO2 Emissions:", co2_emissions)

    # Record the result in the DataFrame
    record_df.loc[len(record_df)] = [start, destination, distance, cargo_weight, truck_weight, co2_emissions]

    # Display the record table
    st.subheader("Record")
    st.table(record_df)

if __name__ == "__main__":
    main()
