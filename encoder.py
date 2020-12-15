from sklearn.preprocessing import LabelEncoder
from utils import make_folder
import numpy as np


class Encoder(object):

    def one_hot_encode(df, col_name):
        
        column_list = df.columns
        if col_name not in column_list:
            raise Exception('Column not in dataframe')
        df_module= df.copy()
        column_uniqueValue_list = df_module[col_name].unique()
        for i in range(len(column_uniqueValue_list)):
            df_module[col_name +" "+column_uniqueValue_list[i]] = np.where(df_module[col_name]==column_uniqueValue_list[i], 1,0)
        df_module = df_module.drop(col_name,axis=1)
        return df_module


    def label_encode(df, object_id):
        make_folder("objects")
        coloms = list(df.columns)
        for colom in coloms:
            if df[colom].dtype.__str__()=='str' or df[colom].dtype.__str__()=='bool':
                l = LabelEncoder()
                l.fit(df[colom])
                np.save(os.path.join('objects',(str(object_id)+str(colom)))+'.npy', l.classes_)
                df[colom] = l.transform(df[colom])
        return df

if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv("example_datasets/iris.csv")

    df = Encoder.one_hot_encode(df, 'specie')
    print(df.head)