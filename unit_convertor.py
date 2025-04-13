import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="centered")

st.title("📏 Project 01: Unit Converter")
st.markdown("### Build a Google-style Unit Converter using Python & Streamlit")

# Unit options
unit_options = ["Metre", "Centimetre"]

# Input box
input_value = st.number_input("Enter value", min_value=0.0, value=1.0)

# Dropdowns for units
from_unit = st.selectbox("From", unit_options, index=0)
to_unit = st.selectbox("To", unit_options, index=1)

# Conversion logic
def convert_units(value, from_u, to_u):
    if from_u == "Metre" and to_u == "Centimetre":
        return value * 100
    elif from_u == "Centimetre" and to_u == "Metre":
        return value / 100
    else:
        return value

# Converted result
result = convert_units(input_value, from_unit, to_unit)

# Show result
st.markdown(f"## {input_value} {from_unit} = {result} {to_unit}")

# Formula
st.markdown("#### 🧮 Formula")
if from_unit == "Metre" and to_unit == "Centimetre":
    st.code("multiply the length value by 100")
elif from_unit == "Centimetre" and to_unit == "Metre":
    st.code("divide the length value by 100")
else:
    st.code("no conversion needed")
