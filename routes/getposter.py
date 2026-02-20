
import os
from pydantic import BaseModel,Field
from typing import List
import pickle as pk
from helper import fetch_poster
from langchain_community.tools import DuckDuckGoSearchRun
# Your TMDB API Key
    
from langchain_groq import ChatGroq
from langchain.agents import create_agent

from langchain_core.tools import tool

from dotenv import load_dotenv
import time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df_path = os.path.join(BASE_DIR, "df.pkl")
df_new=pk.load(open(df_path,'rb'))
import streamlit as st
class MoviePoster(BaseModel):
    movie_title: str =Field(...,description="Name of the movie")
    poster_url: str =Field(...,description="poster url")
    brief_overview: str =Field(...,description="overview of the movie")
load_dotenv()

search = DuckDuckGoSearchRun()


import os
@tool
def web_search(query:str):
    """Search the web for information about movie.

    Args:
        query: Search terms to look for
    
    """
    search.invoke(query)
  
def generate_overview(movie_name:str):
    llm=ChatGroq(model="openai/gpt-oss-20b")
 
#     messages = [
#     (
#         "system",
#         "You are AI expert of generate brief overview of the movie for movie recommendation system.Also reason why user should watch the movie",
#     ),
#     ("human", movie_name),
# ]
#     response=llm.invoke(messages)
    agent = create_agent(
        llm,
        tools=[web_search],

        system_prompt="You are AI expert of generate brief overview of the movie for movie recommendation system.Also reason why user should watch the movie"
    )

    response= agent.invoke(
        {"messages": [{"role": "user", "content": movie_name}]}
    
    )

    return response['messages'][-1].content



def get_movie_poster(similar_idx:list):
    
    posters: List[MoviePoster] = []

    for idx in similar_idx:
        movie_row = df_new.iloc[int(idx)]
        movie_name = movie_row["title"]
        
        movie_overview=generate_overview(movie_row["title"])
        poster_url = fetch_poster(movie_name)

        if poster_url:
            posters.append(
                MoviePoster(
                    movie_title=movie_name,
                    poster_url=poster_url,
                    brief_overview=movie_overview
                    
                )
            )
        time.sleep(2)

    return posters
