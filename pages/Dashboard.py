import streamlit as st
import pandas as pd
import plotly.express as px
from st_pages import hide_pages

# Set page config
st.set_page_config(page_title="Nuclear Power Plant Worker Dashboard", layout="wide")

hide_pages(["login"])

# Set dark theme styling
st.markdown(
    """
    <style>
        body {background-color: #1E1E2F; color: #C5C6E0;}
        .stMetric {background-color: #2C2C3A; padding: 10px; border-radius: 10px; text-align: center; color: white; display: flex; align-items: center; justify-content: center;}
        .center-text {text-align: center; font-size: 22px; font-weight: bold;}
        .large-text {font-size: 20px;}
        table {width: 100%; border-collapse: collapse; margin: 10px 0;}
        th, td {padding: 12px; border: 1px solid #C5C6E0; text-align: left;}
        th {background-color: #2C2C3A; color: white; text-align: left;}
        .top-right-container {display: flex; justify-content: flex-end; align-items: center; gap: 20px;}
        .logout-button {background-color: #FF5555; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;}
        .clock {font-size: 18px; font-weight: bold; color: #FFD700; text-align: right;}
    </style>
    """,
    unsafe_allow_html=True
)

# Top-right corner UI
top_right_col1, top_right_col2 = st.columns([4, 1])
with top_right_col2:
    if st.button("Logout", key="logout", help="Click to log out", on_click=lambda: st.switch_page("login")):
        st.switch_page("login")
    

# Sample data
data = {
    "Plant": ["Plant A", "Plant B", "Plant C", "Plant D"],
    "Sensor Count": [46, 1, 2, 2],
    "Risk Category": ["Normal", "Broken", "Recovery", "At Risk"]
}
df = pd.DataFrame(data)

# Header
st.title("Metrics Platform")

# Centered Pie Chart
st.subheader("Sensor Count Based on Categories")
fig_severity = px.pie(df, names='Risk Category', values='Sensor Count', title='', color_discrete_sequence=['#8A2BE2', '#6A5ACD', '#9370DB', '#483D8B'])
st.plotly_chart(fig_severity, use_container_width=True)

# Sensor Details
st.markdown("<h2 class='center-text'>🔍 Sensor Status</h2>", unsafe_allow_html=True)

def display_sensor_table(sensor_data):
    df_sensors = pd.DataFrame(sensor_data)
    df_sensors = df_sensors.style.set_table_styles([
        {"selector": "th", "props": [("text-align", "left")]},
        {"selector": "td", "props": [("text-align", "left")]}
    ])
    st.markdown(df_sensors.to_html(index=False, escape=False), unsafe_allow_html=True)

with st.expander("Normal Sensors"):
    normal_sensors = [{"Sensor Number": 20, "Sensor Name": "Spec Enthalpy Przr discharge (kJ/kg)"},
                      {"Sensor Number": 21, "Sensor Name": "Spec Enthalpy RCS leak (kJ/kg)"}]
    display_sensor_table(normal_sensors)

with st.expander("Broken Sensors"):
    broken_sensors = [{"Sensor Number": 22,"Sensor Name": "Temp of Molten Concrete (°C)",  "Current Value": "NaN", "Avg Value (24h)": "NaN", "Upper Bound": "NaN", "Lower Bound": "NaN", "Time Left": "NaN", "Rate of Change": "NaN", "Message": "Mechanical failure detected. Schedule immediate maintenance."}]
    display_sensor_table(broken_sensors)

with st.expander("At Risk Sensors"):
    at_risk_sensors = [
        {"Sensor Number": 46, "Sensor Name": "Temp PRZR Saturation (°C)", "Current Value": 231.3, "Avg Value (24h)": 173.2, "Upper Bound": 222.4, "Lower Bound": 74.3, "Time Left": "N/A", "Rate of Change": "N/A", "Message": "High temperature fluctuations detected. Inspect cooling system immediately."},
        {"Sensor Number": 36, "Sensor Name": "Level SG A Narrow Range (%)", "Current Value": 32.4, "Avg Value (24h)": 39.6, "Upper Bound": 65.4, "Lower Bound": 33.7, "Time Left": "N/A", "Rate of Change": "N/A", "Message": "Radiation levels approaching limits. Perform an emergency calibration."}
    ]
    display_sensor_table(at_risk_sensors)

with st.expander("Recovering Sensors"):
    recovering_sensors = [
        {"Sensor Number": 14,"Sensor Name": "Pressure RCS (Bars)",  "Current Value": 462.3, "Avg Value (24h)": 271.9, "Upper Bound": 242.3, "Lower Bound": 51.0, "Time Left": 10.3, "Rate of Change": -21.2, "Message": "System stabilizing after a fault. Monitor closely for the next 24 hours."},
        {"Sensor Number": 21,"Sensor Name": "Flow Reactor Coolant Loop (T/hr)", "Current Value": 632.1, "Avg Value (24h)": 702.4, "Upper Bound": 152.4, "Lower Bound": 75.6, "Time Left": 208.6, "Rate of Change": -2.3, "Message": "Recently rebooted. Ensure stable operation for the next cycle."}
    ]
    display_sensor_table(recovering_sensors)
