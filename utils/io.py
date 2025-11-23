import pandas as pd
import streamlit as st

@st.cache_data
def load_data(file_path='Global_Mobile_Prices_2025_Fixed.csv'):
    """
    Ingest raw CSV data.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"Critical Error: Dataset '{file_path}' not found. Please ensure it is in the root directory.")
        st.stop()