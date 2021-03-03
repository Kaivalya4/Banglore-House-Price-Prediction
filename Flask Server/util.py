import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_price(locations , sqft , bhk , bath):
    try:
        loc_index = __data_columns.index(locations.lower())
    except:
        loc_index = -1
    
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    if loc_index >=0:
        x[loc_index] = 1
    
    global __model
    return __model.predict([x])

def get_location_names():
    return __locations

def load_artifact():
    print("Loading Artifact!!!!")
    global __locations
    global __data_columns

    with open("D:/pdata/Banglore_house_price/Baglore House Price/server/artifact/columns.json","r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[9:]

    global __model
    if __model is None:
        with open('D:/pdata/Banglore_house_price/Baglore House Price/server/artifact/Banglore_home_Price_Prediction.pickle','rb') as f:
            __model = pickle.load(f)
    print("Artifact Loaded")    


if __name__ == "__main__":
    load_artifact()
    print(get_location_names())
    print(get_price("1st phase jp nagar" , 1000 , 3 , 3))