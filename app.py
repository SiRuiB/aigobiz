import streamlit as st

st.set_page_config(page_title="AIGOBIZ", page_icon="🤖", layout="wide")

tab1, tab2 = st.tabs(["Overview", "Demo"])
with tab1: st.markdown("Your pitch…")
with tab2: st.metric("GMV (toy)", "$12,345")

[theme]
primaryColor="#0E7AFE"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F6F8FB"
textColor="#0A0A0A"

st.title("Welcome to AIGOBIZ 🤖🛒")
st.write("This is your first Streamlit app. Replace this text with your own dashboard or analysis.")

price = st.slider("Price", 1.0, 100.0, 25.0, 0.5)
demand = max(0, 120 - 1.2 * price)
gmv = price * demand

st.metric("Estimated Demand", f"{int(demand)} units")
st.metric("GMV (toy example)", f"${gmv:,.0f}")