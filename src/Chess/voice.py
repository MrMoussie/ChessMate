import utils
import speech_recognition as sr


def getmove(info):
    # obtain audio from the microphone
    r = sr.Recognizer()
    move = ""
    with sr.Microphone() as source:
        print(info)
        audio = r.listen(source)
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
