
from flask import Blueprint, render_template, request, redirect, url_for
import urllib.request
import json
# from movie_library-master import Movie


views = Blueprint('views', __name__)

movie_list = []
playlists=[]
@views.route("/")
def home():
    return render_template("home.html", page_name="WHAT2WATCH")

@views.route("/search", methods=['GET'])
def search_results():
    movie_name = request.args.get("Moviequery")
    try:
        url = f"http://www.omdbapi.com/?s={movie_name}&apikey=205f2fa0"
        url = url.replace(" ", "%20")
        response = urllib.request.urlopen(url)
        data = response.read()
        json_data = json.loads(data)["Search"]
        print(json_data)
        return render_template("home.html", page_name="SEARCH RESULTS", movieList=json_data, query=movie_name)
    except Exception as e:
        print(e)
        return f"The movie with this name is not available by your {e}"

@views.route("/add_movie", methods=['POST'])
def add_movie():
    movie_title = request.form.get("movie_title")
    movie_poster = request.form.get("movie_poster")
    
    movie_imdbID = request.form.get("movie_imdbID")
    
    movie=movie
    if movie_title and not any(movie['title'] == movie_title for movie in movie_list):
        movie_list.append({'title': movie_title, 'poster': movie_poster, 'imdbID':movie_imdbID})
    return redirect(url_for('views.playlist'))

@views.route("/delete_movie", methods=['POST'])
def delete_movie():
    movie_title = request.form.get("movie_title")
    global movie_list
    movie_list = [movie for movie in movie_list if movie['title'] != movie_title]

    return redirect(url_for('views.playlist'))

@views.route("/playlist")
def playlist():
    return render_template("playlist.html", page_name="My Playlist", movie_list=movie_list)
