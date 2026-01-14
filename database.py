from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["movie_recommender"]

# Function to save user details
def save_user(name, age, email):
    db.users.insert_one({"name": name, "age": age, "email": email})

# Function to save user ratings
def save_rating(name, selected_movie, recommended_movies, rating, feedback):
    db.ratings.insert_one({
        "name": name,
        "selected_movie": selected_movie,
        "recommended_movies": recommended_movies,
        "rating": rating,
        "feedback": feedback  # Store user feedback
    })


