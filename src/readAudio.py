import speech_recognition as sr 
#import pyaudio

validSet = set(["A", "B", "C", "D", "E", "F", "G", "H"]) 

def getMove():

  #r = sr.Recognizer()
  #with sr.Microphone() as source:
   # print("Say Something")
   # r.adjust_for_ambient_noise(source)
    #audio = r.listen(source)
    #print("Got something")
  #try:
     #command = r.recognize_google(audio)
     #command = "23affafafaffaA8"
     command = raw_input("Enter your move: ")
     return convertMove(command)
  #except sr.UnknownValueError:
  #  print("Google Speech Recognition couldn't understand audio")
  #except sr.RequestError as e:
  #  print("Could not request results from GSR service; {0}".format(e)) 

#Currently assuming valid string
def convertMove(command):
  try:
    print command 
    temp = command.split()
    col1 = temp[0][0]
    col2 = temp[2][0]
    row1 = int(temp[0][1])
    row2 = int(temp[2][1])
    if col1 not in validSet or col2 not in validSet or \
    row1 < 1 or row1 > 8 or row2 < 1 or row2 > 8:  
      return ()
    else: 
      return (col1, row1, col2, row2)
  except Exception as e:
    print e.message
    return ()

