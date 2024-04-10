import streamlit as st
import pandas as pd

def load_data():
    data = pd.read_csv(r"C:\Users\shuod\Downloads\Lab12\Lab12\car_data.csv") 
    return data

data = load_data()

car_name = st.sidebar.text_input("Car Name", "")
transmission = st.sidebar.multiselect("Transmission", data['Transmission'].unique(), default=data['Transmission'].unique())
price_range = st.sidebar.slider("Selling Price", int(data['Selling_Price'].min()), int(data['Selling_Price'].max()), (int(data['Selling_Price'].min()), int(data['Selling_Price'].max())))
year_range = st.sidebar.slider("Year", int(data['Year'].min()), int(data['Year'].max()), (int(data['Year'].min()), int(data['Year'].max())))

if st.sidebar.button("Submit"):
    filtered_data = data
    if car_name:
        filtered_data = filtered_data[filtered_data['Car_Name'].str.contains(car_name, case=False)]
    if transmission:
        filtered_data = filtered_data[filtered_data['Transmission'].isin(transmission)]
    filtered_data = filtered_data[(filtered_data['Selling_Price'] >= price_range[0]) & (filtered_data['Selling_Price'] <= price_range[1])]
    filtered_data = filtered_data[(filtered_data['Year'] >= year_range[0]) & (filtered_data['Year'] <= year_range[1])]

    st.write(filtered_data)
else:
    st.write(data)
