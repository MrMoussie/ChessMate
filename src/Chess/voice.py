import utils
import speech_recognition as sr

def getmove(info):
    # obtain audio from the microphone
    move = ""
    with sr.Microphone() as source:
        r = sr.Recognizer()
        
        print("INFO: " + info)
        # r.adjust_for_ambient_noise(source,duration=1)
        # r.non_speaking_duration = 0.05
        # r.pause_threshold = 0.1
        # r.energy_threshold =50
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