from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
import time


# Đường Dẫn
gecko_path = "D:/Project 02/geckodriver.exe"
# khởi tới đối tượng dv vơi đường geckodriver
ser = Service(gecko_path)

# tạo tùy chọn
options = webdriver.firefox.options.Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
# thiết ập firefox chỉ hiện thị giao diện
options.headless = False

#Khởi tạo driver
driver = webdriver.Firefox(options = options, service=ser)

# tạo url
url = 'https://pythonscraping.com/pages/javascript/ajaxDemo.html'

#truy cập
driver.get(url)

#in ra nội dung của trang web
print("Before: ===========================")
print(driver.page_source)

#tạm dừng khoảng 3 giây
time.sleep(3)

#in lại
print("\n\n\n\nAfter: ========================")
print(driver.page_source)

#Dóng brower
driver.quit()