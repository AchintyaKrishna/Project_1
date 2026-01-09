import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Ola Ride Insights",
    layout="wide"
)

# ---------------- GLOBAL STYLING (TABLEAU-LIKE) ----------------
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
            padding-left: 1.5rem;
            padding-right: 1.5rem;
            padding-bottom: 1rem;
        }

        h1, h2, h3 {
            text-align: center;
        }

        iframe {
            width: 100% !important;
        }

        .insight-box {
            background-color: #1f2933;
            padding: 14px;
            border-left: 6px solid #22c55e;
            border-radius: 6px;
            font-size: 16px;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- LOAD DATA (CACHED) ----------------
@st.cache_data
def load_data():
    return pd.read_csv("OLA_CLEANED.csv")

df = load_data()

# ---------------- TITLE ----------------
st.markdown(
    "<h1>🚖 Ola Ride Insights 🚖</h1>",
    unsafe_allow_html=True
)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------- KPI ROW (FROM FULL DATA) ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Rides", f"{df['Booking_ID'].nunique():,}")

with col2:
    st.metric("Total Revenue (₹)", f"{int(df['Booking_Value'].sum()):,}")

with col3:
    st.metric("Overall Avg Customer Rating", round(df['Customer_Rating'].mean(), 1))

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- KEY INSIGHT (CALLOUT) ----------------
st.markdown(
    """
    <div class="insight-box">
        Most rides are completed successfully (62%), with peak demand occurring during mid-week evenings. 
        This highlights opportunities for optimized driver allocation and surge pricing during high-demand periods.
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- TABLEAU SECTION HEADER ----------------
st.markdown(
    "<h2>📊 OLA Ride Dashboard 📊</h2>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- TABLEAU EMBED (NO WIDTH CUT ISSUE) ----------------
st.components.v1.iframe(
    "https://public.tableau.com/views/Ola_Ride/OlaRideInsightsDashboard?:showVizHome=no&:embed=true",
    height=950,
    scrolling=True
)
