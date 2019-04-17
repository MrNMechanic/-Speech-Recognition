import os
import speech_recognition as sr

mylist = ["first path", "second path",
              "third path", "fourth path"] #you can add as many paths as you like#


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    r.adjust_for_ambient_noise(source, duration=5)
    print('Please Let me know the Number of the File')
    audio = r.listen(source)

    try:
        print("I think you said '" + r.recognize_sphinx(audio) + "'")
    except sr.UnknownValueError:
        print("I could not understand audio")
    except sr.RequestError as e:
        print("Error; {0}".format(e))




while r.recognize_sphinx(audio) != ('stop'): #say stop to terminate the process#


    if r.recognize_sphinx(audio) == ('one'):
        os.startfile(mylist[0])
    elif r.recognize_sphinx(audio) == ('to'):
        os.startfile(mylist[1])
    elif r.recognize_sphinx(audio) == ('three'):
        os.startfile(mylist[2])
    elif r.recognize_sphinx(audio) == ('for'):
        os.startfile(mylist[3])
    else:
        print ('Sorry didnt got that')



    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=5)
        print('Please Let me know the Number of the File')
        audio = r.listen(source)

        try:
            print("I think you said '" + r.recognize_sphinx(audio) + "'")
        except sr.UnknownValueError:
            print("I could not understand audio")
        except sr.RequestError as e:
            print("Error; {0}".format(e))


print ('Gotha.C u soon')

