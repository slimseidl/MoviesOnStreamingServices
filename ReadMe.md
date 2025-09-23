🎬 MoviesOnStreamingServices

A Python project that lets you search for a movie or TV show by title and see:

    - Basic details (title, rating, runtime, plot, release year, genre, type)

    - All US streaming services where it’s available (subscription or free)

    - Select movie from matches and see rent / buy availability

This project uses the Watchmode API to fetch movie/show metadata and streaming service availability.

🚀 Features

Search by title and get multiple matches (movie, TV series, remakes, etc.)

View detailed metadata:

Title

Rating (MPAA/TV rating)

Runtime

Plot overview

Release year

Genre

Type (Movie or TV Series)

See a grouped list of all streaming services where each match is available

Currently supports US region, free and subscription services

🛠 Requirements

    Python 3.8+

    Requests

    Install dependencies:

        pip install requests


You also need a free API key from Watchmode.

📂 Project Structure
MoviesOnStreamingServices

instance.py                 # Example script: create an instance and search

Stream.py                   # Main class with methods:
- get_matches()             # Gets candidate matches by title
- get_movie_info()          # Gets details (title, rating, runtime, plot, etc.)
- get_streaming_services()  # Gets streaming providers for each match
- print_info()              # Prints formatted results
- README.md                 # Project documentation

▶️ Usage

Export your API key as a variable in movies.py (or in an .env file if you extend it):

API_Key = "your_api_key_here"
    I added mine to a separate file, then imported it so I could exclude it with gitignore


Run the script:

python instance.py


Enter a movie/show title when prompted. Example:

Enter a movie to find:
Friday Night Lights


Output:

The Movie / Show entered returned the following matches:

Title: Friday Night Lights | Rating: PG-13 | Genre: Drama | Type: movie | Runtime: 118 | Release Year: 2004

Plot: A small, turbulent town in Texas obsesses over their high school football team...

Streaming Services:
  - Netflix (Subscription)
  - Peacock (Subscription)

--------------------------------------------------------------------------------

Title: Friday Night Lights | Rating: TV-14 | Genre: Drama | Type: tv_series | Runtime: 43 | Release Year: 2006

Plot: The trials and triumphs of life in the small town of Dillon, Texas, where high school football is everything.

Streaming Services:
  - Prime Video (Subscription)

📌 Notes

Currently filters US region only and only returns Free or Subscription services.

Long plot descriptions are printed in full — you may want to truncate if displaying in a UI.

📈 Future Improvements

Command-line arguments for faster searches

Export results to JSON/CSV

Build a simple web interface (e.g., with Flask or Streamlit)