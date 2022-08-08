import pandas as pd
from sklearn.tree import DecisionTreeRegressor

class FirstMlModel():
    def __init__(self):
        self.melbourne_file_path = './data/melb_data.csv'
        self.melb_data = pd.read_csv(self.melbourne_file_path)
        self.melb_data.columns
        self.melb_data = self.melb_data.dropna(axis=0)
        self.y = self.melb_data.Price
        self.melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
        self.X = self.melb_data[self.melbourne_features]
        # print(self.X.describe())
        # print(self.X.head())

    def Process(self):
        # Define model. Specify a number for random_state to ensure same results each run
        self.melbourne_model = DecisionTreeRegressor(random_state=1)

        #Fit model
        self.melbourne_model.fit(self.X, self.y)

        print("Making predictions for the following 5 houses: ")
        print(self.X.head())
        print("The predictions are: ")
        print(self.melbourne_model.predict(self.X.head()))
