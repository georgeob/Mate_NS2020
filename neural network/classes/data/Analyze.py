import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import requests
import io


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
        return counted_column.plot.bar()

    def plot_dataset(self, data_frame):
        sns.pairplot(data_frame)

    def get_data_set_informations(self, data_frame):
        print('Dataset obsahuje {} stlpcov \n'.format(data_frame.shape[1]))
        print('Dataset obsahuje {} riadkov \n'.format(data_frame.shape[0]))
        print('Dataset obsahuje nasledujuce stlpce: ')
        [print('{}, '.format(w)) for w in data_frame.columns]
        print('\n')
        print(data_frame.info())
        print('\n')
