import requests
import json

def emotion_detector(text_to_analyse):
    
    # URL for the emotion detector API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    data = {"raw_document": {"text": text_to_analyse}} # Payload with text to be analyzed
    response = requests.post(url, json=data, headers=header) # POST request to the API with the payload and headers
    status_code = response.status_code

    # If the response status code is 400, set  dominant emotion to None    
    if response.status_code == 400: 
        formatted_response = { 'anger': None,
                             'disgust': None,
                             'fear': None,
                             'joy': None,
                             'sadness': None,
                             'dominant_emotion': None}
    else:
    # If the response status code is 200, extract the dominant emotion from the response
        emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_predictions.items(), key=lambda x: x[1])
    
    return dominant_emotion[0] # Return dominant emotion in a dictionary
