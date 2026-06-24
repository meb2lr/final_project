
import json
import requests


def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=payload, timeout=60)
    response.raise_for_status()  # raises an error for 4xx/5xx responses
    json_resp = response.json()

    pred0_emotions = json_resp["emotionPredictions"][0]["emotion"]

    dominant_emotion = max(pred0_emotions, key=pred0_emotions.get)
    pred0_emotions["dominant_emotion"] = dominant_emotion

    
    return pred0_emotions