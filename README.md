# 📱 2025 Smartphone Market Pulse (Data Storytelling App)

**Author**: Yin Bangyao (Student ID: 4320251020)  
**Course**: WUT2025  ERFEI
**Date**: 2025

## 📖 Project Overview
This Streamlit application is a data storytelling dashboard analyzing the 2025 smartphone market. 
Moving from **Descriptive Analytics** (market overview) to **Diagnostic Analytics** (price vs. performance), it aims to answer the question: *Does a higher price always mean better hardware?*

### Key Features
* **Interactive Dashboard**: Filter by Brand, OS, and Price.
* **Advanced Visualizations**: 
    * Scatter Plots with Trend Lines (Regression).
    * Small Multiples for distribution analysis.
    * Heatmaps for temporal trends.
* **Data Engineering**: Modular code structure with cached data loading.

## 📂 Project Structure
The project follows a modular engineering structure for maintainability:

```text
.
├── app.py                  # Main application entry point
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── Global_Mobile_Prices_2025_Fixed.csv # Raw dataset
├── sections/               # UI Components
│   ├── intro.py            # Headers & Sidebar logic
│   ├── overview.py         # KPI Metrics
│   ├── deep_dives.py       # Analysis Tabs & Visualizations
│   └── conclusions.py      # Data Quality Report
└── utils/                  # Helper Functions
    ├── io.py               # Data Ingestion & Caching
    ├── prep.py             # Data Cleaning & Transformation
    └── viz.py              # Altair Chart Definitions