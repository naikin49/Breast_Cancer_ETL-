import pandas as pd

def load_data(path="data.csv"):
    df = pd.read_csv(path)
    return df
