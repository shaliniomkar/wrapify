import main
from flask import Flask, render_template, jsonify, redirect, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'journal'

@app.route("/")
def stats():
    if main.user_name is None:
        auth_url = main.sp_oauth.get_authorize_url()
        return redirect(auth_url)
    
    return render_template(
                "stats.html", 
                user_name=main.user_name, 
                top_tracks_dict=main.top_tracks_dict, 
                top_artists_list=main.top_artists_list, 
                album_images_dict=main.album_images_dict,
                artist_images_dict=main.artist_images_dict,
                loyalty_index=main.loyalty_index_value,
                loyalty_index_statement=main.loyalty_index_statement,
                music_age=main.music_age_value,
                music_age_statement=main.music_age_statement
            )

@app.route("/create_playlist", methods=["POST"])
def create_playlist():
    try:
        playlist_id = main.create_top_10_playlist(main.name, main.description)
        main.add_tracks_to_playlist(playlist_id, main.top_tracks_uris)
        return jsonify({"status": "success", "message": "Playlist created successfully!"})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if code:
        main.sp_oauth.get_access_token(code)
        main.fetch_user_data()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)