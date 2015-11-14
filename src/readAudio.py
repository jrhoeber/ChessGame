import speech_recognition as sr 

r = sr.Recognizer()
with sr.Microphone() as source:
  print("Say Something")
  audio = r.listen(source)

try:
  print(r.recognize_google(audio))
except sr.UnknownValueError:
  print("Google Speech Recognition couldn't understand audio")
except sr.RequestError as e:
  print("Could not request results from GSR service; {0}".format(e)) 
