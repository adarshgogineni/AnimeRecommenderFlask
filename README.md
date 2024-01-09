# Anime Recommendation System
An Anime Recommender using a Machine Learning Model called Cosine Similarity deployed with Python and Flask

## Table of Contents
- [Overview](#overview)
- [Machine Learning Model](#machine-learning-model)
- [Benefits](#benefits)
- [Deployment](#deployment)
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

## Deployment

The Anime Recommendation System is deployed on Heroku and can be accessed online at [Link to Deployed App](https://anime-recommender-herokuapp.com/). Simply visit the link to start receiving personalized anime recommendations.

## Local Setup

To run the Anime Recommendation System locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/anime-recommendation.git
