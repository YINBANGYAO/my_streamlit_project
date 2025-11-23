import altair as alt
import streamlit as st

def create_scatter(df, x_metric):
    """创建价格 vs 硬件的散点图"""
    base = alt.Chart(df).encode(
        x=alt.X(x_metric, title=x_metric.replace('_', ' ').upper(), scale=alt.Scale(zero=False)),
        y=alt.Y('price_usd', title='Price (USD)'),
        tooltip=['brand', 'model', 'price_usd', 'processor', x_metric]
    )

    points = base.mark_circle(size=100, opacity=0.5).encode(
        color=alt.Color('brand', legend=alt.Legend(title="Brand"))
    )

    line = base.transform_regression(
        x_metric, 'price_usd'
    ).mark_line(color='red', size=4, strokeDash=[5,5]).encode(
        color=alt.value('red')
    )

    return (points + line).interactive().properties(
        height=450,
        title=f"Price vs. {x_metric.replace('_', ' ').title()} (with Trend Line)"
    )

def create_small_multiples(df):
    """创建分面直方图"""
    return alt.Chart(df).mark_bar().encode(
        x=alt.X("price_usd", bin=alt.Bin(step=100), title="Price Range ($100 bins)"),
        y=alt.Y("count()", title="Number of Models"),
        color=alt.Color("os", legend=None)
    ).properties(
        width=200,
        height=300
    ).facet(
        column=alt.Column("os", title="Operating System", header=alt.Header(titleFontSize=18, labelFontSize=14)),
        spacing=20
    ).resolve_scale(
        y='independent'
    ).interactive()

def create_heatmap(df, month_order):
    """创建发布热力图"""
    heatmap = alt.Chart(df).mark_rect().encode(
        x=alt.X('release_month', title='Month', sort=month_order),
        y=alt.Y('brand', title='Brand'),
        color=alt.Color('count()', title='Release Count', scale=alt.Scale(scheme='blues')),
        tooltip=['brand', 'release_month', 'count()']
    ).properties(
        height=400,
        title="2025 Brand Release Intensity"
    ).interactive()
    
    text = heatmap.mark_text(baseline='middle').encode(
        text='count()',
        color=alt.value('black')
    )
    
    return heatmap + text