# What2Watch

What2Watch is a Flask web application that allows users to search for movies using the OMDb API and add them to their playlists after logging in. Users can sign up for accounts, log in, and maintain their playlists.

## For deployed link refer: [Deployed_Link](https://movie-search-web-app-kx5q.onrender.com/))
## Features
- User Authentication: Users can sign up for accounts, log in, and log out securely.
- Search Movies: Users can search for movies using the OMDb API.
- Add to Playlist: Authenticated users can add movies to their playlists.
- Delete from Playlist: Authenticated users can remove movies from their playlists.
- View Playlist: Users can view their playlists.
  
## Prerequisites
Before running the application, ensure you have the following installed:

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Login

# Installation
1. Clone the repository
    git clone https://github.com/yourusername/what2watch.git
    cd what2watch

2. Create a virtual environment:
    python3 -m venv venv

3. Activate the virtual environment:
    venv\Scripts\activate

4. Install the dependencies:
    pip install -r requirements.txt

5. Set up the database:
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade

6. Run the application:
    python main.py

7. Open your web browser and navigate to http://localhost:5000.

# Usage
1. Sign up for an account or log in if you already have one.
2. Search for movies using the search bar on the home page.
3. Click on a movie to view details.
4. Click the "Add to Playlist" button to add a movie to your playlist.
5. View your playlist by clicking on the "My Playlist" link in the navigation bar.
6. To remove a movie from your playlist, click the "Delete" button next to it.

# Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

# Acknowledgments
Thanks to the Fasal Recruiting Team


