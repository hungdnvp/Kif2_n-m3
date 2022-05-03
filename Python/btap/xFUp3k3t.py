import os, sys, requests, time, re
s=requests.session()
s1=requests.session()
s.headers.update({
		"Host":"tuongtaccheo.com",
		"x-requested-with":"XMLHttpRequest",
		"content-type":"application/x-www-form-urlencoded",
		"user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
		"accept":"application/json, text/javascript, */*; q=0.01",
})
s1.headers.update({"Host":"mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","cookie":""})
log = requests.post("https://tuongtaccheo.com/login.php",data={
	"username":"",
	"password":"",
	"submit":"ĐĂNG+NHẬP"},headers={
		"Host":"tuongtaccheo.com",
		"upgrade-insecure-requests":"1",
		"content-type":"application/x-www-form-urlencoded",
		"user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	},allow_redirects=False)
cookie=log.cookies
like = s.get("https://tuongtaccheo.com/kiemtien/getpost.php",cookies=cookie).json()
id = like[0]["idpost"]
link = s1.get("https://mbasic.facebook.com/%s"%id).url
print(link)
access = s1.get(link).text
check_node = re.findall('/a/like.php?.*?"', access)
if check_node == []:
	print("éo có nút like")
else:
	node_like = check_node[0].replace('"',"").replace("amp;","")
	s1.get("https://mbasic.facebook.com%s"%node_like)
	receive = s.post("https://tuongtaccheo.com/kiemtien/nhantien.php", cookies=cookie, data={"id":id})
	print(receive.json())
###Sub
sub = s.get("https://tuongtaccheo.com/kiemtien/subcheo/getpost.php",cookies=cookie).json()
id_sub = sub[0]["idpost"]
link1 = s1.get("https://mbasic.facebook.com/%s"%id_sub).url
print(link1)
access1 = s1.get(link1).text
check_node_sub = re.findall('/a/subscribe.php?.*?"', access1)
if check_node_sub == []:
	print("éo có nút sub")
else:
	node_sub = check_node_sub[0].replace('"',"").replace("amp;","")
	s1.get("https://mbasic.facebook.com%s"%node_sub)
	receive_sub = s.post("https://tuongtaccheo.com/kiemtien/subcheo/nhantien.php", cookies=cookie, data={"id":id_sub})
	print(receive_sub.json())
###Page
like_page = s.get("https://tuongtaccheo.com/kiemtien/likepagecheo/getpost.php",cookies=cookie).json()
id_page = like_page[0]["idpost"]
link2 = s1.get("https://mbasic.facebook.com/%s"%id_page).url
print(link2)
access2 = s1.get(link2).text
check_node_page = re.findall('/a/profile.php?.*?"', access2)
if check_node_page == []:
	print("éo có nút like")
else:
	node_like_page = check_node_page[0].replace('"',"").replace("amp;","")
	s1.get("https://mbasic.facebook.com%s"%node_like_page)
	receive2 = s.post("https://tuongtaccheo.com/kiemtien/likepagecheo/nhantien.php", cookies=cookie, data={"id":id_page})
	print(receive2.json())
###Cảm Xúc
react = s.get("https://tuongtaccheo.com/kiemtien/camxuccheo/getpost.php",cookies=cookie).json()
id_cx = react[0]["idpost"]
loaicx = react[0]["loaicx"]
link3 = s1.get("https://mbasic.facebook.com/%s"%id_cx).url
print(link3)
access3 = s1.get(link3).text
check_node_cx = re.findall('/reactions/picker/?.*?"', access3)
if check_node_cx == []:
	print("éo có nút cảm xúc")
else:
	node_like_cx = check_node_cx[0].replace('"',"").replace("amp;","")
	reaction = s1.get("https://mbasic.facebook.com%s"%node_like_cx).text
	i = 0 if loaicx == "LIKE" else 1 if loaicx == "LOVE" else 2 if loaicx == "CARE" else 3 if loaicx == "HAHA" else 4 if loaicx == "WOW" else 5 if loaicx == "SAD" else 6
	node_react = re.findall('/ufi/reaction/?.*?"', reaction)[i].replace('"',"").replace("amp;","")
	s1.get("https://mbasic.facebook.com%s"%node_react)
	receive3 = s.post("https://tuongtaccheo.com/kiemtien/camxuccheo/nhantien.php", cookies=cookie, data={"id":id_cx,"loaicx":loaicx})
	print(receive3.json())