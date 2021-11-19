import numpy as np
import pickle

with open("D:\EEG Raziskovalna\Data\EEG_DE_features_csv\Participants_test.csv", "a") as f:
    data_npz = np.load("Data/EEG_DE_features/{}_123.npz".format(16))
    data = pickle.loads(data_npz['data'])
    labels = pickle.loads(data_npz['label'])
    for key, value in data.items():

        arr = np.array(labels[key])
        arr_reshaped = np.reshape(arr,(len(arr),1))
 
        solution = np.concatenate((value,arr_reshaped), axis=1)
        np.savetxt(f, solution)

        

