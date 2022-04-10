from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

try:
    smalljobstatus = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//span[@id='jcount']"))
    )
    print(smalljobstatus.text)
    smalljobstatuscon = str(smalljobstatus.text)
    ready = str("READY!")
    print(smalljobstatuscon)
    print(ready)

    if smalljobstatuscon == ready:
        smallhack = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, "//span[@id='jcount']"))
        )
        smallhack.click()

except:
    pass

try:
    job1 = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'A hacker challenges you to free bubba.')]"))
    )
    job1.click()

    trythisjob = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//body/section[@id='main-wrapper']/div[@id='main']/section[@id='content']/div[@id='joblist']/div[3]/form[1]/div[11]/div[1]/input[1]"))
    )
    trythisjob.click()

except:
    pass

