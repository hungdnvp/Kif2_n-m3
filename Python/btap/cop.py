import requests, time
s=requests.session()
s1=requests.session()
cookie_fb ='sb=lf4eYm7KtZjGSGfkTnCUcIFR; datr=mP4eYjjdROy8KWtC5TcBwHT2; dpr=1.1458333730697632; locale=vi_VN; c_user=100004779240033; xs=6:h6EQlM8fd9nM5g:2:1646219833:-1:13085::AcWWD7jwY1M_KNO7CWE1dnSOMO9lYqKDr7ZRv2cjSA; wd=1411x705; fr=0JQSsCZYoohdX5Q5N.AWXJOsfrPjVrM2w7uOLHM0msf10.BiIIML.xg.AAA.0.0.BiII6x.AWWF0CzcqiM'
s.headers.update({
        "Host":"tuongtaccheo.com",
        "x-requested-with":"XMLHttpRequest",
        "content-type":"application/x-www-form-urlencoded",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
        "accept":"application/json, text/javascript, */*; q=0.01",
})
s1.headers.update(
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
    #ok
log = requests.post("https://tuongtaccheo.com/login.php",data={
    "username":"hungdnvp",
    "password":"mothaibabonnam12345",
    "submit":"ĐĂNG+NHẬP"},headers={
        "Host":"tuongtaccheo.com",
        "upgrade-insecure-requests":"1",
        "content-type":"application/x-www-form-urlencoded",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    },allow_redirects=False)
cookie=log.cookies
    #end ok
like = s.get("https://tuongtaccheo.com/kiemtien/getpost.php",cookies=cookie).json()
id = like[0]["idpost"]
link = s1.get("https://mbasic.facebook.com/%s"%id).url
access = s1.get(link).text
# check_node = re.findall('/a/like.php?.*?"', access)
# if check_node == []:
#     print("éo có nút like")
# else:
#     node_like = check_node[0].replace('"',"").replace("amp;","")
#     s1.get("https://mbasic.facebook.com%s"%node_like)
#     receive = s.post("https://tuongtaccheo.com/kiemtien/nhantien.php", cookies=cookie, data={"id":id})
#     print(receive.json())