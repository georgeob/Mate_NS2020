import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import requests
import io

from IPython import get_ipython


class Analyze:

    def get_data_frame_from_file(self, dataset):
        return pd.read_csv(dataset, index_col=None)

    def get_data_frame_from_url(self, url):
        response = requests.get(url).content
        return pd.read_csv(io.StringIO(response.decode('utf-8')))

    def get_first_x_number_of_rows(self, value, data_frame):
        return data_frame.head(value)

    def get_data_description(self, data_frame):
        return data_frame.describe()

    def plot_by_count(self, counted_column):
        #get_ipython().magic('matplotlib inline')
        return counted_column.plot.bar()

    def plot_dataset(self, data_frame):
        #get_ipython().magic('matplotlib inline')
        sns.pairplot(data_frame)

    def transform_non_numerical_data(self, data_frame):
        return pd.concat([data_frame, pd.get_dummies(data_frame.sex), pd.get_dummies(data_frame.smoker), pd.get_dummies(data_frame.region)], axis=1)

    def get_data_set_informations(self, data_frame):
        print('Dataset obsahuje {} stlpcov \n'.format(data_frame.shape[1]))
        print('Dataset obsahuje {} riadkov \n'.format(data_frame.shape[0]))
        print('Dataset obsahuje nasledujuce stlpce: ')
        [print('{}, '.format(w)) for w in data_frame.columns]
        print('\n')
        print(data_frame.info())
        print('\n')
