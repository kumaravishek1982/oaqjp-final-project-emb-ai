from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Retrives the emotion expressed in a sentence

    returns:
    emotions attached to the sentence including dominant emotion 
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    emotion = emotion_detector(text_to_analyze)

    if emotion.get("dominant_emotion") == "None":
        return "Invalid text! Please try again."
    else:
        return emotion
@app.route("/")
def render_index_page():
    """
    Interface for the application presented in standard HTML

    Parameters:
    None
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
