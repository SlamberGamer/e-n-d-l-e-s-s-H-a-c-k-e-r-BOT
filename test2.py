from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui, sys
from selenium.common.exceptions import NoSuchElementException


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(10)

driver.get("https://www.endlesshacker.com/")


print(driver.title)

try:
    username = WebDriverWait(driver,100).until(
       EC.presence_of_element_located((By.XPATH, "//body/section[@id='login']/div[1]/div[1]/form[1]/input[2]"))
    )
    username.click()
    username.send_keys("username")
except:
    pass

try:
    password = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//body/section[@id='login']/div[1]/div[1]/form[1]/input[3]"))
    )
    password.click()
    password.send_keys("pass")
    password.send_keys(Keys.RETURN)
except:
    pass



while True:

    try:
        smalljobstatus = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, "//span[@id='jcount']"))
        )
        print(smalljobstatus.text)
        smalljobstatuscon = str(smalljobstatus.text)
        ready = str("READY!")
        print(smalljobstatuscon)
        print(ready)

        time.sleep(1)

        try:

            if smalljobstatuscon == ready:

                smallhack = WebDriverWait(driver, 100).until(
                    EC.presence_of_element_located((By.XPATH, "//span[@id='jcount']"))
                )
                smallhack.click()


                try:
                    try:
                        captcha = WebDriverWait(driver, 1).until(
                            EC.presence_of_element_located((By.XPATH, "//div[@id='epicaptcha_message']"))
                        )
                    except NoSuchElementException:
                        pass

                    captcha = str(captcha.text)
                    print(captcha)
                    captxt = str('Move your mouse cursor through the bar above from left to right')
                    print(captxt)

                    try:
                        if captcha == captxt:
                            print("yesss")
                            pyautogui.moveTo(1095, 550)
                            pyautogui.moveTo(1855, 550, 2.5)
                            pyautogui.moveTo(1095, 600)
                            pyautogui.moveTo(1855, 600, 2.5)
                            pyautogui.moveTo(1095, 650)
                            pyautogui.moveTo(1855, 650, 2.5)
                            pyautogui.moveTo(1095, 700)
                            pyautogui.moveTo(1855, 700, 2.5)

                            # pyautogui.moveTo(996, 280)
                            # pyautogui.moveTo(1364, 280, 3)
                            # pyautogui.moveTo(1019, 501)
                            # pyautogui.moveTo(1858, 501, 3)
                            # pyautogui.moveTo(1019, 589)
                            # pyautogui.moveTo(1858, 589, 3)

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

                    job = WebDriverWait(driver, 1).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "//label[contains(text(),'Try to get acces to the local traffic lights.')]"))
                            # (By.XPATH, "//label[contains(text(),'Try to blackmail a hacker.')]"))

                    )
                    job.click()

                except:
                    pass

                try:
                    trythisjob = WebDriverWait(driver, 1).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@value='Try this job' and @class='light-bg']"))
                    )
                    trythisjob.click()

                except:
                    pass

        except:
            pass

    except:
        pass



# while (smalljobstatuscon == ready):


