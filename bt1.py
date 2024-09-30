from selenium import webdriver
from selenium.webdriver.common.by import By
#2 dòng thu vien
import time
#khoi tao WebDriver
driver = webdriver.Chrome();

#Mo 1 trang web
driver.get("https://gomotungkinh.com")
time.sleep(500)
#tim phantu img co id a=lad "bonk"
bonk_img = driver.find_element(By.ID,"bonk")
#click lien tuc vao img"bonk"

while True:
 bonk_img.click()
from selenium import webdriver
from selenium.webdriver.common.by import By
#2 dong thu vien
import time
#khoi tao webdriver
driver = webdriver.Chrome();

#Mo 1 trang Web
driver.get("https://gomotungkinh.com")
time.sleep(500)
#tim phan tu img co id a=lad "bonk"
bonk_img = driver.find_element(By.ID,"bonk")
#click lien tuc vao img "bonk"

while true:
    bonk_img.click()
    from selenium import webdriver
    from selenium.webdriver.common.by import By
# 2 dong thu vien
import time
# khoi tao Webdriver
driver = webdriver.Chrome();

# Mo 1 trang web
driver.get("https://gomotungkinh.com")
time.sleep(5)
#tim phan tu img_co id la "bonk"
bonk_img = driver.find_element(By.ID,"bonk")
# click lien tuc vao img"bonk"

while True:
    bonk_img.click()
    print("click on the he bonk image")
    time.sleep(0,1)