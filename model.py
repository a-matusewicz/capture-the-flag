import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from gtts import gTTS
import os

def create_model(filename):
    authenticator = IAMAuthenticator("X0t0F11_IQ978kLmsy80im1ldnxh6h06dJh4-c17kRVM")
    visual_recognition = VisualRecognitionV3(
        version='2018-03-19',
        authenticator=authenticator
    )
    visual_recognition.set_service_url("https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/654cef63-0edc-439a-934a-0f2175f22ed0")
    with open(filename, 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file=images_file,
            threshold='0.6',
            owners=["me"]).get_result()
        result = classes['images'][0]['classifiers'][0]['classes']
        if len(result) > 0 and result[0]['score'] > .7:
            pretty = result[0]['class'].split('.')[0]
            return pretty
        else:
            return