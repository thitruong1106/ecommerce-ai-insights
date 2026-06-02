from src.loader import load_all_data
from src.transformer import build_master_table
from src.analyser import revenue_by_category, freight_ratio_by_category, delivery_vs_reviews
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
print(delivery_vs_reviews(master_table))