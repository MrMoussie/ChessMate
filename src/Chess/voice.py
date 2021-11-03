import utils
import speech_recognition as sr
import pyaudio


def getmove(info):
    # obtain audio from the microphone
    r = sr.Recognizer()
    move = ""
    with sr.Microphone(0) as source:
        print("INFO: " + info)
        audio = r.listen(source)
        print("TEST2")
    # recognize speech using google speech recognition
    try:
        move = r.recognize_google(audio, language="en-us")
        print(move)
        move = utils.traslateMove(move)
        return move
    except sr.UnknownValueError:
        print("Couldn't understand")
    except sr.RequestError as e:
        print("could not request results from google speech recognition service; {0}".format(e))
    return move
