from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import wget

driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.instagram.com/')
username = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[name='username']"))).send_keys('##') #your username
password = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[name='password']"))).send_keys('##') #your password
Login = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[type='submit']"))).click()
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
search = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Search']")))
search.clear()
tosearch = '#dogs' #thing you want to search
search.send_keys(tosearch)
enter = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='fuqBx ']/div[1]"))).click()

#scroll down to scrape more images
driver.execute_script("window.scrollTo(0, 4000);")

#target all images on the page
img = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in img]

#saving
path = os.getcwd()#navigate to the path where you saved your coding file
path = os.path.join(path, tosearch[1:])

#create the directory
if not os.path.exists(path):
    os.mkdir(path)

c = 0
for img in images:
    save_as = os.path.join(path, tosearch[1:] + str(c) + '.png')
    wget.download(img, save_as)
    c += 1

print('All Done')

