from pydantic import BaseModel,Field
import pickle as pk
from typing import List
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df_path = os.path.join(BASE_DIR, "df.pkl")
df_new=pk.load(open(df_path,'rb'))
class MovieInfo(BaseModel):
    title: str = Field(...,description="name of the movie")
    overview:str= Field(...,description="overview of the film")
    genres:str =Field(...,description='genre of the film')
    tagline:str=Field(...,description="tagline of the film")	
    vote_average:float=Field(...,description="vote average")	
    popularity:float=Field(...,description="popularity of the movie")	
    tags:str= Field(...,description="tags")

def details(similar_idx: int):
    movies: List[MovieInfo] = []

    for idx in similar_idx:
        movie_row = df_new.iloc[int(idx)].to_dict()
        movies.append(MovieInfo(**movie_row))

    return movies