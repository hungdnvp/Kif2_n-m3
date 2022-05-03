import sys
import os
import re
import json
import requests
from datetime import datetime
from time import sleep, time
import random

# os.system("clear")
dau = "\033[1;32m~ "
dem = 0
cookie = '_ga=GA1.2.1328820328.1643071374; __gads=ID=f5796e7eea91c4d0-225399092dd000c8:T=1643071375:RT=1643071375:S=ALNI_MaF_qlDYYh4ukr59YFN939MmLqulg; _fbp=fb.1.1643071375638.956500003; __tawkuuid=e::tuongtaccheo.com::mNOxMfDWfXqJP1MIOZ1y5RCr+y7VcUqT49sFB7l+i1RS0G0l6UkzFaT+jFu8al+X::2; _gid=GA1.2.308019050.1646102212; PHPSESSID=7j9fj750khc2fjbv8oi4690g26; _gat_gtag_UA_88794877_6=1; TawkConnectionTime=0'
# tokenfb = input(dau+'Nhập Token Fecabook : ')
healogin = {
    'Host': 'tuongtaccheo.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
    'cookie': cookie,
}
hea = {
    # 'Host': 'tuongtaccheo.com',
    # 'accept': 'application/json, text/javascript, */*; q=0.01',
    # 'accept-language': 'vi,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
    # 'x-requested-with': 'XMLHttpRequest',
    # 'cookie': cookie,
    # 'referer': 'https://tuongtaccheo.com/kiemtien/',
    # 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'sec-fetch-dest': 'empty',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-site': 'same-origin'
    # ':authority': 'tuongtaccheo.com',
    # ':method': 'GET',
    # ':path': '/kiemtien/getpost.php',
    # ':scheme': 'https',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'vi,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'cookie': '_ga=GA1.2.1328820328.1643071374; __gads=ID=f5796e7eea91c4d0-225399092dd000c8:T=1643071375:RT=1643071375:S=ALNI_MaF_qlDYYh4ukr59YFN939MmLqulg; _fbp=fb.1.1643071375638.956500003; __tawkuuid=e::tuongtaccheo.com::mNOxMfDWfXqJP1MIOZ1y5RCr+y7VcUqT49sFB7l+i1RS0G0l6UkzFaT+jFu8al+X::2; _gid=GA1.2.1329504914.1646225563; PHPSESSID=sq9nv608qu38eli4oiu31m06q3; TawkConnectionTime=0; _gat_gtag_UA_88794877_6=1',
    'referer': 'https://tuongtaccheo.com/kiemtien/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
    'x-requested-with': 'XMLHttpRequest'

}
heanhan = {
    'Host': 'tuongtaccheo.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
    'x-requested-with': 'XMLHttpRequest',
    'origin': 'https://tuongtaccheo.com',
    'referer': 'https://tuongtaccheo.com/kiemtien/',
    'cookie': cookie,
}
# b = requests.get(f'https://tuongtaccheo.com/home.php', headers=healogin,timeout=10)
# print(b.text)
# xu = b.text.split('id="soduchinh">')     #.split('</strong>')[0]
# print(dau+'Xu Hiện Tại: ', xu)

# while (True):
# a = requests.get(f'https://tuongtaccheo.com/kiemtien/getpost.php', headers=hea)
# x = a.text.split('idpost":"')[1]
# print(str(a.content))
# idlike = x.split('","link')[0]
idlike = '1543051426082203'
# print('🌸Đang Like ID: ', idlike)
link = 'https://www.facebook.com/100036221520538/posts/653109519239760'
# urllike = 'https://graph.facebook.com/'+str(idlike)+'/likes'
urllike = 'https://graph.facebook.com/'+'1543051426082203'+'/likes'

datalike = "access_token="+'EAAGNwlgFPQYBAHQkzh9gASfuECVidBZADkdw87MwYzgNHCDhbWPBIDmv12wSgHw6T88ZCBjfgGZBCZAI24LuT7bKx1lTnlCSY2eEhcfWkSVB0a6XrvJPUb99VI2eRLYre9GeCfs1ZBcUOPpEgZA7QRV9C2gAjN2daHlGeMpXof9KVmDYYBuuELibe0WIKDx90ZD'
da = {
    'id': idlike,
}
like = requests.post(urllike, data=datalike)
nhan = json.loads(requests.post('https://tuongtaccheo.com/kiemtien/nhantien.php', headers=heanhan, data=da).text)
print(nhan)
# sleep(10)
