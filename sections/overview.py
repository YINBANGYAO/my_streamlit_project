import streamlit as st

def show_kpis(df):
    st.subheader("1. 市场概览 (Market Overview)")

    col1, col2, col3, col4 = st.columns(4)

    avg_price = df['price_usd'].mean()
    avg_rating = df['rating'].mean()
    total_models = len(df)
    top_brand = df['brand'].mode()[0] if not df.empty else "N/A"

    col1.metric("平均价格 (Avg Price)", f"${avg_price:,.0f}", delta_color="inverse")
    col2.metric("平均评分 (Avg Rating)", f"{avg_rating:.1f}/5.0")
    col3.metric("样本量 (Sample Size)", total_models)
    col4.metric("主导品牌 (Top Brand)", top_brand)

    st.markdown("---")