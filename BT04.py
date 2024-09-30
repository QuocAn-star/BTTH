from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo webdriver
driver = webdriver.Chrome()

for i in range(65, 91):
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22"+chr(i)+"%22"

    try:
        # Mở trang
        driver.get(url)

        # Đợi một chút để trang tải
        time.sleep(2)

        # Lấy ra tất cả các thẻ ul
        ul_tags = driver.find_elements(By.TAG_NAME, "ul")
        print(len(ul_tags))

        # Chọn thẻ ul thứ 21
        if len(ul_tags) > 20:
            ul_painters = ul_tags[20]  # list start with index = 0

            # Lấy ra tất cả thẻ <li> thuộc ul_painters
            li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

            # Tạo danh sách các url
            links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]

            # Tạo danh sách các title
            titles = [tag.find_element(By.TAG_NAME, "a").get_attribute("title") for tag in li_tags]

            # In ra các title
            for title in titles:
                print(title)
        else:
            print(f"Không tìm thấy ul thứ 21 trên trang: {url}")

    except Exception as e:
        # Bắt lỗi và in ra thông báo lỗi
        print(f"Error at {url}: {e}")

# Đóng web
driver.quit()
