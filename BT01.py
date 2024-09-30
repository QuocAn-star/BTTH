from selenium import webdriver
from selenium.webdriver.common.by import By
# dung để ngưng đọng thời gian
import time

#khởi tạo webdriver
driver = webdriver.Chrome()

#mở trang
url = "https://en.wikipedia.org/wiki/list_of_painters_by_name"
driver.get(url)

# đợi khoảng 2 giây
time.sleep(2)

# lấy tắt cả các thẻ <a>
tags = driver.find_elements(By.TAG_NAME, "a");

#tạo ra danh sách các liên kết
#lấy tag trong cái thẻ
links = [tag.get_attribute("href") for tag in tags]

#xuất thông tin
for link in links:
    print(link)

#dòng xuất
driver.quit()