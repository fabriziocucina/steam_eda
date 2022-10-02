import pandas as pd
import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(level=logging.INFO)
from tqdm import tqdm


# Get the http response and parse the html
def get_soup(url: str) -> object:

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
def get_games_links(soup: object, url: str) -> list:
    links: list = []
    # Finding the hrefs in html tree
    games_links = soup.find_all("tr")
    # Skipping header
    games_links.pop(0)
    # Looping for the links
    for game in games_links:
        links.append(url+game.a["href"])
    logging.info("Links Extracted...")
    return links

# Get games data
def get_game_info(links: list) -> object:
    logging.info("Extracting data from games...")
    game_list: list = links
    # Create lists for the info
    developers,genres,languages,tags,publishers,categories = [],[],[],[],[],[]
    release_dates,prices,old_userscores,metascores,owners,followers,title = [],[],[],[],[],[],[]
    # Temporal lists
    genres_temp, languages_temp,tags_temp = [],[],[]
    # Looping the list with the links
    for game in tqdm(game_list):
        # Requesting the https response
        soup: object = get_soup(game)
        game_soup = soup.find("div" ,attrs = {"class":"col-md-4 no-padding"}).find("p")

        for ahref in game_soup.find_all("a"): # for ahref
            try:
                if "/genre/" in str(ahref):
                    genres_temp.append(ahref.text)
            except:
                    genres_temp.append("N/A")
            try:
                if "language" in str(ahref):
                    languages_temp.append(ahref.text)
            except:
                    languages_temp.append("N/A")
            try:
                if "tag" in str(ahref):
                    tags_temp.append(ahref.text)
            except:
                    tags_temp.append("N/A")
        # Make union of the values, clean temporal list and append it to the main list
        genres_union = ",".join(genres_temp)
        genres_temp.clear()
        genres.append(genres_union)
        languages_union = ",".join(languages_temp)
        languages_temp.clear()
        languages.append(languages_union)
        tags_union = ",".join(tags_temp)
        tags_temp.clear()
        tags.append(tags_union)

        for strong in game_soup.find_all("strong"): # for strong
            try:
                if "Developer" in str(strong):
                    developers.append(strong.find_next_sibling("a").text)
            except:
                    developers.append("N/A")
            try:
                if "Publisher" in str(strong):
                    publishers.append(strong.nextSibling.nextSibling.text)
            except:
                    publishers.append("N/A")
            try:
                if "Category" in str(strong):
                    categories.append(strong.nextSibling)
            except:
                    categories.append("N/A")
            try:
                if "Release date" in str(strong):
                    release_dates.append(strong.nextSibling.replace(":","").replace("(previously","").strip())
            except:
                    release_dates.append("N/A")
            try:
                if "Price" in str(strong):
                    prices.append(strong.nextSibling.strip())
            except:
                    prices.append("N/A")
            try:
                if "Old userscore" in str(strong):
                    old_userscores.append(strong.nextSibling.strip())
            except:
                    old_userscores.append("N/A")
            try:
                if "Metascore" in str(strong):
                    metascores.append(strong.nextSibling.strip())
            except:
                    metascores.append("N/A")
            try:
                if "Owners" in str(strong):
                    owners.append(strong.nextSibling.replace(r": ","").strip().replace(u"\xa0..\xa0",u" - "))
            except:
                    owners.append("N/A")
            try:
                if "Followers" in str(strong):
                    followers.append(strong.nextSibling.replace(": ",""))
            except:
                    followers.append("N/A")
        # Get title       
        title.append(soup.find("div" ,attrs = {"class":"col-md-4 no-padding"}).find("h3").text)

    data = {
            "title": title,
            "developer": developers,
            "genre": genres,
            "language": languages,
            "tag": tags,
            "publisher": publishers,
            "category": categories,
            "release_date": release_dates,
            "price": prices,
            "old_userscore": old_userscores,
            "metascore": metascores,
            "owners": owners,
            "followers": followers
        }

    logging.info("Data extracted finalized...")
    return data

def get_df(df) -> pd.DataFrame:
    logging.info("Creating the Dataframe...")
    df = pd.DataFrame(df)
    return df


