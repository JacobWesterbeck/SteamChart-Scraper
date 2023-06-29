from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os

url = "https://steamcharts.com/top"

#setup chromedriver
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver,10)

#get the page and tell me if it is process successful
driver.get(url)
try:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "content")))
    print("Got your data!")
except:
    print('Element not found')



#set up list to capture data and map desired elements to variables
table = driver.find_element(By.TAG_NAME, 'tbody')
rows = table.find_elements(By.TAG_NAME, "tr")

dataset = []

#create a list to store values and identify them by keys
for row in rows:
    games = {} 
    cells = row.find_elements(By.TAG_NAME, "td")
    games['rank'] = cells[0].text
    games['name'] = cells[1].text
    games['current_players'] = cells[2].text
    games['peak'] = cells[4].text
    games['hours_played'] = cells[5].text

    dataset.append(games)

#put the data into a pandas dataframe
df = pd.DataFrame(dataset)


#get current date in proper format for database(I'll be using PostgreSQL)
now = datetime.now()
date = now.strftime("%Y%m%d")

#path to save the csv file
path = r'~/Workspace/steam_scrape/data'
filename = "steam_data_" + date

#export the dataframe to a csvfile 
df.to_csv(os.path.join(path, filename + '.csv'), index=False, encoding='utf-8')
print('Data sent to ' + path)