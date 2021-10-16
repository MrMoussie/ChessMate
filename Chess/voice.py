
import speech_recognition as sr

def getmove():
    # obtain audio from the microphone
    r = sr.recognizer()
    move = ""
    with sr.microphone() as source:
        print("say something!")
        audio = r.listen(source)

    # recognize speech using google speech recognition
    try:
        move = r.recognize_google(audio, language = "en-us");
        print("google speech recognition thinks you said " + move)
    except sr.unknownvalueerror:
        print("google speech recognition could not understand audio")
    except sr.requesterror as e:
        print("could not request results from google speech recognition service; {0}".format(e))
    return move
