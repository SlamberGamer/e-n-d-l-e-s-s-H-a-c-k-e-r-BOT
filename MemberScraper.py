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

x=158;
list = []
level = []
lonline =[]
NOVALUE = str("NaN")

while x < len(fsa):

    try:
        driver.get(fsa[x]);
        x += 1

        try:
            captcha = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='epicaptcha_message']"))
            )
            captcha = str(captcha.text)
            print(captcha)
            captxt = str('Move your mouse cursor through the bar above from left to right')
            print(captxt)

            try:
                if captcha == captxt:
                    print("yesss")
                    x -= 1
                    # pyautogui.moveTo(1095,350)
                    # pyautogui.moveTo(1855, 350, 1)
                    # pyautogui.moveTo(1095, 400)
                    # pyautogui.moveTo(1855, 400, 1)
                    # pyautogui.moveTo(1095, 500)
                    # pyautogui.moveTo(1855, 500, 2.5)
                    pyautogui.moveTo(996, 280)
                    pyautogui.moveTo(1364, 280, 3)
                    pyautogui.moveTo(1019, 501)
                    pyautogui.moveTo(1858, 501, 3)
                    pyautogui.moveTo(1019, 589)
                    pyautogui.moveTo(1858, 589, 3)
                    # pyautogui.moveTo(1095, 550)
                    # pyautogui.moveTo(1855, 550, 2.5)
                    # pyautogui.moveTo(1095, 600)
                    # pyautogui.moveTo(1855, 600, 2.5)
                    # pyautogui.moveTo(1095, 650)
                    # pyautogui.moveTo(1855, 650, 2.5)
                    # pyautogui.moveTo(1095, 700)
                    # pyautogui.moveTo(1855, 700, 2.5)
                    # pyautogui.moveTo (1095,624,3)

                    submit = WebDriverWait(driver, 1).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@id='epi']"))
                    )
                    submit.click()

                    # time.sleep(1)
            except:
                pass
        except:
            pass

        try:
            NaN = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Hacker not found.')]"))
            )
            NaNN = str(NaN.text)
            print(NaNN)
            NaNtxt = str('Hacker not found.')
            print(NaNtxt)

            try:
                if NaNN == NaNtxt:
                    print("if nan == nantxt")
                    print(NaNN, "=", NaNtxt)
                    list.append(NaNN)
                    level.append(NOVALUE)
                    lonline.append(NOVALUE)

                    print(list)
                    print(level)
                    print(lonline)

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

        try:
            excessively = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'You are on a 5 minute captcha lockout for refreshi')]"))
            )
            excessivelyy = str(excessively.text)
            excessivelytxt = str('You are on a 5 minute captcha lockout for refreshing the captcha excessively.')

            try:
                if excessivelyy == excessivelytxt:
                    x-=1
            except:
                pass
        except:
            pass

        try:
            disableacc = WebDriverWait(driver, 0).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'You can not view profiles of disabled accounts.')]"))
            )
            disableaccc = str(disableacc.text)
            disableacctxt = str('You can not view profiles of disabled accounts.')

            try:
                if disableaccc == disableacctxt:
                    print(disableaccc, '=', disableacctxt)
                    list.append(disableaccc)
                    level.append(NOVALUE)
                    lonline.append(NOVALUE)

                    print(list)
                    print(level)
                    print(lonline)

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


        name = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, "//body/section[@id='main-wrapper']/div[@id='main']/section[@id='content']/div[@id='profile']/div[@id='profile-wrapper']/h1[1]")))

        levell = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, "//body/section[@id='main-wrapper']/div[@id='main']/section[@id='content']/div[@id='profile']/div[@id='profile-wrapper']/div[@id='profile-info']/div[3]/div[2]")))

        lonlinee = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, "//body/section[@id='main-wrapper']/div[@id='main']/section[@id='content']/div[@id='profile']/div[@id='profile-wrapper']/div[@id='profile-info']/div[2]/div[3]")))

        user = str(name.text)
        levelll = str(levell.text)
        lonlineee = str(lonlinee.text)
        list.append(user)
        level.append(levelll)
        lonline.append(lonlineee)

        print(list)
        print(level)
        print(lonline)

        data = [list, level, lonline]
        export_data = zip_longest(*data, fillvalue='')
        file = open('username data.csv', 'w', encoding="ISO-8859-1", newline='')
        with file:
            write = csv.writer(file)
            write.writerows(export_data)

    except:
        pass




