import requests

api_key = "ad26761976d9d5350a28f9c8215cd871"
url = "https://api.themoviedb.org/3"
poster_url = "https://image.tmdb.org/t/p/w500/"

class MovieRecommender:
    def __init__(self,api_key):
        self.api_key = api_key
        self.url = url


    # search movie by name 
    def search_movie(self,movie_name):
        search_url = f"{url}/search/movie"
        response = requests.get(search_url, params={"api_key": api_key, "language": "en-US", "query": movie_name})
        response.raise_for_status()
        search_results = response.json()['results']
        
        if search_results:
            result = search_results[0]
            title = result['title']
            movie_id = result['id']
            return title, movie_id
        
        else :
            return None, None
        

    # to get movie details 
    def get_movie_details(self,movie_id):
        response = requests.get(f'{url}/movie/{movie_id}', params={"api_key": api_key, "language": "en-US"})
        response.raise_for_status()
        movie_details = response.json()
        return movie_details
    

    # movie recommendations
    def get_movie_recommendations(self,movie_id):
        recommendation_url = f"{url}/movie/{movie_id}/recommendations"
        response = requests.get(recommendation_url, params={"api_key": api_key, "language": "en-US"})
        response.raise_for_status()
        recommendations = response.json()['results']
        return recommendations
    
    # recommended by movie name 
    def get_recommendations_by_name(self, movie_name):
        title, movie_id = self.search_movie(movie_name)

        if title is None or movie_id is None:
            return []

        recommendations = self.get_movie_recommendations(movie_id)
        return recommendations


    # fetch the poster
    def fetch_poster(self, movie_id):
        response = requests.get(f"{self.url}/movie/{movie_id}?api_key={self.api_key}")
        data = response.json()
        if 'poster_path' in data:
            return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
        else:
            return "URL_to_a_default_image_or_placeholder"
    

recommender = MovieRecommender(api_key)
# recommender.get_recommendations_by_name(movie_name)