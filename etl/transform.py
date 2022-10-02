from distutils.command.config import config
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
        new_columns.append(new_column.capitalize().strip())
    df.columns = new_columns
    return df

# Clean the rows
def clean_rows(df):
    logging.info("Normalizing rows...")
    changes_in_rows = ["\[", "\]", "\'", "%", "\$", "/app/"]
    for change in changes_in_rows:
        df.replace(change, "", regex = True, inplace = True)
        df.reset_index(drop = True, inplace = True)
    return df

# Trim all values in the rows
def trim_all_columns(df):
    logging.info("Triming values...")
    trim_strings = lambda x: x.strip() if isinstance(x, str) else x
    df.applymap(trim_strings)
    return df

# Get results in a excel file
def save_data(df,path: str):
    logging.info("Saving results in the folder...")
    df.to_excel(path["path_extract"]+"\\"+"steam_games_"+str(path["year"])+".xlsx")

