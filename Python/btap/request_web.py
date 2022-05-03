import requests
import time
import re

# tai khoan tuongtaccheo
username = 'hungdnvp'
password = 'mothaibabonnam12345'

# request
session_ttc = requests.session()
header = {
            'accept-language': 'vi,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'referer': 'https://tuongtaccheo.com/index.php',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'
        }
session_ttc.headers.update(header)
data = {
            'username':username,
            'password':password,
            'submit':'ĐĂNG NHẬP'
        }
login_in = session_ttc.post('https://tuongtaccheo.com/login.php',data=data,allow_redirects=False,timeout=10)
cookie_ttc = login_in.cookies
session_ttc.cookies.update(login_in.cookies)

    
def checkxu(self):
    getxu = session_ttc.get("https://tuongtaccheo.com/home.php")
    xu_now = getxu.text.split('id="soduchinh">')[1].split('</strong>')[0]
    return xu_now

###############confix*******
head = {
            "Host":"tuongtaccheo.com",
            "x-requested-with":"XMLHttpRequest",
            "content-type":"application/x-www-form-urlencoded",
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
            "accept":"application/json, text/javascript, */*; q=0.01",
        }
session_ttc.headers.update(head)
getpost = session_ttc.get("https://tuongtaccheo.com/kiemtien/getpost.php",cookies=cookie_ttc).json()
list_idpost = []
for i in getpost:
    list_idpost.append(i["idpost"])

    ##################_____-------___________OK ID LIKE________



# logfb
cookie_fb ='sb=lf4eYm7KtZjGSGfkTnCUcIFR; datr=mP4eYjjdROy8KWtC5TcBwHT2; dpr=1.1458333730697632; locale=vi_VN; c_user=100004779240033; xs=6:h6EQlM8fd9nM5g:2:1646219833:-1:13085::AcWWD7jwY1M_KNO7CWE1dnSOMO9lYqKDr7ZRv2cjSA; wd=1411x705; fr=0JQSsCZYoohdX5Q5N.AWXJOsfrPjVrM2w7uOLHM0msf10.BiIIML.xg.AAA.0.0.BiII6x.AWWF0CzcqiM'

session_fb = requests.session()
session_fb.headers.update(
{
    "Host":"mbasic.facebook.com",
    "content-type":"application/x-www-form-urlencoded",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site":"same-origin",
    "sec-fetch-mode":"navigate",
    "sec-fetch-user":"?1",
    "sec-fetch-dest":"document",
    "cookie":cookie_fb
})
# urllike = 'https://graph.facebook.com/'+str(idlike)+'/likes'
datalike = "access_token="+'EAAGNwlgFPQYBAHQkzh9gASfuECVidBZADkdw87MwYzgNHCDhbWPBIDmv12wSgHw6T88ZCBjfgGZBCZAI24LuT7bKx1lTnlCSY2eEhcfWkSVB0a6XrvJPUb99VI2eRLYre9GeCfs1ZBcUOPpEgZA7QRV9C2gAjN2daHlGeMpXof9KVmDYYBuuELibe0WIKDx90ZD'
idpost = list_idpost[0]
idpost = '279828580968894'
#**********_____________-------------SU DUNG COOKIE______------------
# for idpost in list_idpost:

link = session_fb.get("https://mbasic.facebook.com/%s"%idpost).url 
access = session_fb.get(link).text
check_node = re.findall('/a/like.php?.*?"', access)
if check_node == []:
    print("ko có nút like")
else:
    node_like = check_node[0].replace('"',"").replace("amp;","")
    session_fb.get("https://mbasic.facebook.com%s"%node_like)   
    receive = session_ttc.post("https://tuongtaccheo.com/kiemtien/nhantien.php", cookies=cookie_ttc, data={"id":idpost})
    print(receive.json())

    ######################### SU DUNG TOKEN
# urllike = 'https://graph.facebook.com/'+str(idpost) +'/likes'
# like = requests.post(urllike, data=datalike)
# print(like)
# receive = session_ttc.post("https://tuongtaccheo.com/kiemtien/nhantien.php", cookies=cookie_ttc, data={"id":idpost})
# print(receive.json())

# home_ttc = session_ttc.get(f'https://tuongtaccheo.com/home.php')
# print(home_ttc.text)
# xu = home_ttc.text.split('id="soduchinh">').split('</strong>')[0]
# print('Xu Hiện Tại: ', xu)






