import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Quang_Hung\\Downloads\\app\\chromedriver_win32\\chromedriver.exe")

driver.set_window_size(900,800)
tooken_fb = 'EAAGNwlgFPQYBAHQkzh9gASfuECVidBZADkdw87MwYzgNHCDhbWPBIDmv12wSgHw6T88ZCBjfgGZBCZAI24LuT7bKx1lTnlCSY2eEhcfWkSVB0a6XrvJPUb99VI2eRLYre9GeCfs1ZBcUOPpEgZA7QRV9C2gAjN2daHlGeMpXof9KVmDYYBuuELibe0WIKDx90ZD'

driver.get("https://tuongtaccheo.com/home.php")


time.sleep(3)

driver.execute_script('document.querySelector("#memberModal > div > div > div.modal-footer > div > button").click()')

driver.find_element_by_id('name').send_keys('hungdnvp')
driver.find_element_by_id('password').send_keys('mothaibabonnam12345')
driver.find_element_by_name('submit').click()
# đăng nhập complete
time.sleep(3)
#kiếm xu
driver.execute_script('document.querySelector("#navbar > ul:nth-child(1) > li:nth-child(2) > a").click()')
time.sleep(1)
# like tương tác
# driver.execute_script('document.querySelector("#navbar > ul:nth-child(1) > li.dropdown.open > ul > li:nth-child(2) > a > i.fab.fa-facebook-square").click()')
# time.sleep(1)
# driver.execute_script('''document.querySelector('[class = "btn btn-default"]').click()''')
# time.sleep(7)
