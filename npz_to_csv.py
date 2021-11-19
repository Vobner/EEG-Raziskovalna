import numpy as np
import pickle


for i in range(1,17):
    with open("csvData/participant{}".format(i) + ".csv", "a") as f:
        data_npz = np.load("Data/EEG_DE_features/{}_123.npz".format(i))
        data = pickle.loads(data_npz['data'])
        labels = pickle.loads(data_npz['label'])
        for key, value in data.items():
            # first creating a vector (value) wich cointains all features data
            # then creating a another vector(arr) wich cointains the labels
            arr = np.array(labels[key])
            # reshaping arr into a vertical vector
            arr_reshaped = np.reshape(arr,(len(arr),1))
            # merging the two vectors together
            solution = np.concatenate((value,arr_reshaped), axis=1)
            np.savetxt(f, solution)