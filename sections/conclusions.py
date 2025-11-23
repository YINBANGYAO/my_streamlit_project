import streamlit as st

def show_quality_report(df):
    st.markdown("---")
    with st.expander("🔍 数据质量与局限性 (Data Quality & Limitations)"):
        st.markdown("""
        **数据来源**: Global Mobile Prices 2025 Dataset.
        
        **质量检查 (Quality Checks):**
        * **完整性**: 检查了缺失值 (Null Values)。
        * **一致性**: 确保 'Release Month' 按照时间顺序而非字母顺序排序。
        
        **局限性 (Limitations):**
        * 数据仅包含2025年发布的机型，不代表历史市场存量。
        * 价格为美元计价的全球平均价格，未考虑地区税费差异。
        """)
        
        if st.checkbox("显示原始数据样本"):
            st.dataframe(df.head(10))