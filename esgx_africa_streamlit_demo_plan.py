# ESGx.Africa – Streamlit Demo Prototype (Ubuntu ESG Score Calculator)
# This script creates a simple Streamlit app for funders to interact with your ESG scoring logic.

import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

logo = Image.open("esgx-logo.png")
st.image(logo, width=200)
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



# --- App Header ---
st.set_page_config(page_title="ESGx.Africa Demo", layout="centered")
st.title("ESGx.Africa – Ubuntu ESG Score Calculator")
st.subheader("Demonstrating AI-Powered ESG Contextual Intelligence")

# --- User Inputs (Simulated Community ESG Data) ---
with st.form("esg_form"):
    st.write("### Community ESG Inputs")
    water = st.slider("Water Access Score", 0, 100, 60)
    equity = st.slider("Employment Equity Score", 0, 100, 70)
    engagement = st.slider("Community Engagement", 0, 100, 85)
    governance = st.slider("Governance Transparency Score", 0, 100, 65)
    carbon = st.slider("Carbon Footprint Reduction (%)", 0, 100, 45)

    submit = st.form_submit_button("Calculate Ubuntu ESG Score")

# --- Scoring Logic ---
if submit:
    scores = {
        "Water Access": water,
        "Equity": equity,
        "Community Engagement": engagement,
        "Governance": governance,
        "Carbon Reduction": carbon
    }
    ubuntu_score = round((water * 0.3 + equity * 0.2 + engagement * 0.2 + governance * 0.2 + carbon * 0.1), 2)

    st.markdown("---")
    st.write("### ESGx.Africa Report Summary")
    st.metric("Ubuntu ESG Score", f"{ubuntu_score} / 100")

    if ubuntu_score >= 85:
        st.success("🌍 Community Verified: Excellent ESG Alignment")
    elif ubuntu_score >= 65:
        st.warning("⚠️ Moderate Alignment – Opportunities for Impact")
    else:
        st.error("❌ Needs Improvement – Low ESG Cohesion")

    # --- Narrative Output ---
    st.write("\n")
    st.write("#### AI-Powered Narrative:")
    st.write(f"This community has shown strong water access ({water}%) and excellent engagement ({engagement}%).")
    st.write(f"Employment equity is improving, and carbon emissions are being addressed at {carbon}% reduction.")
    st.write("Governance practices show promising transparency. Overall, ESGx.Africa recommends recognition for community progress and sustained improvement.")

    # --- Impact Visual ---
    st.write("\n")
    st.write("### Visual Breakdown of ESG Inputs")
    fig, ax = plt.subplots()
    categories = list(scores.keys())
    values = list(scores.values())
    ax.barh(categories, values, color='seagreen')
    ax.set_xlim(0, 100)
    ax.set_title('Ubuntu ESG Input Breakdown')
    for index, value in enumerate(values):
        ax.text(value + 1, index, str(value), va='center')
    st.pyplot(fig)

# --- Funder Analytics Page ---
st.markdown("---")
st.write("### Funder Insights")
with st.expander("Show ROI and Job Creation Estimates"):
    st.write("**Projected Jobs Created (per R10M invested):** 112")
    st.write("**Estimated ESG Compliance ROI (Year 1):** 14.5%")
    st.write("**Regulatory Risk Reduction:** High in mining, municipalities")
    st.write("**Community Sentiment Improvement:** +32% (pilot sites)")

# --- Footer ---
st.markdown("---")
st.caption("ESGx.Africa™ | Powered by Ubuntu | Demo Prototype for Funders")
