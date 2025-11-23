import streamlit as st
import os

def show_header():
    st.title("📱 2025 Smartphone Market Pulse")
    st.markdown("""
    **核心问题 (The Question):** 在2025年的智能手机市场，高昂的价格是否一定意味着更好的硬件规格？
    Android 与 iOS 在定价策略上是否存在根本性差异？
    """)

def show_sidebar_methodology():
    # --- 1. Logo 区域 ---
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        if os.path.exists("assets/logo1.png"):
            # 修改点：将 use_container_width 改为 use_column_width
            st.image("assets/logo1.png", use_column_width=True)
        else:
            st.warning("Logo1 missing")

    with col2:
        if os.path.exists("assets/logo2.png"):
            # 修改点：将 use_container_width 改为 use_column_width
            st.image("assets/logo2.png", use_column_width=True)
        else:
            st.warning("Logo2 missing")

    # --- 2. 原有标题与内容 ---
    st.sidebar.title("📱 2025 Market Pulse")
    st.sidebar.markdown("---")
    
    with st.sidebar.expander("📊 项目方法论 (Methodology)"):
        st.markdown("""
        **Role: Data Analyst**
        本项目遵循数据分析流程，从**描述性分析** (Descriptive) 走向**诊断性分析** (Diagnostic)。
        
        **Visualization Strategy:**
        基于 *Chart Suggestion Guide* 选择图表：
        * **Relationship**: 散点图 (Scatter) 用于探索价格与性能的权衡。
        * **Distribution**: Small Multiples 用于对比不同 OS 的价格分布。
        * **Trend**: 热力图用于展示发布时间节奏。
        """)
        st.caption("Reference: MS Learn Data Analyst Path & Abela's Chart Guide")