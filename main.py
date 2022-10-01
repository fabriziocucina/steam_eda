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


def main():
    # Configuration variables
    logging.info("Starting the scraper...")
    conf = configuration()
    main_url = scraping.get_soup(conf["sites"]["steam_spy_year"]+str(conf["year"]))
    links = scraping.get_games_links(main_url,conf["sites"]["steam_spy_main"])
    game_info = scraping.get_game_info(links)
    scraping.get_excel(game_info,conf["year"])


if __name__ == "__main__":
    main()