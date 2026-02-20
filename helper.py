import os
from dotenv import load_dotenv
import requests
import time
load_dotenv()
def fetch_poster(movie_name: str) -> str | None:
    search_url = "https://api.themoviedb.org/3/search/movie"

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
   

    params = {
        "api_key":os.getenv("API_KEY"),
        "query": movie_name
    }

    try:
        response = requests.get(search_url, params=params, timeout=3,headers=headers)
        response.raise_for_status()

        data = response.json()

        if data.get("results"):
            poster_path = data["results"][0].get("poster_path")
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"

    except requests.exceptions.RequestException as e:
        print("TMDB request failed:", e)
        return None

    return None