import streamlit as st
# 这里的 import 语句非常关键，它从你的文件夹里加载逻辑
from utils import io, prep
from sections import intro, overview, deep_dives, conclusions

# 1. 配置页面
st.set_page_config(
    page_title="2025 Smartphone Market Pulse",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 加载与预处理数据
# 调用 utils/io.py 和 utils/prep.py
df_raw = io.load_data()
df_processed = prep.preprocess_data(df_raw)

# 3. 侧边栏与标题
# 【关键】这里调用了 sections/intro.py 里那个带 Logo 的函数
intro.show_sidebar_methodology() 

with st.sidebar:
    st.subheader("🔍 过滤器 (Filters)")
    
    all_brands = sorted(df_processed['brand'].unique())
    selected_brands = st.multiselect("选择品牌", all_brands, default=all_brands[:3])
    
    all_os = sorted(df_processed['os'].unique())
    selected_os = st.multiselect("操作系统", all_os, default=all_os)
    
    min_price = int(df_processed['price_usd'].min())
    max_price = int(df_processed['price_usd'].max())
    price_range = st.slider("价格范围 (USD)", min_price, max_price, (min_price, max_price))

# 4. 应用过滤逻辑 (在主文件里做筛选最方便)
if not selected_brands:
    df_filtered = df_processed.copy()
else:
    df_filtered = df_processed[df_processed['brand'].isin(selected_brands)]

if selected_os:
    df_filtered = df_filtered[df_filtered['os'].isin(selected_os)]

df_filtered = df_filtered[
    (df_filtered['price_usd'] >= price_range[0]) & 
    (df_filtered['price_usd'] <= price_range[1])
]

# 5. 渲染主页面各个部分
# 依次调用 sections/ 文件夹里的其他模块
intro.show_header()
overview.show_kpis(df_filtered)
deep_dives.show_charts(df_filtered, df_processed) # 传入 df_processed 用于获取月份排序
conclusions.show_quality_report(df_filtered)