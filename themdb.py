import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

# Your TMDB API Key
API_KEY = "YOUR_API_KEY_HERE"

def get_movie_poster(movie_name):
    # Search Movie API URL
    search_url = "https://api.themoviedb.org/3/search/movie"
    
    params = {
        "api_key": "15d2ea6d0dc1d476efbca3eba2b9bbfb",
        "query": movie_name
    }
    
    response = requests.get(search_url, params=params)
    data = response.json()
    
    if data["results"]:
        # Get first result
        poster_path = data["results"][0]["poster_path"]
        title = data["results"][0]["title"]
        
        if poster_path:
            # Construct full poster URL
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            
            print("Movie Found:", title)
            print("Poster URL:", poster_url)
            
            # Fetch poster image
            img_response = requests.get(poster_url)
            img = Image.open(BytesIO(img_response.content))
            
            # Display image
            plt.imshow(img)
            plt.axis("off")
            plt.title(title)
            plt.show()
        else:
            print("Poster not available.")
    else:
        print("Movie not found.")

# Example Usage
movie_name=input("name:")
get_movie_poster(movie_name)