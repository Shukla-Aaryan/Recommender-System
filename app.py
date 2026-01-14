import pickle
import streamlit as st
import requests
import base64
from database import save_user, save_rating

def add_bg(image_file):
    with open(image_file, "rb") as img:
        encoded_string = base64.b64encode(img.read()).decode()
    bg_css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)

add_bg("Background (1).jpg") 

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f47f3795f4e9717df0acf00fa6c329e6"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching poster: Poor Connection")
        return None

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        poster_url = fetch_poster(movie_id)
        if poster_url:
            recommended_movie_posters.append(poster_url)
            recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

st.title('🎬 STREAMFLIX')

st.markdown("""
    <h3 style='text-align: center; color: white;'>Sign Up or Log In</h3>
    <p style='text-align: center; color: lightgray;'>Enter your details to personalize your movie recommendations.</p>
""", unsafe_allow_html=True)

if 'user_details_submitted' not in st.session_state:
    st.session_state.user_details_submitted = False

if not st.session_state.user_details_submitted:
    st.markdown("""
        <style>
            .form-container {
                background-color: rgba(255, 255, 255, 0.1);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.2);
                width: 50%;
                margin: auto;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.form("user_details_form"):
        st.markdown("<div class='form-container'>", unsafe_allow_html=True)
        name = st.text_input("Enter your name")
        age = st.number_input("Enter your age", min_value=10, max_value=100)
        email = st.text_input("Enter your email")
        submit_details = st.form_submit_button("Submit", help="Click to register", args=["success"])
        st.markdown("</div>", unsafe_allow_html=True)
    
    if submit_details and name and email:
        st.session_state.user_details_submitted = True
        st.session_state.name = name
        save_user(name, age, email)
        st.success(f"Welcome, {name}! Let's find some great movies for you.")
        st.rerun()
else:
    st.success(f"Welcome, {st.session_state.name}! Let's find some great movies for you.")

movies = pickle.load(open('artificats/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artificats/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

recommended_movie_names, recommended_movie_posters = [], []
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    if recommended_movie_names and recommended_movie_posters:
        cols = st.columns(5)
        for i, col in enumerate(cols):
            if i < len(recommended_movie_names):
                col.text(recommended_movie_names[i])
                col.image(recommended_movie_posters[i])
    else:
        st.error("No recommendations found.")

st.markdown("---")

rating = st.slider("How satisfied are you with the recommendations?", 1, 5, 3)
feedback = st.text_area("Leave additional feedback:")
if st.button("Submit Rating"):
    if st.session_state.user_details_submitted:
        save_rating(st.session_state.name, selected_movie, recommended_movie_names, rating,feedback)
        st.success("Your rating has been saved. Thank you!")
    else:
        st.warning("Please enter your details first.")

