import streamlit as st
from utils import viz

def show_charts(df_filtered, df_raw):
    st.subheader("2. 诊断性分析 (Diagnostic Analytics)")
    tab1, tab2, tab3 = st.tabs(["📈 价格 vs 性能", "🧩 操作系统分布", "🗓️ 发布趋势"])

    with tab1:
        st.subheader("价格的硬件溢价分析")
        st.caption("方法论: 使用 **散点图** 展示变量相关性与趋势线。")
        scatter_metric = st.radio("选择X轴硬件指标:", ["battery_mah", "camera_mp", "ram_gb"], horizontal=True, index=0)
        
        chart = viz.create_scatter(df_filtered, scatter_metric)
        st.altair_chart(chart, use_container_width=True)
        st.info(f"💡 **Key Insight**: 红线代表趋势。红线下方的数据点代表高性价比机型（相同配置下价格更低）。")

    with tab2:
        st.subheader("操作系统定价策略对比")
        st.caption("方法论: 使用 **Small Multiples** 替代单一图表，清晰展示不同组别的分布差异。")
        
        chart = viz.create_small_multiples(df_filtered)
        st.altair_chart(chart, use_container_width=True)
        st.info("📊 **分析**: Android 呈现长尾分布，覆盖所有价位；iOS 集中在高端区间。")

    with tab3:
        st.subheader("品牌发布日历")
        st.caption("方法论: 使用 **热力图** 消除线条重叠，展示季节性发布密度。")
        
        month_order = list(df_raw['release_month'].cat.categories)
        chart = viz.create_heatmap(df_filtered, month_order)
        st.altair_chart(chart, use_container_width=True)
        st.info("📅 **分析**: 颜色越深代表该月发布越密集，可直观看出品牌的市场节奏。")