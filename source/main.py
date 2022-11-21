from flask import Flask, redirect, url_for, render_template, request
import youtube
import visualizer

app = Flask(__name__)

#home page
@app.route("/", methods = ["POST", "GET"])
def home(): 
    if request.method == "POST":
        search_request = request.form["name"]
        try:
            yt = youtube.audio_finder(search_request)
            yt.get_audio()
            title = yt.youtubeObject.title
            return "Now Playing..." + title
        except:
            return "Download Failed. Make sure you inputted a YouTube link."
    else:
        return render_template("home.html")
    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)