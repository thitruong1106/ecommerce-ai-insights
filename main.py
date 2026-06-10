from src.loader import load_all_data
from src.transformer import build_master_table
from src.analyser import revenue_by_category, freight_ratio_by_category, delivery_vs_reviews, low_review_categories
from src.visualiser import plot_revenue_by_category, plot_freight_ratio, plot_delivery_vs_review, plot_low_reviews_cat
data = load_all_data()
master = build_master_table(data)

from src.transformer import build_product_table
master_table = build_master_table(data)
product_table = build_product_table(data)
print(product_table.shape)
print(product_table.columns.tolist())
print(revenue_by_category(product_table))

"""
The highest revenue categories like home comfort, and flowers are losing over 40% of revenue to shipping cost. While Highest revenue category like 
watches and computers are the most shipping efficent. Consider whether home comfrot and flowers are worth keeping in inventory. 
"""
print(freight_ratio_by_category(product_table))

"""
Average review score on late orders - 2.272 
Average review score on early orders - 4.290

When orders arrive late, customer satisfaction drops nearly 50%. Late delivery average 2.3 stars, 
compared to 4.3 for orders that were on time. While 7% of orders didnt meet estimated delivery time, those orders 
are driving negative word of mouth, and could potentialy lose new customers. 
"""
print(delivery_vs_reviews(master_table))

"""
Of the categories with meaningful sales volume, office furniture has the worst satisfaction score. 
Generating 274k in revenue with consistently poor review. 

Business recommendation - The highest risk categories arent the ones making the least money, 
they are making the most with worst satisfaction. Bed bath and table generated over 1 million in total revenue, 
but has below average reviews sitting at 3.9, with 11115 items sold. If customer satisfaction drops further, that revenue disappears. 

"""
print(low_review_categories(product_table).head(10))

plot_revenue_by_category(product_table)
plot_freight_ratio(product_table)
plot_delivery_vs_review(master_table)
plot_low_reviews_cat(product_table)