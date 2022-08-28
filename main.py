#import speech_recognition library
import speech_recognition as sr

#initialize Reconizer variable
r = sr.Recognizer()

#start a while loop to continuously perform speech recognition
while True:
    try:
        with sr.Microphone() as source:
            print("Say something....")
            audio = r.listen(source)

            text = r.recognize_google(audio)
            text = text.lower()
            print(f"Recognized speech:  {text}")
    except:
        print("could not understand, please repeat")
        r = sr.Recognizer()
        continue

