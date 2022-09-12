from textblob import TextBlob
import math
from verify import verifier

def Detector(inputLine, txt):

  zen = TextBlob(inputLine)  #add inputLine here
  lines = []
  sym=0
  noOfSym=1
  with open( txt.strip(""),'r') as f:
      lines = f.readlines()         #all lines in file
      for line in lines:           #each symptom in file
          noOfSym+=1
          if (zen.find(line.strip()) != -1):
              #print(line , " -- ", zen.find(line.strip()))
              sym+=1 #print symptom found                      
              print(sym , "sym ")
  return sym


def Analyse(text,filename):

  # --------Analyzer code----------------
  testinput = TextBlob(text)
  pvalueOfInput = 0
  lines=0
  symscore = Detector(str(testinput),filename)
  for sentence in testinput.sentences:
    print( sentence, "--", sentence.sentiment)                  # value for each sentence in text
    v=verifier(str(sentence))
    print("varifier says - " + v)
    c = sentence.sentiment.polarity
    print("other says - ", c)
    # print(type(c))
    if((v == "positive" and c>0) or (v == "negative" and c<0) ):
      pvalueOfInput += c
    else:
      pvalueOfInput -=c
    lines=lines+1
    print("therefore ",c)
  pvalueOfInput = pvalueOfInput/lines
  if(symscore>0):
    return (pvalueOfInput-1)/2 
  else:
    return pvalueOfInput
