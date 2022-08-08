import pandas as pd

def first_model():
    melbourne_file_path = './data/melb_data.csv'
    melb_data = pd.read_csv(melbourne_file_path)
    melb_data.columns
    melb_data = melb_data.dropna(axis=0)
    y = melb_data.Price
    melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
    X = melb_data[melbourne_features]
    #print(X.describe())
    #print(X.head())



