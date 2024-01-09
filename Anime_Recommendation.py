import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# read data
anime_data = pd.read_csv('anime.csv')
# Impute missing values in 'genre' and 'type' with the mode (most frequent value)
anime_data['genre'].fillna(anime_data['genre'].mode()[0], inplace=True)
anime_data['type'].fillna(anime_data['type'].mode()[0], inplace=True)

# Impute missing values in 'rating' with the median
anime_data['rating'].fillna(anime_data['rating'].median(), inplace=True)
# Replace NaN and non-string values with a placeholder or an empty string
anime_data['genre'] = anime_data['genre'].fillna('Unknown').astype(str)

# Convert 'Unknown' to NaN
anime_data['episodes'] = pd.to_numeric(anime_data['episodes'], errors='coerce')

# Replace NaN with median or mean
anime_data['episodes'].fillna(anime_data['episodes'].median(), inplace=True)

#Feature engineering
scaler = StandardScaler()
#'genre' is a string of genres separated by commas
anime_data['genre'] = anime_data['genre'].apply(lambda x: x.split(','))

mlb = MultiLabelBinarizer()
genres = mlb.fit_transform(anime_data['genre'])

# Create a DataFrame with the transformed genres and concatenate with the original DataFrame
genres_df = pd.DataFrame(genres, columns=mlb.classes_)
anime_data = pd.concat([anime_data, genres_df], axis=1)

#type is categorical variable - convert to binary
type_dummies = pd.get_dummies(anime_data['type'])
anime_data = pd.concat([anime_data, type_dummies], axis=1)

#Normalize Rating
anime_data['rating_scaled'] = scaler.fit_transform(anime_data[['rating']])

#Normalize episodes
anime_data['episodes_scaled'] = scaler.fit_transform(anime_data[['episodes']])

#Feature matrix
# Combine all relevant features into one matrix
feature_matrix = pd.concat([genres_df, type_dummies, anime_data[['episodes_scaled', 'rating_scaled']]], axis=1)
# Calculate cosine similarity
cosine_sim = cosine_similarity(feature_matrix, feature_matrix)
#Function to get similar anime
def get_recommendations(anime_name, cosine_sim=cosine_sim):
    # Check if the anime name exists in the dataset
    if anime_name not in anime_data['name'].values:
        return "Anime not found. Please check the name and try again."

    # Get the index of the anime that matches the name
    idx = anime_data[anime_data['name'] == anime_name].index[0]

    # Get the pairwise similarity scores of all anime with that anime
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the anime based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Filter out closely related anime (like sequels or related movies)
    filtered_scores = [item for item in sim_scores if not anime_data['name'][item[0]].startswith(anime_name)]

    # Get the scores of the 10 most similar anime (excluding closely related ones)
    filtered_scores = filtered_scores[1:16]

    # Get the anime indices
    anime_indices = [i[0] for i in filtered_scores]

    # Return the top 10 most similar anime
    return anime_data['name'].iloc[anime_indices]


print(get_recommendations('Naruto'))