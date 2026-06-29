"""
Minimal flask server classifying emotions contained in query string.
"""
from flask import Flask, request, Response
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")


@app.route("/emotionDetector")
def resp_emotion_detector():
    """
    Process passed URL query string.

    Returns:
        Response containing the classified emotions.
    """
    payload = request.args.get("textToAnalyze")
    status = 200
    output = ""

    if payload in ('', None):
        output = "Invalid text! Please try again!"
        status = 400
    else:
        scores = emotion_detector(str(payload))
        output = (
        "For the given statement, the system response is "
        f"'anger': {scores['anger']}, 'disgust': {scores['disgust']}, "
        f"'fear': {scores['fear']} , 'joy': {scores['joy']} and "
        f"'sadness': {scores['sadness']}. The dominant emotion is {scores['dominant_emotion']}."
        )

    return Response(output, status=status)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
