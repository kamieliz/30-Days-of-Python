import requests
import pprint
import pandas as pd

api_key = 'c5e97a575a624b8381e45ce29e1c7c57'
api_key_v4 = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNWU5N2E1NzVhNjI0YjgzODFlNDVjZTI5ZTFjN2M1NyIsInN1YiI6IjYyMGFhY2EwMDE0MzI1MDAxYjU4ODA3MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ZZ7VEyujJoLTYLvu-ujXSvGf4iFjMgxdsdamQmKIIZM'

# using version 3 api
movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"

# r = requests.get(endpoint)
# print(r.status_code)
# print(r.text)

# using API v4
movie_id = 501
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
headers = {
    'Authorization': f'Bearer {api_key_v4}',
    'Content-Type': 'application/json;charset=utf-8'
}
# r = requests.get(endpoint)
# print(r.status_code)
# print(r.text)

# searching for movies via api
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f'/search/movie'
search_query = 'The Matrix'
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
r = requests.get(endpoint)
if r.status_code in range(200,299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        movie_ids = set()
        for result in results:
            _id = result['id']
            # print(result['title'], _id)
            movie_ids.add(_id)
        # print(list(movie_ids))
output = 'movies.csv'
movie_data = []
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
        data = r.json()
        movie_data.append(data)

df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index=False)