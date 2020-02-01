import uuid
import pyttsx3 as tts
from picamera import PiCamera
from time import sleep

def takePhoto():
    camera = PiCamera()
    camera.start_preview(alpha=192)
    sleep(1)
    hexID = generateID()
    camera.capture("/home/pi/Desktop/Pictures/" + hexID)
    camera.stop_preview()

def generateID():
    randID = uuid.uuid1()
    return randID.hex

def speak(obj):
    client = tts.init()
    getSpeed = client.getProperty('rate')
    client.setProperty('rate', 145)
    client.say(obj)
    client.runAndWait()

def main():
    takePhoto()
main()
