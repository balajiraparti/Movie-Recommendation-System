import streamlit as st
from routes.getposter import get_movie_poster
from routes.getmovierecmmendation import recommendation
from routes.getposter import get_movie_poster

if 'movie_name' not in st.session_state:
    st.session_state['movie_name'] = ''

if 'similar_idx' not in st.session_state:
    st.session_state['similar_idx'] = ''

if 'poster_details' not in st.session_state:
    st.session_state['poster_details'] = ''
    
@st.dialog("overview dialog")
def overview(movie):
    st.subheader(movie.movie_title)
    st.write(movie.brief_overview)
    
   
   
st.session_state.movie_name=st.text_input("Enter movie name:")
if st.button('recommend'):
    if st.session_state.movie_name:
        st.session_state.similar_idx=recommendation(st.session_state.movie_name)
        st.session_state.poster_details=get_movie_poster(st.session_state.similar_idx)
        
if st.session_state.poster_details:
        num_cols = 5  # posters per row
        posters=st.session_state.poster_details
        for i in range(0, len(posters), num_cols):

            cols = st.columns(num_cols)

            for col, movie in zip(cols, posters[i:i+num_cols]):

                with col:
                    st.image(movie.poster_url, width='stretch')
                    if st.button(
                        movie.movie_title,
                        key=f"btn_{movie.movie_title}_{i}"
                    ):
                        overview(movie)
                    

