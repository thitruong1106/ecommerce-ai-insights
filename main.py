from src.loader import load_all_data
from src.transformer import build_master_table

data = load_all_data()
master = build_master_table(data)

from src.transformer import build_product_table

product_table = build_product_table(data)
print(product_table.shape)
print(product_table.columns.tolist())