import pandas as pd
import numpy as np
import os

def load_file(file_name):
    """function checks the file extension and
    load it accordingly"""

    file_extension = os.path.splittext(file_name)

    if file_extension=='.csv':
        dataframe = pd.read_csv(file_name)

    else:
        raise Exception('File type {}, expected CSV'.format(file_extension))

    return dataframe




