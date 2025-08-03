from flask import Flask, render_template, request
from EmotionDetection import emotion_detector
app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    
    return render_template("index.html")

@app.route("/emotionDetector", methods = ["GET"])
def emotionDetection():
    text = request.args.get("textToAnalyze")
    print(text)
    output = emotion_detector(text)
    output_text = f"For the given statement, the system response is 'anger': {output['anger']}, 'disgust': {output['disgust']}, 'fear': {output['fear']}, 'joy': {output['joy']} and 'sadness': {output['sadness']}. The dominant emotion is {output['dominant_emotion']}."
    return output_text