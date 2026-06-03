
# Wrapify

A Flask-based web application that gives users a personalized, mid-year look at their listening habits over the last 6 months. Built with Python, Flask, Bootstrap, and the Spotify Web API.




## Features

- Spotify Auth: Secure user login via Spotify OAuth.
- Responsive Design: Clean UI built with Bootstrap.
- Custom Playlist Creator: Instantly generate and save a Spotify playlist of your top tracks directly to your account.
- Listening Age: Discover the statistical "age" of your music taste based on the release years of your favorite tracks.
- Loyalty Score: Find out how dedicated you are to your top artists compared to mainstream listeners.
- Top Tracks & Artists: View your most-played songs and favorite musicians from the past 6 months.


## Tech Stack

**Backend:** Python 3.14.5, Flask, 

**Frontend:** Bootstrap 5, HTML5, CSS3, JavaScript
 (Async Fetch API / AJAX)
 
**API / Libraries:** Spotify Web API (`spotipy`), `python-dotenv`




## Prerequisites

Before running this project, make sure you have: 

- Python 3.8 or higher installed
- A Spotify Premium account
- A Spotify Developer account to get API keys.
## Installation

First, clone my repository.

```bash
git clone https://github.com/shaliniomkar/wrapify
cd wrapify
```

Then, set up a virtual environment.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Next, install dependencies.

```bash
pip install -r requirements.txt
```

We will need to configure the Spotify API credentials. Start by going to the Spotify Developer Dashboard and logging in with your Spotify account. Then, create an app, fill in the details, and access your client ID and secret. In the app settings, set the redirect URI to http://127.0.0.1:5000/callback.

Create a file named .env in your project's root directory and add the following:

```bash
SPOTIFY_API_KEY="YOUR-CLIENT-ID"
SPOTIFY_CLIENT_SECRET="YOUR-CLIENT-SECRET"
```

Then, run the application.

```bash
flask run
```

Open http://127.0.0.1:5000 in your web browser to log in and see your wrapped data.


## License

Distributed under the MIT License. See `LICENSE` for more information.
