import requests 
import json
from Secrets import API_Key



title = input("Enter a movie title to search for:\n\n").replace(" ","%20")

response = requests.get(f'https://api.watchmode.com/v1/search/?apiKey={API_Key}&search_field=name&search_value={title}').json()

movie_id_list = []

for data in response["title_results"]:
    movie_id_list.append(data["id"])
    # print(data["id"], data["name"])

print(movie_id_list)
select_list = []
for movie_id in movie_id_list:
    response = requests.get(f'https://api.watchmode.com/v1/title/{movie_id}/details/?apiKey={API_Key}').json()
    if response["genre_names"]:
        primary_genre = response["genre_names"][0]
    else:
        continue
    if response["us_rating"]:
        rated = response["us_rating"]
    else:
        continue
    movie_key = response["id"]
    movie_name = response["title"]
    runtime = response["runtime_minutes"]
    plot = response["plot_overview"]
    release_year = response["year"]
    select_list.append(movie_key)


    # print(f'\nTitle: {movie_name} | Rating: {rated} | Release Year: {release_year} | Runtime: {runtime} Minutes | Genre: {primary_genre} | Movie ID: {movie_id}\n'
    #       f'Plot: {plot}\n')
    
print(select_list)

for id in select_list:
    response = requests.get(f'https://api.watchmode.com/v1/title/{id}/sources/?apiKey={API_Key}').json()
    for item in response:
        if item["region"] == 'US':
            service = item["name"]
            type = item["type"]
            if item["type"] == "buy" or item["type"] == "rent":
                price = item["price"]
            elif item["type"] == "sub":
                price = "Included in Subscription"
            elif item["type"] == "free":
                price = "free"
            else:
                price = "No price information"    
        else:
            continue

        print(f'Service: {service} | Type: {type} | Price: {price}')








