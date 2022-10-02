import logging
import pandas as pd
import numpy as np 
import re


# Clean the columns
def clean_column_names(df):
    logging.info("Normalizing column names...")
    new_columns = []
    changes = ["\[", "\]", "\'", "%", "\$", "/app/",",","-","."]
    for column in df.columns: 
        for change in changes:
                new_column = column.replace(change,"").replace(" ","_")
        new_columns.append(new_column.capitalize())
    df.columns = new_columns
    return df

# Clean the rows
def clean_rows(df):
    logging.info("Normalizing rows...")
    changes = ["\[", "\]", "\'", "%", "\$", "/app/",",","-","."]
    for change in changes:
        df= df.replace(change, "", regex = True)
    df = df.reset_index(drop = True, inplace = True)
    return df

