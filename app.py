from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
from joblib import dump, load

mlb = load('mlb.joblib')
scaler = load('scaler.joblib')
cosine_sim = load('cosine_sim.joblib')

anime_data = pd.read_csv('anime.csv')


def get_recommendations(anime_name, cosine_sim=cosine_sim):
    # Convert input anime name to lowercase
    anime_name_lower = anime_name.lower()

    # Check if the anime name exists in the dataset (case-insensitive)
    if anime_name_lower not in map(str.lower, anime_data['name'].values):
        return None

    # Get the index of the anime that matches the name (case-insensitive)
    idx = next((index for index, name in enumerate(anime_data['name'].values) if name.lower() == anime_name_lower), None)
    if idx is None:
        return None

    # Get the pairwise similarity scores of all anime with that anime
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the anime based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Filter out closely related anime (like sequels or related movies, case-insensitive)
    filtered_scores = [item for item in sim_scores if not anime_data['name'][item[0]].lower().startswith(anime_name_lower)]

    # Get the scores of the 10 most similar anime (excluding closely related ones)
    filtered_scores = filtered_scores[1:16]

    # Get the anime indices
    anime_indices = [i[0] for i in filtered_scores]

    # Return the top 10 most similar anime
    return anime_data['name'].iloc[anime_indices]


app = Flask(__name__)
app.secret_key = 'doryuuheki'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    anime_name = request.form['anime_name']
    recommendations = get_recommendations(anime_name)  # Call your ML model function

    if recommendations is None or len(recommendations) == 0:
        flash('Anime not found. Please check the name and try again.')
        return redirect(url_for('index'))  

    return render_template('recommendations.html', recommendations=recommendations)
