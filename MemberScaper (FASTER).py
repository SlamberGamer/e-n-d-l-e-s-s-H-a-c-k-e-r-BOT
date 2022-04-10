import csv
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui, sys
import time
from csv import writer
from itertools import zip_longest

with open('EndlessHacker Player List.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)

    fsa = []

    for row in reader:
     # print(row[0])
     fsa.append(row[0])

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(10)
driver.get(fsa[1])
print(driver.title)

try:
    username = WebDriverWait(driver,100).until(
       EC.presence_of_element_located((By.XPATH, "//body/section[@id='login']/div[1]/div[1]/form[1]/input[2]"))
    )
    username.click()
    username.send_keys("slambergamer@gmail.com")
except:
    pass

try:
    password = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//body/section[@id='login']/div[1]/div[1]/form[1]/input[3]"))
    )
    password.click()
    password.send_keys("!yqxeQ2d!qrM5Bt")
    password.send_keys(Keys.RETURN)
except:
    pass

x=4315;
list = []
level = []
lonline =[]
NOVALUE = str("NaN")

while x < len(fsa):

    try:
        driver.get(fsa[x]);
        x += 1

        try:

            name = WebDriverWait(driver, 0).until(
                EC.presence_of_element_located((By.XPATH, "//body/section[@id='main-wrapper']/div[@id='main']/section[@id='content']/div[@id='profile']/div[@id='profile-wrapper']/h1[1]")))

            levell = WebDriverWait(driver, 0).until(
                EC.presence_of_element_located((By.XPATH, "//body/section[@id='main-wrapper']/div[@id='main']/section[@id='content']/div[@id='profile']/div[@id='profile-wrapper']/div[@id='profile-info']/div[3]/div[2]")))

            lonlinee = WebDriverWait(driver, 0).until(
                EC.presence_of_element_located((By.XPATH, "//body/section[@id='main-wrapper']/div[@id='main']/section[@id='content']/div[@id='profile']/div[@id='profile-wrapper']/div[@id='profile-info']/div[2]/div[3]")))

            if driver.find_element_by_xpath("//body/section[@id='main-wrapper']/div[@id='main']/section[@id='content']/div[@id='profile']/div[@id='profile-wrapper']/h1[1]"):
                user = str(name.text)
                levelll = str(levell.text)
                lonlineee = str(lonlinee.text)
                list.append(user)
                level.append(levelll)
                lonline.append(lonlineee)

                print(list)
                print(level)
                print(lonline)
                print(x)

                data = [list, level, lonline]
                export_data = zip_longest(*data, fillvalue='')
                file = open('username data.csv', 'w', encoding="ISO-8859-1", newline='')
                with file:
                    write = csv.writer(file)
                    write.writerows(export_data)

        except:
            pass
    except:
        pass




