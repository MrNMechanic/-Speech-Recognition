import os
import speech_recognition as sr

mylist = ["C:\Users\hp\Desktop\BANANA", "C:\Users\hp\Desktop\Haar Training",
              "C:\Users\hp\Desktop\Drive-Github Projects", "C:\Users\hp\Desktop\Open CV Projects"]


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




while r.recognize_sphinx(audio) != ('stop'):


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

