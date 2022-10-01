import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(level=logging.info)


# Get the http response and parse the html
def get_soup(url: str) -> object:
    logging.info("Requesting the https response...")
    response: object = requests.get(url)
    # Parse the html in case of positive response
    try:
        if response.status_code == 200:
            soup: object = BeautifulSoup(response.text,"html.parser")
            return soup           
    # Exception handling needs to be improved (under development).
    except Exception as e:
        logging.info("Error during the parser: {} ".format(e))

# Get links to the games
def get_game_apps(soup: object, url: str) -> list:
    logging.info("Getting links...")
    links: list = []
    # Finding the hrefs in html tree
    games_links = soup.find_all("tr")
    # Skipping header
    games_links.pop(0)
    # Looping for the links
    for game in games_links:
        links.append(url+game.a["href"])

# Get games data
def get_game_tags_info(url: str):
    logging.info("Extracting data from the game...")
    response = requests.get(game_url)
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.text,"html.parser")
            
# -------------------------------->Extract the game info
            #print('HTTP 200 OK -- SUCCESSFUL REQUEST FOR GAME APP')
            try:
                game_soup = soup.find("div" ,attrs = {"class":"col-md-4 no-padding"}).find("p")
                return game_soup
            except:
                game_data_dict["dev"].append(None)
                game_data_dict["publisher"].append(None)
                game_data_dict["genre"].append(None)
                game_data_dict["language"].append(None)
                game_data_dict["tags"].append(None)
                game_data_dict["category"].append(None)
                game_data_dict["release"].append(None)
                game_data_dict["actual_price"].append(None)
                game_data_dict["discount"].append(None)
                game_data_dict["old_userscore"].append(None)
                game_data_dict["metascore"].append(None)
                game_data_dict["owners"].append(None)
                game_data_dict["followers"].append(None)
                return "FORMAT ERROR"
    except:
        print('error')
