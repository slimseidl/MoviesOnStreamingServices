import requests 
import json
from Secrets import API_Key



title = input("Enter a movie title to search for:\n\n").replace(" ","%20")

response = requests.get(f'https://api.watchmode.com/v1/search/?apiKey={API_Key}&search_field=name&search_value={title}').json()

movie_id_list = []

for data in response["title_results"]:
    movie_id_list.append(data["id"])
    # print(data["id"], data["name"])

# print(movie_id_list)
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

viewings = []
for id in select_list:
    response = requests.get(f'https://api.watchmode.com/v1/title/{id}/sources/?apiKey={API_Key}').json()
    for item in response:
        if item["region"] == 'US' and item["type"] in ('free','sub'):
            service = item["name"]
            if item["type"] == "sub":
                type_ = "Subscription"
            else:
                type = "Free"
            # format = item["format"]
            # if item["type"] == "buy" or item["type"] == "rent": If decide to add rent or buy 
                # price = item["price"]
            # elif item["type"] == "sub":
            #     price = "Included in Subscription"
            # elif item["type"] == "free":
            #     price = "free"
            # else:
            #     price = "No price information"    
        else:
            continue
        viewings.append((service, type_))

viewings.sort(key=lambda x: x[0])

print(f'The selected Movie / Show is available on the following streaming services:\n')
for service, type_ in viewings:
    print(f'Service: {service} | Type: {type_}')








