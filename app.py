import streamlit as st 
import os 
from src.loader import load_all_data 
from src.transformer import build_master_table, build_product_table 
from src.visualiser import plot_revenue_by_category, plot_freight_ratio, plot_delivery_vs_review, plot_low_reviews_cat
import matplotlib.pyplot as plt 
import matplotlib
from src.ai_insights import generate_insights, format_analysis_for_ai
from src.analyser import revenue_by_category, freight_ratio_by_category, delivery_vs_reviews, low_review_categories
matplotlib.use('Agg')

data = load_all_data() 
master_table = build_master_table(data)
product_table = build_product_table(data)

total_revenue = product_table['price'].sum() 
total_order = master_table['order_id'].count() 
avg_review = product_table['review_score'].mean() 
col1, col2, col3 = st.columns(3)

col1.metric(label="Total Revenue", value=f"${total_revenue:,.0f}")
col2.metric(label="Total Order", value =f"{total_order:,}")
col3.metric(label="Average Review", value = f"{avg_review:.1f}")

st.header("Revenue by Category")
fig_cat = plot_revenue_by_category(product_table)
st.pyplot(fig_cat)
plt.close(fig_cat)
st.divider() 

st.header("Freight Ratio by Category")
fig_ratio = plot_freight_ratio(product_table)
st.pyplot(fig_ratio)
plt.close(fig_ratio)
st.divider() 

st.header("Delivery vs Review")
fig_delivery = plot_delivery_vs_review(master_table)
st.pyplot(fig_delivery)
plt.close(fig_delivery)

st.divider() 

st.header("Low review categories")
low_review_fig = plot_low_reviews_cat(product_table)
st.pyplot(low_review_fig)
plt.close(low_review_fig)

st.divider() 

#if button 


if st.button(label="Generate insight"):
    
    revenue = revenue_by_category(product_table)
    freight = freight_ratio_by_category(product_table)
    delivery = delivery_vs_reviews(master_table)
    low_reviews = low_review_categories(product_table)

    analysis_summary = format_analysis_for_ai(
        revenue,
        freight,
        delivery,
        low_reviews
    )
    insight = generate_insights(analysis_summary)
    st.subheader("AI business insights")
    st.write(insight)
