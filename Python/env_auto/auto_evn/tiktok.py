import time,requests
from selenium import webdriver


# tai khoan tuongtaccheo
username = 'hungdnvp'
password = 'mothaibabonnam12345'

# request
# session_ttc = requests.session()
# header = {
#             'accept-language': 'vi,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
#             'referer': 'https://tuongtaccheo.com/index.php',
#             'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': "Windows",
#             'sec-fetch-dest': 'document',
#             'sec-fetch-mode': 'navigate',
#             'sec-fetch-site': 'same-origin',
#             'sec-fetch-user': '?1',
#             'upgrade-insecure-requests': '1',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'
#         }
# session_ttc.headers.update(header)
# head = {
#             "Host":"tuongtaccheo.com",
#             "x-requested-with":"XMLHttpRequest",
#             "content-type":"application/x-www-form-urlencoded",
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
#             "accept":"application/json, text/javascript, */*; q=0.01",
#         }

# data = {
#             'username':username,
#             'password':password,
#             'submit':'ĐĂNG NHẬP'
#         }
# login_in = session_ttc.post('https://tuongtaccheo.com/login.php',data=data,allow_redirects=False,timeout=10)
# cookie_ttc = login_in.cookies
# session_ttc.headers.update(head)
# getlink = session_ttc.get("https://tuongtaccheo.com/tiktok/kiemtien/getpost.php",cookies=cookie_ttc).json()
# list_link = []
# for i in getlink:
#     list_link.append(i["link"])


