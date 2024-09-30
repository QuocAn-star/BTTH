from selenium import webdriver
from selenium.webdriver.common.by import By
# dung để ngưng đọng thời gian
import time

#khởi tạo webdriver
driver = webdriver.Chrome()

#mở trang
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22P%22"
driver.get(url)

#đợi một chút để trang tải
time.sleep(2)

# lấy ra tất cả các thẻ ul
ul_tags = driver.find_elements(By.TAG_NAME, "ul")
print(len(ul_tags))

#for ul_tag in ul_tags:
#print(ul_tag.get_attribute())

# chọn thẻ ul thứ 21
ul_painters = ul_tags[20] #list start with index = 0

#lấy ra tất c thẻ <li> thuộc ul_painters
li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

# tạo danh sách cac url
links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]

#tạo danh sách các url
titles = [tag.find_element(By.TAG_NAME, "a").get_attribute("title") for tag in li_tags]

#in ra url
for link in titles:
    print(link)

# đóng web
driver.quit()