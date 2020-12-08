import sklearn.impute as Imputer
import numpy as np
from utils import *

class LeafImputer(object):

    def __init__(self, missing_val=np.nan, constant=None):
        self.missing_val = missing_val
        self.constant = constant

    def mean_imputer(self):
        imputer = Imputer.SimpleImputer(missing_values=self.missing_val,
                                        strategy='mean')
        return imputer

    def media_imputer(self):
        imputer = Imputer.SimpleImputer(missing_values=self.missing_val,
                                        strategy='median')
        return imputer

    def mostfrequent_imputer(self):
        imputer = Imputer.SimpleImputer(missing_values=self.missing_val,
                                        strategy='most_frequent')
        return imputer

    def constant_imputer(self):

        if self.missing_val is None:
            raise Exception("Give 'constant' some value while initializing LeafImputer\
                            when using constant_imputer")

        imputer = Imputer.SimpleImputer(missing_values=self.missing_val,
                                        strategy='constant',
                                        fill_value=self.missing_val)
        return imputer

if __name__ == "__main__":

    dataset_path = "./exmaple_datasets/iris.csv"
    data = load_file(dataset_path)

    imputer = LeafImputer()


