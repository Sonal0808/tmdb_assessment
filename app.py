from flask import Flask, jsonify, request
import requests
import pandas as pd

app = Flask(__name__)

api_key = '4d04263a33beb5f8e4814792412fbb12'
base_url = 'https://api.themoviedb.org/3'

def fetch_all_data_from_tmdb(endpoint, params=None):
    all_data = []
    page = 1
    while True:
        params = params or {}
        params['api_key'] = api_key
        params['page'] = page
        response = requests.get(f'{base_url}/{endpoint}', params=params).json()
        if 'results' in response:
            all_data.extend(response['results'])
            if len(response['results']) < 20:
                break
            page += 1
        else:
            break
    return all_data

@app.route('/popular-movies')
def popular_movies():
    # Fetch movie data
    movies = fetch_all_data_from_tmdb('movie/popular')
    movie_data = [{'name': movie['title'], 'vote_count': movie['vote_count']} for movie in movies]

    # Sort the movie data by vote count in descending order
    movie_data.sort(key=lambda x: x['vote_count'], reverse=True)

    # Create a better visual format for the output
    formatted_movies = ""
    for movie in movie_data:
        formatted_movies += f"<strong>{movie['name']}</strong><br>"
        formatted_movies += f"Votes: {movie['vote_count']}<br><hr>"

    # Return the formatted movies as an HTML response
    return f"<h1>Popular Movies</h1><div>{formatted_movies}</div>"

def get_popular_actors(api_key, pages=5):
    actors = []
    for page in range(1, pages + 1):
        url = f"{base_url}/person/popular"
        params = {'api_key': api_key, 'page': page}
        response = requests.get(url, params=params).json()
        actors.extend(response.get('results', []))
    return actors

def get_movie_count_for_actor(actor_id):
    url = f"{base_url}/person/{actor_id}/movie_credits"
    params = {'api_key': api_key}
    response = requests.get(url, params=params).json()
    return len(response.get('cast', []))


@app.route('/top-actors')
def top_actors():
    # Fetch actor data
    actors = get_popular_actors(api_key)
    actor_data = []

    # Get the number of actors per page dynamically (default is 20 if not provided)
    actors_per_page = request.args.get('actors_per_page', default=20, type=int)  # Use query parameter or default to 20
    total_actors = len(actors)
    total_pages = (total_actors // actors_per_page) + (1 if total_actors % actors_per_page > 0 else 0)

    # Print to the console
    print(f"Total actors: {total_actors}")
    print(f"Displaying actors in {total_pages} pages, {actors_per_page} actors per page.")

    # Pagination: Show actors for each page
    for page in range(1, total_pages + 1):
        start_index = (page - 1) * actors_per_page
        end_index = start_index + actors_per_page
        actors_for_page = actors[start_index:end_index]

        # Print how many actors are being shown on this page
        print(f"Page {page}: Showing {len(actors_for_page)} actors.")

        # Collect actor data and their movie counts
        for actor in actors_for_page:
            try:
                count = get_movie_count_for_actor(actor['id'])
                actor_data.append({'name': actor['name'], 'movie_count': count})
            except:
                continue

    # Sort actors by movie count in descending order
    actor_data.sort(key=lambda x: x['movie_count'], reverse=True)

    # Create a better visual format using Flexbox
    formatted_actors = "<div style='display: flex; flex-direction: column;'>"

    for actor in actor_data:
        formatted_actors += f"<div style='display: flex; justify-content: space-between; padding: 5px; border-bottom: 1px solid #ddd;'>"
        formatted_actors += f"<span>{actor['name']}</span>"
        formatted_actors += f"<span>Movies: {actor['movie_count']}</span>"
        formatted_actors += "</div>"

    formatted_actors += "</div>"

    # Return the formatted actors without page info
    return f"<h1>Top Actors</h1><div>{formatted_actors}</div>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
