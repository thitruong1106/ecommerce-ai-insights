
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

def build_product_table(data): 
    """
    
    Args: 
        data: the dataset 

    Returns: 
        Product table, one row per order item. Not one row per order 

    """
    order_items = data['order_items']
    order_reviews = data['order_reviews']
    products = data['products']
    product_cat = data['product_category']

    # Aggregate reviews first so each order_id appears once 
    review_agg =(order_reviews.groupby('order_id')['review_score'].mean().reset_index())

    # Build product-level table 
    master = order_items.merge(products, on='product_id', how='left')

    master = master.merge(product_cat, on='product_category_name', how='left')

    #join only order_id + aggregated review_score 
    master = master.merge(review_agg, on='order_id', how='left')

    master = master[['order_id', 'product_id', 'product_category_name_english', 'price', 'freight_value', 'review_score']]
    return master 
