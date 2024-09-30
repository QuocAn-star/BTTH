from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import re

######################################################
# I. Tạo danh sách chứa links và DataFrame rỗng
all_links = []
d = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})

# Khởi tạo Webdriver
driver = webdriver.Chrome()

######################################################
# II. Lấy ra tất cả đường dẫn để truy cập đến họa sĩ
for i in range(65, 91):  # Từ 'A' đến 'Z'
    url = f"https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22{chr(i)}%22"
    try:
        # Mở trang
        driver.get(url)
        # Chờ cho trang được tải đầy đủ
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "ul")))

        # Lấy ra tất cả các thẻ ul
        ul_tag = driver.find_elements(By.TAG_NAME, "ul")

        # Chọn thẻ ul thứ 20
        if len(ul_tag) > 20:
            ul_painters = ul_tag[20]  # list start with index = 0

            # Lấy ra tất cả các thẻ <li> thuộc ul_painters
            li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

            links = []
            for tag in li_tags:
                try:
                    links.append(tag.find_element(By.TAG_NAME, "a").get_attribute("href"))
                except Exception as e:
                    print(f"Lỗi khi lấy thông tin từ thẻ <li>: {e}")
                    continue

            all_links.extend(links)  # Dùng extend để không tạo danh sách lồng
    except Exception as e:
        print(f"Lỗi khi truy cập {url}: {e}")

######################################################
# III. Lấy thông tin của từng họa sĩ
for link in all_links:
    try:
        driver.get(link)
        time.sleep(2)

        # Lấy tên họa sĩ
        try:
            name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text
        except:
            name = ""

        # Lấy ngày sinh
        try:
            birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
            birth = birth_element.text
            birth_match = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', birth)
            birth = birth_match[0] if birth_match else ""
        except:
            birth = ""

        # Lấy ngày mất
        try:
            death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
            death = death_element.text
            death_match = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', death)
            death = death_match[0] if death_match else ""
        except:
            death = ""

        # Lấy quốc tịch
        try:
            nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
            nationality = nationality_element.text
        except:
            nationality = ""

        # Tạo dictionary thông tin của họa sĩ
        painter = {'name': name, 'birth': birth, 'death': death, 'nationality': nationality}

        # Chuyển đổi dictionary thành DataFrame và thêm vào DataFrame chính
        painter_df = pd.DataFrame([painter])
        d = pd.concat([d, painter_df], ignore_index=True)

    except Exception as e:
        print(f"Error fetching painter info from {link}: {e}")

######################################################
# IV. Lưu thông tin vào file Excel
try:
    file_name = 'Painters.xlsx'
    d.to_excel(file_name, index=False, engine='openpyxl')  # index=False để không lưu chỉ số
    print(f'Tệp Excel "{file_name}" đã được lưu thành công!')
except Exception as e:
    print(f'Đã xảy ra lỗi khi lưu tệp Excel: {e}')

# Đóng webdriver sau khi lấy thông tin
driver.quit()
