import os
import glob
import pandas as pd

def features_train(fp):
    while True:
        if not os.path.exists(fp):
            files = glob.glob('data/f*.csv')
            features, features_test = [pd.read_csv(file, index_col='match_id') for file in files]
            features_train = pd.concat([features.loc[:, features_test.columns], features['radiant_win']], axis=1, sort=False).to_csv(fp)
        else:
            features_train = pd.read_csv(fp, index_col='match_id')
            return features_train
