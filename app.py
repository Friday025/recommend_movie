import streamlit as st
from movies import MovieRecommender

# Instantiate MovieRecommender class with the api_key
api_key = "ad26761976d9d5350a28f9c8215cd871"
movie_recommender = MovieRecommender(api_key)

# Streamlit app title
st.title("Movie Recommendations System")

# Text input field for movie name
movie_name = st.text_input("Enter a movie name for recommendations")

# Convert input to title case
movie_name = movie_name.title()

# Check if movie name is provided
if movie_name:
    # Get movie recommendations based on the input movie name
    recommendations = movie_recommender.get_recommendations_by_name(movie_name)

    # Display recommendations or error message
    if not recommendations:
        st.error(f"No Movie found try a again!")

    else:
        st.header("Recommendations:")
        
        # Define the number of columns
        num_columns = 5
        
        # Split the recommendations into chunks to display in columns
        chunks = [recommendations[i:i+num_columns] for i in range(0, len(recommendations), num_columns)]
        
        # Iterate over each chunk and display in columns
        for chunk in chunks:
            # Start a new row
            cols = st.columns(num_columns)
            
            # Iterate over each recommendation in the chunk and display title and poster
            for recommendation, col in zip(chunk, cols):
                col.write(recommendation['title'])
                poster_url = movie_recommender.fetch_poster(recommendation['id'])
                col.image(poster_url, caption=recommendation['title'], use_column_width=True)

    