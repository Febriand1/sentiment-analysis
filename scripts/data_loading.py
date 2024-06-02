import pandas as pd

path1 = 'dataset/'

def load_dataframe(file_name):
    df = pd.read_csv(path1 + file_name)
    return df
