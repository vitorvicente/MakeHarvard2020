# Imports
import uuid, io, os, pyttsx3 as tts
from picamera import PiCamera
from time import sleep
from google.cloud import vision
from google.cloud.vision import types

def takePhoto():
    camera = PiCamera()
    camera.start_preview(alpha=192)
    sleep(1)
    hexID = str(generateID() + ".jpg")
    print("[*] Photo Created w/ ID: " + hexID)
    path = str("/home/pi/Desktop/Pictures/" + hexID)
    camera.capture(path)
    camera.stop_preview()
    return(path)

def speak(obj):
    client = tts.init()
    getSpeed = client.getProperty('rate')
    client.setProperty('rate', 145)
    client.say(obj)
    client.runAndWait()

def analyze(filePath):
    client = vision.ImageAnnotatorClient.from_service_account_json('/home/pi/makeharvard.json')
    file_name = os.path.abspath(filePath)
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.label_detection(image=image)
    objects = response.label_annotations
    print("[*] The Likely Object is: " + str(objects[0]))
    return(objects[0].description)

def generateID():
    randID = uuid.uuid1()
    return randID.hex

def main():
    print("[*] Ready to Analyze!")
    filePath = takePhoto()
    object = analyze(filePath)
    speak(object)

main()
