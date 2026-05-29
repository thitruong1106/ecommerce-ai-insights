from src.loader import load_all_data
from src.transformer import build_master_table

data = load_all_data()
master = build_master_table(data)

print(master.shape)
print(master.columns.tolist())