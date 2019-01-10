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

    time.sleep(5)

    riaa_html = browser.html 
    soup = BeautifulSoup(riaa_html, 'html.parser')

    # #click 10 times to load more results
    # for x in range(1, 10):
    #     browser.click_link_by_id('loadmore')

    table = soup.find_all('table')[0]

    print(table)

    no_details = pd.read_html(str(table), header=0)

    

scrape()