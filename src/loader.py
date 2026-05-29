#Take a file path as an agruement import pandas as pd def load_csv(file_path): """ Load a csv file into a pandas DataFrame. Args: file_path (str): The path to the csv file. Returns: pandas.DataFrame: The loaded dataset. """ #load the csv using panda try: df = pd.read_csv(file_path) print(df.head(5)) return df except FileNotFoundError: print(f"Error: The file {file_path} does not exists.") return None#Take a file path as an agruement 
import pandas as pd 
from pathlib import Path
def load_csv(file_path): 
    """
    Load a csv file into a pandas DataFrame. 

    Args: 
        file_path (str): The path to the csv file. 

    Returns: 
        pandas.DataFrame: The loaded dataset. 
    """
    #load the csv using panda 
    try: 
        df = pd.read_csv(file_path)
        print(f"Shape: {df.shape}")
        return df
    except FileNotFoundError: 
        print(f"Error: The file {file_path} does not exists.")
        return None 


def load_all_data():
    """
    Load all ecommerce CSV files and reutrn them in one dictionary 

    """
    #base path 
    base_path = Path("data/Brazilian E-Commerce Public Dataset by Olist")

    # Multiple tables to return 
    datasets = {
        "customers": "olist_customers_dataset.csv",
        "geolocation": "olist_geolocation_dataset.csv",
        "order_items": "olist_order_items_dataset.csv",
        "order_payments": "olist_order_payments_dataset.csv",
        "order_reviews": "olist_order_reviews_dataset.csv",
        "orders": "olist_orders_dataset.csv",
        "products": "olist_products_dataset.csv",
        "sellers": "olist_sellers_dataset.csv",
        "product_category": "product_category_name_translation.csv",
    }

    #To store our df 
    data = {} 

    for name, filename in datasets.items(): 
        file_path = base_path / filename 
        data[name] = load_csv(file_path)
    
    return data 