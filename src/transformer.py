
def build_master_table(data):
    """

    Transform and join data 
    
    Args: 
        data: The dataset 

    Returns: 
        A cleaned joined data 

    """

    orders = data['orders']
    order_items = data['order_items']
    order_payments = data['order_payments']
    customers = data['customers']
    order_reviews = data['order_reviews']

    item_agg = order_items.groupby('order_id')[['price', 'freight_value']].sum().reset_index()
    payment_agg = order_payments.groupby('order_id')['payment_value'].sum().reset_index() 
    reviews_agg = order_reviews.groupby('order_id')['review_score'].mean().reset_index()

    master = orders.merge(item_agg, on='order_id', how='left')
    master = master.merge(payment_agg, on='order_id', how='left')
    master = master.merge(customers, on='customer_id', how='left')
    master = master.merge(reviews_agg, on='order_id', how='left')


    return master 