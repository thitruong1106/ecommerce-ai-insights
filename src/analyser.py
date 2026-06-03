import pandas as pd 

"""
    Take the master table as parameter 
    Ask one specific business question 
    retuen results 
"""

def revenue_by_category(product_table): 
    total_revenue = product_table.groupby('product_category_name_english')['price'].sum().sort_values(ascending=False)
    return total_revenue

def freight_ratio_by_category(product_table): 
    freight_summary  = product_table.groupby('product_category_name_english').agg(
        total_revenue = ('price', 'sum'),
        total_freight = ('freight_value', 'sum') 
    )

    freight_summary['percentage'] = freight_summary['total_freight'] / freight_summary['total_revenue']
    freight_summary = freight_summary.sort_values('percentage', ascending=False)


    return freight_summary 

def delivery_vs_reviews(master_table): 
    #Does slow delivery lead to bad reveiews 
    df = master_table.copy()

    #calculate delivery delay 
    df['delay'] = (
        pd.to_datetime(df['order_delivered_customer_date'])
        - pd.to_datetime(df['order_estimated_delivery_date'])
        ).dt.days

    late_order = df[df['delay'] > 0]
    early_order_or_on_time = df[df['delay'] <= 0]

    #average review score for late orders and early/on time orders 
    late_avg_review = late_order['review_score'].mean()
    early_order_or_on_time_avg_review = early_order_or_on_time['review_score'].mean() 

    #late count / early count 
    late_count = late_order['review_score'].count() 
    on_time_or_early_count = early_order_or_on_time['review_score'].count() 

    summary = {
        "late_orders": {
            "avg_review_score": late_avg_review,
            "order_count": late_count
        }, 
        "early_or_ontime_orders": {
            "avg_review_early_or_on_time": early_order_or_on_time_avg_review,
            "order_count": on_time_or_early_count
        }, 
        "difference": early_order_or_on_time_avg_review - late_avg_review
    }

    return summary

#Product cat that have the worst customer sat

def low_review_categories(product_table):
    #return summary per category showing 
    # total revenue, 
    # average review score, 
    # count of items sold 

    df = product_table.copy()
    summary = df.groupby('product_category_name_english').agg(
        total_revenue = ('price','sum'),
        avg_review_score = ('review_score', 'mean'),
        count_of_sold_items = ('order_id', 'count')
    ).sort_values('avg_review_score', ascending = True).reset_index() 
    summary = summary[summary['count_of_sold_items'] > 100]
    return summary 
    