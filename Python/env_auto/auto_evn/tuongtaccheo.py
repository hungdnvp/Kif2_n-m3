
import  requests

# log = requests.post('https://tuongtaccheo.com/logintoken.php',data={'access_token':'e93ebbdcd0aaab340a22a9ddb91c6914'})


scraping_url = "https://covidapi.info/api/v1/country/VNM"

response = requests.get(scraping_url)

print(response.json())

# POST https://tuongtaccheo.com/logintoken.php
# Content-type: application/x-www-form-urlencoded
# Body:
# access_token: {TTC_Access_token của bạn}

