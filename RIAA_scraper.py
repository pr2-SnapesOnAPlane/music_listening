from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe', 'user_agent': 'Custom User Agent'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    #list url to visit
    riaa_url = 'https://www.riaa.com/gold-platinum/?tab_active=awards_by_album#search_section'

    #visit url
    browser.visit(riaa_url)

    time.sleep(15)

    riaa_html = browser.html 
    soup = BeautifulSoup(riaa_html, 'html.parser')

    # #click 100 times to load more results
    # for x in range(1, 100):
    #     browser.click_link_by_id('loadmore')

    #find table
    table = soup.find_all('table')[0]

    #read into pandas
    no_details = pd.read_html(str(table), header=0)

    #select the first table
    no_details_cleanup = no_details[0]

    #drop first column
    no_details_cleanup.drop(no_details_cleanup.columns[0], axis=1, inplace=True)

    #drop last column
    no_details_cleanup.drop(no_details_cleanup.columns[5], axis=1, inplace=True)

    ##clean certified units columns to have only number
    # grab certified units column and split
    c_units = no_details_cleanup['Certified Units (In Millions)'].str.split(" ", n = 1, expand = True)

    # grab first column of df
    cu = c_units[c_units.columns[0]]

    # add to cleanup df
    no_details_cleanup['Certified Units (Millions)'] = cu

    # drop original certified units column
    no_details_cleanup.drop(no_details_cleanup.columns[4], axis=1, inplace=True)




scrape()