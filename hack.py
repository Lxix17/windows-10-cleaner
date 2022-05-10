#3R64W2pRH5SR9ObmY0dc3ihHFwLrxOJf
import requests

api = "http://api.windy.com/api/webcams/v2/list/country=PH/category=beach?show=webcams:url"

headers = {
    'x-windy-key':'3R64W2pRH5SR9ObmY0dc3ihHFwLrxOJf'
}
response = requests.get(url=api, headers=headers)

print(response.json())