#     'cookie':'passport_csrf_token=ade3805159d80723900a0169f399b345; passport_csrf_token_default=ade3805159d80723900a0169f399b345; MONITOR_WEB_ID=f496ccc9-03fe-4daf-a81f-8a92c79b2fde; MONITOR_DEVICE_ID=0a6383c9-82b0-4d56-986c-6cb3c693d706; d_ticket=a0e27337decc58f0d0f286867ef7d76a1c349; passport_auth_status=71f823ad64acd5ade212bca7fbe04d62%2C; passport_auth_status_ss=71f823ad64acd5ade212bca7fbe04d62%2C; sid_guard=a43a5a5be35721d89f56bbc0da48d5d0%7C1646925195%7C5184000%7CMon%2C+09-May-2022+15%3A13%3A15+GMT; uid_tt=0cefb8053645f69670759d79fa6dba153c02cba20781cccaa17cf7e36109c7fe; uid_tt_ss=0cefb8053645f69670759d79fa6dba153c02cba20781cccaa17cf7e36109c7fe; sid_tt=a43a5a5be35721d89f56bbc0da48d5d0; sessionid=a43a5a5be35721d89f56bbc0da48d5d0; sessionid_ss=a43a5a5be35721d89f56bbc0da48d5d0; sid_ucp_v1=1.0.0-KDIxNWEwNzA5Yjc3ZWJiNWU3YmRiMWJlZTNkMWI1YWRkYTYxY2U5NTQKIAiBiIvYntWClWIQi6uokQYYswsgDDC_laiRBjgBQOoHEAEaA3NnMSIgYTQzYTVhNWJlMzU3MjFkODlmNTZiYmMwZGE0OGQ1ZDA; ssid_ucp_v1=1.0.0-KDIxNWEwNzA5Yjc3ZWJiNWU3YmRiMWJlZTNkMWI1YWRkYTYxY2U5NTQKIAiBiIvYntWClWIQi6uokQYYswsgDDC_laiRBjgBQOoHEAEaA3NnMSIgYTQzYTVhNWJlMzU3MjFkODlmNTZiYmMwZGE0OGQ1ZDA; store-idc=useast2a; store-country-code=vn; tt-target-idc=alisg; tt_csrf_token=d8P67HKIK2ls4sGoRntmsPsC; bm_sz=6A0E5ACEF5FB7650ED6395F8E96EC967~YAAQtVFNGyAzU2d/AQAA6MuFdw/eEYHgQke+3ZIC3yLWKbqTQFxe12WkN4oQx8g1cQQ+6nKqfloygCGxrSYAwENWG+RQZI+zirRcavbpAIUrE2maqCHTGWT//rrHlxp16ZZOA8eo5U+7dwQolNhX7VhgWawAXlP2/qhIhHGvPuwim2jIOmHtwhzgO4ZC8Dq73ex7l09mMNgALfdabKAC1A/e3wfrcc/MGAZUB9xhTM6OTSwcBRKKfRea9sPLw7LgL0fBCO0CsrMd3jbLh6pp69x2svzc+twJFumSB1eyii8Vjdo=~3687493~4535348; passport_fe_beating_status=true; cmpl_token=AgQQAPOFF-RMpbIU5A5jMB04-GEC1_4P_4MOYMFB6Q; bm_mi=8DB4EEE6AD4EB4C43380512AA38E193A~VSwjBPP2+KK/Jt30L+zzntxnhmHHWJwO7d9iRMZfq36iGgBqljojexBgsjRh80JFNQ6tY9k9Jb6ECMWMc6RjGQfhbRRakCX2AvTpcOPNpIVOGmi//bGziFyJCJ0nsJjiF7nLN/t4bs7qJ8VtJghA1AKimtwwao4hqHhU1uveKSA4nugmJS9ND4zohb0GOn4YM8LJySYl9NDU44qTD5tBW4rb6GfRBg0lr9QrG1eUISMY/1+gUloy41SJaRzkwfHI9/AM4/sizFStiVaXqZWHVg==; bm_sv=CB4D1558475B4A80ECC97BE4435C1E2B~yJVpabFZBV2LFNRQ6kjjIUYQX9TJEgYPmA7DAepMZxNxCv0J8Tb7StQcvz3a7SfapSlYBLcfl+AJOx1UklNC3gF6UqaxjNl2ADKCODXGUrflZYFoUO2E7rUChocUhsFvwTBC2lMLNigXCoTJdnWFZEDDOzboVSVZpZgxb99X3Mc=; ak_bmsc=B70A79849923178EBCA0531E17F2DBF0~000000000000000000000000000000~YAAQl1FNG5FxqWl/AQAAxryjdw8Mrj5tMaxOfJPN5tYM2SCURiKG5Wb8igD1RIEby6sggGFxminI7hMn5M1yhniQqmQF1kUurat6lo5qVg74JYCFNC1EnxccuaeJ1tKIPKE37NrWzapgv/MYgNp3VBN0qbqIlzq0a8OYCjW4uwkRkRd6w708vopfN6ISSBh5twgfgVC/YsR3y757bM3KpgRiTVUaWosbyR69nPPTsV++3qSHBduXzWWm8WCgkO8UMYMmVnNweywdkV0pttokb8remil72yYAyJFren5jJ7eFFTuAc+TP+PDM6jlOs954y9EDfAaUtWYPjm/xFhbqCaFVDVMUj7nd5uNi9w+tYL/5ZyrJ7VQMBIh7nrmo2JXeZpiXsEyHWDFxXWT5p3QW1LYAhulq1f5W6cql2edn0FHtIeTTXAhgzwMCWLQ2facRyTQW4+6e47C3DMPctVq+2mKbPkE=; _abck=2E1268756AEC5730251517EE379DC0FF~-1~YAAQdFFNG1ugR2Z/AQAAJdGkdwcaJCv0utcZ6+YQFYG+zoe51Aqgka9KpyjVA8bWGxY26DGKmNJcX4RFVFZU79qNCtOX3iShas+FdzWBUZcz0l43WBeLSZ5AQL2Gddk9alU5MNXC4F3l5vBlW3TXibAXsx1r9sTpbl8aK1dwXi/LxMzJd1vKdQ2jg5TqITaxz1DB4mI2xgTLgXlOFIzmDH8/o62FsJ0MuvM+1FDSx7AwQki0h2Dtne7TDDfdywkjouS91KB8nq621ih+aGuz3xVsn9GVER8SY7c5IBIXk8TyM4AKFwg0VP6F4p8VVzYTOT6poEusIeDs/n1LDKkoEAPhHHsrLlEY20uoyQWmG+8grWug+jM8NXcteZiups/zSy7QyMRgO7Mlew==~-1~-1~-1; odin_tt=02d32d2a43d806739ff71c0bb33c8e9c4cd1161309597c28c9245f156457562cd6f755e35cdb46bcb6a24a58c30e4f71044a85af18e5d9968331368b3af605f585b58a73737f06fc7dfeecbb21a903cd; ttwid=1%7C22CrHdmi7MgzBZCx7qeK63KFg-RyWdCWZAUFsZchkLA%7C1646980397%7C087b230b4ac1c20e361308e52b959e8f84a27f0bd5356eb366e0263fa0134da1; msToken=PSf2D5L9pcGsSxlW2P7oPVd86_tbNPe7Pr00TbkmDWzK4DluhAr3ULT6SlCAdCSAsmUHbjlH9MV1waquKcV71MkGBdW2MLqxUc6KraAYys9XyUZ7f4FPdpv0JJH6EX4hxKnAh1IwZnEGCDzS; msToken=9-2NQXP7MDlVtGJKIFMz2NHAnSf-LiMa-n_Tte0dfCSjE-2o3kGV0_udOMNxciy05YENzJ559Dohb63clQZZXugBimmPf5yJniqQWK_pff8gAepZy5aydhEOaUJgBvAPaFWZkHnbGJDLPEMi'

driver = webdriver.Chrome(executable_path="C:\\Users\\Quang_Hung\\Downloads\\app\\chromedriver_win32\\chromedriver.exe")
driver.set_window_size(1200,800)
driver.get("https://google.com")
# driver.get("https://www.tiktok.com/login/phone-or-email/email")
# time.sleep(5)
# driver.find_element_by_name('email').send_keys('quanghungorc@gmail.com')
# driver.find_element_by_name('password').send_keys('MTA@nhockoi2001')
# time.sleep(5)
# driver.execute_script('document.querySelector("button.login-button-31D24.highlight-1TvcX").click()')
# time.sleep(5)

# driver.get(list_link[0])

# driver.execute_script('document.querySelector("button.tiktok-1xiuanb-ButtonActionItem.e1bs7gq20").click()')
# receive = session_ttc.post("https://tuongtaccheo.com/tiktok/kiemtien/nhantien.php", cookies=cookie_ttc)
# print(receive.json())
