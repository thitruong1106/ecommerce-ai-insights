from src.loader import load_all_data
from src.transformer import build_master_table

data = load_all_data()

customers = data["customers"]
geolocation = data["geolocation"]
order_items = data["order_items"]
order_payments = data["order_payments"]
order_reviews = data["order_reviews"]
orders = data["orders"]
products = data["products"]
sellers = data["sellers"]
product_category = data["product_category"]

master = build_master_table(data)

print(master.head())
print(master.shape)

print(master.columns.tolist())
