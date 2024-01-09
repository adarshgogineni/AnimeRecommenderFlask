from flask import Flask, render_template, request, redirect, url_for, flash
import Anime_Recommendation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    anime_name = request.form['anime_name']
    recommendations = Anime_Recommendation.get_recommendations(anime_name)  # Call your ML model function
    print(recommendations)
    if isinstance(recommendations, str):
        return recommendations  # handle the error message
    else:
        return render_template('recommendations.html', recommendations=recommendations)

