# Imports
import uuid, io, os, pyttsx3 as tts
#from picamera import PiCamera
from time import sleep
from google.cloud import vision
from google.cloud.vision import types

class main:
    def __init__(self):
        print("[*] Ready to analyze")

    def takePhoto(self):
        camera = PiCamera()
        camera.start_preview(alpha=192)
        sleep(1)
        hexID = generateID()
        path = "/home/pi/Desktop/Pictures/" + hexID + ".jpg"
        camera.capture()
        camera.stop_preview(path)
        return(path)

    def generateID():
        randID = uuid.uuid1()
        return randID.hex

    def speak(obj):
        client = tts.init()
        getSpeed = client.getProperty('rate')
        client.setProperty('rate', 145)
        client.say(obj)
        client.runAndWait()

class visionAPI:
    def analyze(filePath):
        client = vision.ImageAnnotatorClient.from_service_account_json('/home/pi/makeharvard.json')
        file_name = os.path.abspath(filePath)
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content)
        response = client.label_detection(image=image)
        objects = response.label_annotations
        return(labels[0].description)

if __name__ == '__main__':
    TTE = main()
    filePath = TTE.takePhoto()
    object = visionAPI.analyze(filePath)
    print("[*] The Likely Object Is: " + object)
    TTE.speak(object)
