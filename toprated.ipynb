import pandas as pd
import requests
data=requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1')
df=pd.DataFrame()
print(df)
pd.DataFrame(data.json()['results']).head()
pd.DataFrame(data.json()['results'])[['id','title','overview','release_date','title']]
for i in range(1, 425):
    response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page={}'.format(i))
    temp = pd.DataFrame(response.json()['results'])[['id', 'title', 'overview', 'release_date']]
    df = pd.concat([df, temp], ignore_index=True)
df.head()
df.shape
df.to_csv('movies.csv')
pd.read_csv('movies.csv')
