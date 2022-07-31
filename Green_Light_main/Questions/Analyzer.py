from textblob import TextBlob
import math

def Detector(inputLine, txt):

  zen = TextBlob(inputLine)  #add inputLine here
  #txt = filename
  lines = []
  sym=0
  noOfSym=1
  #fileName = ["depression.txt"]
  #for txt in fileName:
  with open( txt.strip(""),'r') as f:
      lines = f.readlines()         #all lines in file
      for line in lines:           #each symptom in file
          noOfSym+=1
          if (zen.find(line.strip()) != -1):
              print(line , " -- ", zen.find(line.strip()))
              sym+=0.3 #print symptom found                      
              print(sym , "sym ")
                  #define a threshold abv which it is a problem..
          # if( sym >= 3 ):
          #     print("\n\n\nu may have "+ txt.strip("").rstrip(".txt"))
  return sym

#driver
#def main():
def Analyse(text,filename):
  overallAvg =0         #final value from survey
  #noOfAns=0
  #within loop until inputs from survey ends
  # --------Analyzer code----------------
  testinput = TextBlob(text)
  pvalueOfInput = 0
  lines=0
  symscore = Detector(str(testinput),filename)
  for sentence in testinput.sentences:
    #print( sentence, "--", sentence.sentiment)                  # value for each sentence in text
    #testimonial.sentiment.polarity
  # Detector(str(sentence))                                 #     call detector()
    #avg of all sentences gives mood
    pvalueOfInput += sentence.sentiment.polarity
    lines=lines+1
  pvalueOfInput = math.ceil(pvalueOfInput/lines)
  #print("\n\n\nhealth score = ",pvalueOfInput)
  pvalueOfInput = (pvalueOfInput-symscore)/2
  
  
  # if(pvalueOfInput <0):
  #   pvalueOfInput=pvalueOfInput*-5
  # elif (pvalueOfInput == 0):
  #   pvalueOfInput = 5
  # else:
  #   pvalueOfInput=pvalueOfInput+5
  
  
  
  #noOfAns = noOfAns+1
  #when input from survey ends -exit loop -then
  #overallAvg = math.ceil(overallAvg/noOfAns)    #to be used for detection of possibility
  return pvalueOfInput
            