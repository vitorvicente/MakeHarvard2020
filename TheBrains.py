# Imports
import uuid, io, os, pyttsx3 as tts, RPi.GPIO as GPIO
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
    vol = client.getProperty('volume')
    client.setProperty('volume',1.0)
    client.say(obj)
    client.runAndWait()
    exit()

def analyze(filePath):
    client = vision.ImageAnnotatorClient.from_service_account_json('/home/pi/makeharvard.json')
    file_name = os.path.abspath(filePath)
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.label_detection(image=image)
    objects = response.label_annotations
    return(objects[0].description)

def generateID():
    randID = uuid.uuid1()
    return randID.hex

def main_event():
    filePath = takePhoto()
    object = analyze(filePath)
    print("[*] The Likely Object is: " + str(object))
    speak(object)

def checkButtonPress():
    print("[*] Ready to Analyze!")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    while(1):
        if GPIO.input(18) == GPIO.HIGH:
            main_event()
    #GPIO.add_event_detect(18, GPIO.RISING, callback = main_event)


checkButtonPress()
