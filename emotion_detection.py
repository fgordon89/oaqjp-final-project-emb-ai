import requests  # Import the requests library to handle HTTP requests

def emotion_detection (text_to_analyze):  # Define function named emotion_detection 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection
    myobj = {"raw_document": {"text": text_to_analyze } }  # Create dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set headers required for API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with text and headers
    
    return response.text  # Return the response text from the API