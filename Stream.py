import requests 
import json
from Secrets import API_Key

class Stream():
    def __init__(self,title=None):
        self.title = title 

    # Retrieve list of matching movie ID's
    def get_matches(self):
        response = requests.get(f'https://api.watchmode.com/v1/search/?apiKey={API_Key}&search_field=name&search_value={self.title}').json()

        movie_id_list = []
        for data in response["title_results"]:
            movie_id_list.append(data["id"])

        return movie_id_list
    
    # Retrieve matching movie information
    def get_movie_info(self):
        select_list = []
        for movie_id in self.get_matches():
            response = requests.get(f'https://api.watchmode.com/v1/title/{movie_id}/details/?apiKey={API_Key}').json()
            if response["genre_names"]:
                primary_genre = response["genre_names"][0]
            else:
                continue
            if response["us_rating"]:
                rated = response["us_rating"]
            else:
                continue
            show_type = response["type"].replace("_"," ").title()
            movie_key = response["id"]
            movie_name = response["title"]
            runtime = response["runtime_minutes"]
            plot = response["plot_overview"]
            release_year = response["year"]
            select_list.append((movie_key,movie_name,runtime,plot,release_year,primary_genre,rated,show_type))
        return select_list

    # Retrieve streaming services for matching movie ID's
    def get_streaming_services(self):
        viewings = []
        for movie_tuple in self.get_movie_info():
            response = requests.get(f'https://api.watchmode.com/v1/title/{movie_tuple[0]}/sources/?apiKey={API_Key}').json()
            for item in response:
                if item["region"] == 'US' and item["type"] in ('free','sub'):
                    service = item["name"]
                    if item["type"] == "sub":
                        type_ = "Subscription"
                    else:
                        type_ = "Free"
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
                viewings.append((movie_tuple[0],service, type_))

        viewings.sort(key=lambda x: x[0])
        return viewings

    def print_info(self):
        print(f'The Movie / Show entered returned the following matches:\n')
        
        movies = self.get_movie_info()
        services = self.get_streaming_services()

        match_list = []
        match_counter = 0
        for movie in movies:
            primary_id = movie[0]
            name = movie[1]
            runtime = movie[2]
            plot = movie[3]
            release_year = movie[4]
            genre = movie[5]
            rating = movie[6]
            show_type = movie[7]
            match_counter+=1
            match_list.append((match_counter,primary_id))

            print(f'Title: {name} | Rating: {rating} | Genre: {genre} | Type: {show_type} | Runtime: {runtime} | Release Year: {release_year} | Match No. {match_counter}'
                    f'\n\nPlot: {plot}\n')
            
            movie_services = [(svc[1], svc[2]) for svc in services if svc[0] == primary_id] # consolidated loop into single line

            # for svc in services:
            #     if svc[0] == primary_id:
            #         movie_services = (svc[1], svc[2]) 
            
            # for service in self.get_streaming_services():
            #     if service[0] == primary_id:
            #         svc = service[1]
            #         type_ = service[2]
            #         print(f'Streaming Services:\n\t-{svc} | Plan Type: {type_}\n')

            if movie_services:
                print('Streaming Services:')
                for service, type_ in movie_services:
                    print(f' - {service} ({type_})')
            else:
                print('No streaming services available.')

            print(f'\n' + "-"*80 + "\n")

    #     choice = int(input("Enter the match number of the movie or show you'd like more information for:"))

    #     movie_id = None 
    #     for match_no, primary_id in match_list:
    #         if match_no == choice:
    #             movie_id = primary_id
    #             break

    #     print(f'Now fetching cast and crew information for {name} {show_type} {release_year}')

    #     cast_crew = self.get_cast_crew(movie_id)

    #     if "cast" in cast_crew:
    #         print("Cast:")
    #         for member in cast_crew["cast"][:5]:
    #             print(f' - {member["name"]} as {member.get("character_name", "N/A")}')

    #     if "crew" in cast_crew:
    #         print("\nCrew:")
    #         for member in cast_crew["crew"][:5]:
    #             print(f' - {member["name"]} ({member.get("job", "N/A")})')

    
    # def get_cast_crew(self,title_id):
    #     response = requests.get(f'https://api.watchmode.com/v1/title/{title_id}/cast-crew/?apiKey={API_Key}').json()
    #     return response



            






