#!/usr/bin/env python
# coding: utf-8

# In[3]:


conda install -c anaconda beautifulsoup4


# In[ ]:


import requests
from bs4 import BeautifulSoup
import argparse
import pandas
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter the number of pages to parse", type=int)
parser.add_argument("--dbname", help="Enter the number of pages to parse", type=int)
args = parser.parse_args()

oyo_url="https://www.oyorooms.com/hotels-in-bangalore/?page="
headers={"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
page_num_MAX = args.page_num_max
scraped_info_list = []
connect.connect(args.dbname)

for page_num in range(1, page_num_MAX):
    req = requests.get(oyo_url + str(page_num),headers=headers)
    content = req.content
    
    soup = BeautifulSoup(content, "html.parser")
    
    all_hotels = soup.find_all("div", {"class": "hotelCardListing"})
    
    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3", {"class": "listingHotelDescription_hotelName"}).text
        hotel_dict["address"] = hotel.find("span", {"itemprop": "streetAddress"}).text
        hotel_dict["price"] = hotel.find("span", {"class": "listingPrice_finalPrice"}).text
        # try ....except
        try:
            hotel_dict["rating"] = hotel.find("span", {"class": "hotelRating_ratingSummary"}).text
        except AttributeError:
            pass
        
        parent_amenities_element = hotel.find("div", {"class": "amenityWrapper"})
        
        amenities_list = []
        for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper_amenity"}):
            amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())
        hotel_dict["amenities"] = ', '.join(amenities_list[:-1])
        
        scraped_info_list.append(hotel_dict)
        connect.insert_into_table(args.dbname,tuple(hotel_dict.values())
                                  
        # print(hotel_name, hotel_address, hotel_price, hotel_rating, amenities_list)

dataFrame = pandas.DataFrame(scraped_info_list)
dataFrame.to_csv("Oyo.csv")
connect.get_hotel_info(args.dbname)

