#import webbrowser, time
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

api_url_base = 'https://api.chimu.moe/v1/download/'


PATH = 'C:/Users/Ifaz/Downloads/chromedriver_win32/chromedriver.exe'
browser = webdriver.Chrome(PATH)

with open('C:/Users/Ifaz/Downloads/maps.txt', 'r') as file:
    lines = file.readlines()

links = []

for line in lines:
    if (line[0:4] == 'http'):
        links.append(line.split(' ')[0])


for link in links:
    beatmapID = link.split('/')[-1]
    #webbrowser.open_new_tab("https://beatconnect.io/b/" + beatmapID)
    browser.get(api_url_base + beatmapID + "?n=1")
    #urllib.request.urlretrieve(api_url_base + beatmapID + "?n=1")
    #requests.get(api_url_base + beatmapID + '?n=1')
    time.sleep(1)
