import pandas as pd
import os

def load_file(file_name):
    """function checks the file extension and
    load it accordingly"""

    file_extension = os.path.splittext(file_name)

    if file_extension=='.csv':
        dataframe = pd.read_csv(file_name)
        # target =

    else:
        raise Exception('File type {}, expected CSV'.format(file_extension))

    return dataframe

def make_folder(name):
    try:
        os.mkdir(name)
    except:
        pass

def load_file_db():

    """loading data from database"""

    return 0




