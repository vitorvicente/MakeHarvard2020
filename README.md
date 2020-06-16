# The Third Eye

This project was my team's entry to the 2020 edition of Harvard's anual makeathon: MakeHarvard.

## The Team

- Patrick Kuzdzal
- Justin Sayah
- Conor Walsh
- Vitor Vicente

## What it does?

The basic idea behind this project was to allow for the creation of a small gadget that would use Google's Vision API to narrate what it saw to the user, thus allowing visually impaired people to have some assistance.

Building the project in python, alongside the Google API, we were able to await a button press to take a snapshot of whatever the camera is pointing at, sending it through to the Vision API, and retrieving the answer to then be narrated via text-to-speech using Pyttsx3.

The hardware behind the project consisted of a Raspberry Pi running Raspbian, with a camera and speakers attatched to it. Although the camera module was native to the Rasp. PI, the speakers were customly adapted for it.

## Issues

Software wise, our biggest issue was to make it so the program would always be listening for the button press, however, once this very small hiccup was resolved, we encountered no further issues.

Hardware wise, the project was a bit of a mess, starting with the fact that the PI's wifi chip was fried, us not having any way of testing the PI, the button not working, and much, much more... However we did, in the end, manage to present a working prototype to the makeathon, and post it here on GitHub

## What we learned?

On top of solidifying our knowledge of the Google Cloud APIs, we learned a great deal about hardware, their components, compatibility, and everything in-between.

## What's next?

Given the time, we would have liked to incorporate a more compact and modular solution, however we are more than proud with our accomplishments.
