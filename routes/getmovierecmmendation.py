import pickle as pk
import os
from sklearn.metrics.pairwise import cosine_similarity
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tfidf_path = os.path.join(BASE_DIR, "tfidf_matrix.pkl")
indices_path = os.path.join(BASE_DIR, "indices.pkl")
df_path = os.path.join(BASE_DIR, "df.pkl")
tfidf_matrix=pk.load(open(tfidf_path,'rb'))
indices=pk.load(open(indices_path,'rb'))
df_new=pk.load(open(df_path,'rb'))

def recommendation(movie_title:str,k:int =10):
    if movie_title not in indices:
        return ['Movie not found']
    idx=indices[movie_title]
    sim_score=cosine_similarity(tfidf_matrix[idx],tfidf_matrix).flatten()
    similar_idx=sim_score.argsort()[::-1][1:k+1]
    return similar_idx


