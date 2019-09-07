from sklearn.preprocessing import LabelEncoder
from utils import make_folder

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
    df = pd.read_csv("/home/greatskull/00personal_projects/da_vinci/example_datasets/iris.csv")
    df = label_encode(df, 1)