import pandas as pd
import numpy as np 
import re



def clean_column_names(df):
    new_columns = []
    changes = ["\[", "\]", "\'", "%", "\$", "/app/",",","-","."]
    for change in changes: 
        for column in df.columns:
            new_column = column.replace(change,"").replace(" ","_")
            new_columns.append(new_column.capitalize())
    df_new = df
    df_new.columns = new_columns
    return df_new

def clean_rows(df):
    changes = ["\[", "\]", "\'", "%", "\$", "/app/",",","-","."]
    for change in changes:
        for 
