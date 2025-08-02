import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }  
    input_json = json.dumps(input_json)

    response = requests.post(url, headers = headers, data = input_json)

    emotion_input = json.loads(response.text)["emotionPredictions"][0]["emotion"]
    anger_score = emotion_input["anger"]
    disgust_score = emotion_input["disgust"]
    fear_score = emotion_input["fear"]
    joy_score = emotion_input["joy"]
    sadness_score = emotion_input["sadness"]
    

    emotion_output = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    }

    dominant_emotion = max(emotion_output, key = emotion_output.get)
    emotion_output["dominant_emotion"] = dominant_emotion


    return emotion_output

response = emotion_detector("I love this new technology")
print(response)