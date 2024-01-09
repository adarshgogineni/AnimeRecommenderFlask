# Anime Recommendation System
An Anime Recommender using a Machine Learning Model - Cosine Similarity. 

##Technologies used: Python and Flask, Javascript, HTML, CSS
[![Python](URL_for_Python_logo "Python")](https://www.python.org/)
[![Flask](URL_for_Flask_logo "Flask")](https://flask.palletsprojects.com/)


## Table of Contents
- [Overview](#overview)
- [Machine Learning Model](#machine-learning-model)
- [Benefits](#benefits)
- [Local Setup](#local-setup)
- [Usage](#usage)

## Overview

This project is an Anime Recommendation System that utilizes machine learning to provide anime recommendations to users. Whether you're an anime enthusiast or new to the world of anime, the system aims to help you discover anime titles that align with your preferences. Simply type an anime that you like into the search bar, and find other similar animes like it.
 
## Machine Learning Model

The recommendation system is powered by a Cosine Similarity-based machine learning model. Cosine Similarity is a technique used to measure the similarity between items based on their feature vectors. In the context of the anime recommendation system, it calculates the similarity between different anime titles by comparing their feature vectors.

### Why Cosine Similarity?

- **Efficiency**: Cosine Similarity is computationally efficient, making it suitable for providing real-time recommendations.

- **Ease of Interpretation**: This technique is easy to understand and interpret, making it valuable for explaining recommendations to users.

- **Effective for High-Dimensional Data**: Cosine Similarity works well for high-dimensional data, which is common in recommendation systems with many features.

The model computes the cosine similarity scores between anime titles based on their genre, type, episodes, and rating. These scores are used to recommend anime titles that are most similar to the user's preferences.

The `get_recommendations` function in the code calculates and returns a list of anime titles that are most similar to the input anime, allowing users to discover new anime based on their interests.


- **Scalability**: It works well for a large number of users and items, making it suitable for anime recommendation systems.

- **Ease of Interpretation**: This technique is easy to understand and interpret, making it valuable for explaining recommendations to users.

## Benefits

- **Personalized Recommendations**: Discover anime titles tailored to your unique preferences.

- **Diverse Anime Selection**: Explore a wide range of anime genres and styles, ensuring you find anime that suits your taste.

- **User-Friendly Interface**: The application provides an intuitive and user-friendly interface for an enjoyable experience.


## Local Setup

To run the Anime Recommendation System locally, follow these steps:

1. Clone the repository:
   ```sh
   https://github.com/adarshgogineni/AnimeRecommenderFlask.git
   ```
2. Navigate to the project directory 
   ```sh
   cd AnimeRecommenderFlask
   ```
3. Create a virtual environment (optional but recommended)
   ```sh
   python -m venv venv
   ```
4. Activate the Virtual Environment
   
   Windows:
   ```sh
   venv\Scripts\activate
   ```
   Mac:
   ```sh
   source venv/bin/activate
   ```
6. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
7. Run the Application:
   ```sh
   flask run
   ```
8. View application on local host:
   ```sh
   http://127.0.0.1:5000/
   ```

## Usage:
<img width="1624" alt="Screenshot 2024-01-09 at 9 54 33 AM" src="https://github.com/adarshgogineni/AnimeRecommenderFlask/assets/32943978/8327efc4-4d5e-4e91-9f8d-23c4b8924f0b">

Type in the name of an anime you like:
<img width="1624" alt="Screenshot 2024-01-09 at 9 55 48 AM" src="https://github.com/adarshgogineni/AnimeRecommenderFlask/assets/32943978/105fdfec-36c0-455a-9470-f8a744a88874">

Get results similar to the anime:
<img width="1624" alt="Screenshot 2024-01-09 at 9 56 12 AM" src="https://github.com/adarshgogineni/AnimeRecommenderFlask/assets/32943978/c3e8b088-9708-4f94-b982-0c370f0cc86c">

