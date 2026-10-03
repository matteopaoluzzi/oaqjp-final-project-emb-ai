from flask import Flask, render_template, request
from EmotionDetection import emotion_detector
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    pre = "For the given statement, the system response is "
    emotions = ""
    for emotion, value in response.items():
        emotions += f"'{emotion}': {value}"
        if emotion == "sadness":
            emotions += ". "
            break
        elif emotion == "joy":
            emotions += " and "
        else:
            emotions += ", "
    post = f"The dominant emotion is <strong>{response['dominant_emotion']}</strong>"
        
    return pre+emotions+post


@app.route("/")
def render_index_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)