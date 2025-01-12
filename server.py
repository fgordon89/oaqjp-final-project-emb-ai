"""Notes"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    """Pass the text to the emotion_detector function and store the response
       Extract the emotions from the response"""
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detector(text_to_analyze)
    if dominant_emotion is None:
        return "Invalid text! Please try again."

    return f"The given text has been indentifed as {dominant_emotion}"
        # Return a formatted string with the dominant emotion

@app.route("/")
def render_index_page():
    """Notes"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
