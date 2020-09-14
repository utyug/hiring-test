# coding: utf-8

import pandas as pd

if __name__ == '__main__':
    
    test = pd.read_csv('/hiring-test-data/test.csv')    
    
    target_prediction = pd.DataFrame()
    target_prediction['index'] = range(test.shape[0])
    target_prediction['prediction'] = 0

    target_prediction.to_csv('/hiring-test-data/prediction.csv', index=False)
