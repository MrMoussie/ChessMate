import utils
import speech_recognition as sr


def getmove(info, promotion=False):
    # obtain audio from the microphone
    move = ""
    micIndex = 0
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if (name == "default"):
            micIndex = index
    with sr.Microphone(device_index=micIndex) as source:
        r = sr.Recognizer()
        if not promotion:
            print("Listening -> " + info)
        else:
            print("Listening -> give your promotion:\n", 'Queen = 1\n','Knight = 2\n', 'Bishop = 3\n', 'Rook = 4\n')
        r.adjust_for_ambient_noise(source, duration=1)
        # r.non_speaking_duration = 0.25
        # r.pause_threshold = 0.5
        # r.energy_threshold =50
        audio = r.listen(source)
    # recognize speech using google speech recognition
    try:
        move = r.recognize_google(audio, language="en-us")
        print(move)
        if not promotion:
            move = utils.traslateMove(move)
            return move
        else:
            move = utils.translatePromotion(move)
            return move
    except sr.UnknownValueError:
        print("Couldn't understand")
        return None
    except sr.RequestError as e:
        print("could not request results from google speech recognition service; {0}".format(e))
    return None
