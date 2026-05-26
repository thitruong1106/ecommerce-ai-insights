#Take a file path as an agruement import pandas as pd def load_csv(file_path): """ Load a csv file into a pandas DataFrame. Args: file_path (str): The path to the csv file. Returns: pandas.DataFrame: The loaded dataset. """ #load the csv using panda try: df = pd.read_csv(file_path) print(df.head(5)) return df except FileNotFoundError: print(f"Error: The file {file_path} does not exists.") return None#Take a file path as an agruement 
import pandas as pd 
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
        print(df.head(5))
        return df
    except FileNotFoundError: 
        print(f"Error: The file {file_path} does not exists.")
        return None 

