import requests
url = "https://real-time-amazon-data.p.rapidapi.com/search"

querystring = {"query":"Phone","page":"1","country":"US","category_id":"aps"}

headers = {
	"X-RapidAPI-Key": "55bf7ea8bbmsh50ac1576f0dcf48p1c6b41jsn05c690cab719",
	"X-RapidAPI-Host": "real-time-amazon-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data=pd.DataFrame(response.json()['data'])
# data.shape
# data -> google collab/jupiter 
data.to_csv('amazon.csv')
pd.read_csv('amazon.csv')

