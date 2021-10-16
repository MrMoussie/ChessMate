import speech_recognition as sr

def getMove():
    # obtain audio from the microphone
    r = sr.Recognizer()
    move = ""
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        move = r.recognize_google(audio, language = "en-US");
        print("Google Speech Recognition thinks you said " + move)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return move
