import requests
scraping_url = "https://covidapi.info/api/v1/country/VNM"

response = requests.get(scraping_url)

print(response.json())