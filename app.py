import streamlit as st

st.set_page_config(page_title="AIGOBIZ", page_icon="🤖", layout="wide")

st.title("Welcome to AIGOBIZ 🤖🛒")
st.write("This is your first Streamlit app. Replace this with your dashboard or demo.")

tab1, tab2 = st.tabs(["Overview", "Demo"])

with tab1:
    st.subheader("What we do")
    st.markdown("We optimize assortment, pricing, and promotions using AI/ML + operations research.")

with tab2:
    st.subheader("Tiny Demo")
    price = st.slider("Price", 1.0, 100.0, 25.0, 0.5)
    demand = max(0, 120 - 1.2 * price)  # toy curve
    gmv = price * demand
    st.metric("Estimated Demand (toy)", f"{int(demand)} units")
    st.metric("GMV (toy)", f"${gmv:,.0f}")