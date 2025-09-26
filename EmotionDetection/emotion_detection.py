import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myObj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myObj, headers=header)

    # If the response status code is 200, print the response normally
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        #dominant_score = emotion_scores[dominant_emotion]

        emotion_scores['dominant_emotion'] = dominant_emotion

    # If the response status code is 400, return same dictionary with values for all keys being 'None' 
    elif response.status_code == 400:
        for key, value in emotion_scores.items():
          if isinstance(value, (int, float)):
             emotion_scores[key] = None

    formatted_response = json.loads(response.text)
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    #dominant_score = emotion_scores[dominant_emotion]

    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores