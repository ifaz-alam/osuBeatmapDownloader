import time
import requests
from selenium import webdriver

PATH = 'C:/Users/Ifaz/Downloads/chromedriver_win32/chromedriver.exe'
browser = webdriver.Chrome(PATH)

with open('C:/Users/Ifaz/Downloads/maps.txt', 'r') as file:
    lines = file.readlines()

# list that is to store the osu.ppy.sh beatmap urls
links = []

# extract the osu.ppy.sh urls
for line in lines:
    if (line[0:4] == 'http'):
        links.append(line.split(' ')[0])

count = 0

for link in links:
    beatmapID = link.split('/')[-1]
    # download the beatmap corresponding to the beatmap ID
    # by default n = 1 corresponds to no video associated to the .osz file
    # set n = 0 if you would like to download .osz with video
    response = requests.get('https://api.chimu.moe/v1/download/' + beatmapID + '?n=1')
    if (response.status_code == 404):
        # beatmap has not been found on Chimu.moe beatmap host, try alternative host
        print('This beatmap is not available on Chimu.moe! Attempting to retrieve from Sayobot osu! beatmap mirror.')
        browser.get('https://usa1.sayobot.cn/beatmaps/135/0684/novideo?filename=' + beatmapID)
    else:
        browser.get('https://api.chimu.moe/v1/download/' + beatmapID + '?n=1')
    count += 1
    print('%d/%d beatmap listings processed' % (count, len(lines)))
    # delay in seconds
    time.sleep(1.5)

print('Finished downloading beatmaps.')
