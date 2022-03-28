import requests
from bs4 import BeautifulSoup
import re
import pymongo


def getPrices(hun):
    names = hun.findAll("td", {"class":"nafn"})
    datesCaught = hun.findAll("td", {"class":"dags"})
    links = []
    prices = hun.findAll("td", {"class":"verd"})
    lis = []
    # Loop through every item in the name list
    for i in range(len(names)):
        # Name is fine straight from mbl
        name = names[i].text.strip()
        # Date needs to be today, as we'd run this every day
        date = datesCaught[i].text.strip()
        print("Date ", date)
        # Price
        price = prices[i].text.strip()
        # Slice the last 6 character off to get rid of kr/kg and the whitespace infront
        price = price[:6] 
        data = {
        "name" :name,
        "date" : date,
        "price" : price
    }   
        lis.append(data)
    return lis

def add_to_mongoDB(data):
    # Example data
    # data = {
    #     "name" :"karfi",
    #     "date" : "21.02.22",
    #     "price" : "327,28"
    # }
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # Database Name
    db = client["dailycatches"]
    
    # Collection Name
    col = db["seafood"]
    for x in data:
        col.insert_one(x)
    cursor = col.find()
    print("Cursor ", cursor)

def get_fish_prices(fish_link):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    f = requests.get(fish_link,headers=headers).text
    hun = BeautifulSoup(f,'html.parser')
    value = getPrices(hun)
    return value

# Gets the name, date, and price per kilo of catches in Iceland
def main():
    SITEURL = "https://www.mbl.is/200milur/afurdir/" 
    catchInfo = get_fish_prices(SITEURL)
    add_to_mongoDB(catchInfo)
main()