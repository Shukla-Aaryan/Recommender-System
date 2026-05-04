# STREAMFLIX
# 🎬 Movie Recommender System

## 📌 Project Overview

This is one of my first projects.
The **Movie Recommender System** is an AI-based application designed to suggest movies to users based on their preferences and interests. This project demonstrates the practical application of **Machine Learning, Natural Language Processing (NLP), and data similarity techniques** to build a real-world recommendation engine.

The system primarily follows a **Content-Based Recommendation approach**, where movies are recommended by analyzing similarities between movie features such as genres, keywords, overview, cast, and crew.

This project is ideal for:

* AI/ML portfolios
* Academic submissions
* Understanding recommendation systems from scratch
* Demonstrating end-to-end ML project workflow

---

## 🎯 Objectives

* Build a personalized movie recommendation engine
* Apply NLP techniques on textual movie data
* Use similarity metrics to recommend relevant movies
* Create an interactive user interface
* Demonstrate deployment-ready ML architecture

---

## 🧠 Recommendation Approach

### Content-Based Filtering

The system recommends movies similar to a selected movie by:

1. Extracting important features from the dataset
2. Converting text data into numerical vectors using NLP
3. Calculating similarity scores between movies
4. Ranking movies based on similarity

This approach does **not** rely on user-user data, making it suitable even when user history is limited.

---

## 🛠️ Technologies Used

### Programming & Tools

* **Python**
* **Jupyter Notebook** (for experimentation)
* **Streamlit** (for web interface)

### Libraries

* `pandas` – data manipulation
* `numpy` – numerical operations
* `scikit-learn` – ML utilities and similarity measures
* `nltk` – text preprocessing
* `pickle` – model serialization

---

## 📊 Dataset Description

The dataset contains metadata about movies, including:

* Movie title
* Genres
* Overview
* Keywords
* Cast
* Crew

These features are combined into a single textual representation used for similarity computation.

---

## ⚙️ Feature Engineering & NLP Pipeline

1. Data cleaning and handling missing values
2. Text normalization (lowercasing, tokenization)
3. Stop-word removal
4. Stemming using Porter Stemmer
5. Feature concatenation
6. Vectorization using **CountVectorizer**
7. Similarity computation using **Cosine Similarity**

---

## 🧮 Similarity Measure

* **Cosine Similarity** is used to measure the closeness between two movies
* Produces a similarity score between 0 and 1
* Higher score indicates more similar movies

---

## 🖥️ User Interface

The project uses **Streamlit** to provide an interactive UI where:

* Users select a movie from a dropdown
* The system recommends top similar movies
* Results are displayed instantly

---

## 🚀 How to Run the Project

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

```cmd
git clone <repo>
cd movie-recommender-system
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```cmd
conda create --name myenv python=3.10
conda activate myenv
```

### 3️⃣ Install Dependencies

```cmd
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```cmd
streamlit run app.py
```

### 5️⃣ Open in Browser

Once the server starts, open:

```
http://localhost:8501
```

---

## 📈 Future Enhancements

* Add user authentication and profiles
* Store user ratings and feedback
* Hybrid recommender (Content + Collaborative)
* Use word embeddings (Word2Vec / BERT)
* Deploy using Docker or Cloud services

---

## 🧪 Learning Outcomes

* Hands-on experience with recommender systems
* Understanding NLP pipelines in ML projects
* Practical usage of cosine similarity
* Building and deploying ML-powered web apps

---

## 📜 Conclusion

This Movie Recommender System demonstrates how machine learning and NLP can be used to solve real-world problems. The project highlights a complete ML workflow—from data preprocessing to model deployment—making it a strong addition to any AI/ML portfolio.

---

## 👤 Author

**Aaryan Shukla**
MSc Artificial Intelligence
AI/ML Engineer

---
