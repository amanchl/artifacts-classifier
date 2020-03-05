from gazpacho import get, Soup
from selenium import webdriver
import re
import urllib
import time
import pandas as pd

browser = webdriver.Firefox()
browser.get("https://www.pinterest.ca/catherine8610/greek-pottery/")
for i in range(1,5000):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

soup = Soup(browser.page_source)

greek_images = re.findall(r'https:\/\/[^"]+?\.jpg', str(soup))

greek_df = pd.DataFrame(greek_images)
greek_urls = greek_df[0].unique().tolist()

for url in greek_urls[1::2]:
    try:
        urllib.request.urlretrieve(url, f"/Users/username/Greece/greek{greek_urls.index(url)}.jpg")
    except:
        pass


browser = webdriver.Firefox()
browser.get("https://www.pinterest.ca/armidaptaylor/italian-renaissance-ceramicsceramiche-rinascimenta/")
for i in range(1,2500):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

soup = Soup(browser.page_source)

ren_images = re.findall(r'https:\/\/[^"]+?\.jpg', str(soup))

ren_df = pd.DataFrame(ren_images)
ren_urls = ren_df[0].unique().tolist()

for url in ren_urls[1::2]:
    try:
        urllib.request.urlretrieve(url, f"/Users/username/Renaissance/ren{ren_urls.index(url)}.jpg")
    except:
        pass


browser = webdriver.Firefox()
browser.get("https://www.pinterest.ca/leequimby/prehistoric-artifacts/")
for i in range(1,2500):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

soup = Soup(browser.page_source)

ph_images = re.findall(r'https:\/\/[^"]+?\.jpg', str(soup))

ph_df = pd.DataFrame(ph_images)
ph_urls = ph_df[0].unique().tolist()

for url in ph_urls[1::2]:
    try:
        urllib.request.urlretrieve(url, f"/Users/username/Prehistory/ph{ph_urls.index(url)}.jpg")
    except:
        pass
