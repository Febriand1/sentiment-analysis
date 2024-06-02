import pickle

path2 = 'model/'

def load_model(file_name):
    with open(path2 + file_name, 'rb') as file:
        model = pickle.load(file)
    return model
