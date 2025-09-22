import requests 
import json
from Secrets import API_Key



title = input("Enter a movie title to search for:\n").replace(" ","%20")

response = requests.get(f'https://api.watchmode.com/v1/search/?apiKey={API_Key}&search_field=name&search_value={title}').json()

movie_id_list = []

for data in response["title_results"]:
    movie_id_list.append(data["id"])
    # print(data["id"], data["name"])

# print(movie_id_list)

for movie_id in movie_id_list:
    response = requests.get(f'https://api.watchmode.com/v1/title/{movie_id}/details/?apiKey={API_Key}').json()
    movie_name = response["title"]
    runtime = response["runtime_minutes"]
    plot = response["plot_overview"]
    print(plot)
    





