# Importing standard python libraies
import time
import sys
import logging
logging.basicConfig(level=logging.INFO)
# Importing third-party libraries
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# Import internal libraries
from etl import scraping
from configuration import configuration
from etl import transform


def main():
    logging.info("Starting the scraper...")
    conf = configuration()
    main_url = scraping.get_soup(conf["sites"]["steam_spy_year"]+str(conf["year"]))
    links = scraping.get_games_links(main_url,conf["sites"]["steam_spy_main"])
    time.sleep(4)
    game_info = scraping.get_game_info(links)
    time.sleep(4)
    data = scraping.get_df(game_info)
    time.sleep(4)
    columns = transform.clean_column_names(data)
    time.sleep(4)
    rows = transform.clean_rows(columns)
    time.sleep(4)
    spaces = transform.trim_all_columns(rows)
    time.sleep(4)
    transform.save_data(spaces,conf)


if __name__ == "__main__":
    main()