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

# lấy tắt cả các thẻ <a> với title chứa "List of painters"
tags = driver.find_elements(By.XPATH, "//a[contains(@title, 'List of painters')]");

#tạo ra danh sách các liên kết
#lấy tag trong cái thẻ
links = [tag.get_attribute("href") for tag in tags]

#xuất thông tin
for link in links:
    print(link)

#dòng xuất
driver.quit()