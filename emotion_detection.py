import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }  
    input_json = json.dumps(input_json)

    response = requests.post(url, headers = headers, data = input_json)
    return response.text

response = emotion_detector("I love this new technology")
print(response)