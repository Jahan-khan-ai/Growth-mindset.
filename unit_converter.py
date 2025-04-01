import streamlit as st

# Title of the application
st.title("***Unit Converter***")

# show unit type
unit_type = st.selectbox("***Select Unit Type***",["Length", "Weight", "Temperature"])


# Function to convert length
def convert_length(value, from_unit, to_unit):
    length_conversions = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "inches": 0.0254,
        "feet": 0.3048,
        "yards": 0.9144,
        "miles": 1609.34
    }
    return value * length_conversions[from_unit] / length_conversions[to_unit]

# Function to convert weight
def convert_weight(value, from_unit, to_unit):
    weight_conversions = {
        "grams": 1,
        "kilograms": 1000,
        "milligrams": 0.001,
        "pounds": 453.592,
        "ounces": 28.3495
    }
    return value * weight_conversions[from_unit] / weight_conversions[to_unit]

# Function to convert temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
        else:
            return value

    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
        else:
            return value
            
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value

# Main interface
if unit_type == "Length":
    st.header("Length Converter")
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards", "miles"])
    with col2:
        to_unit = st.selectbox("To", ["meters", "kilometers", "centimeters", "millimeters", "inches", "feet", "yards", "miles"])
    value = st.number_input("Enter value", min_value=0.0)
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif unit_type == "Weight":
    st.header("Weight Converter")
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("***From***", ["grams", "kilograms", "milligrams", "pounds", "ounces"])
    with col2:
        to_unit = st.selectbox("***To***", ["grams", "kilograms", "milligrams", "pounds", "ounces"])
    value = st.number_input("***Enter value***", min_value=0.0)
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif unit_type == "Temperature":
    st.header("Temperature Converter")
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("***From***", ["celsius", "fahrenheit", "kelvin"])
    with col2:
        to_unit = st.selectbox("***To***", ["celsius", "fahrenheit", "kelvin"])
    value = st.number_input("Enter value")
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")