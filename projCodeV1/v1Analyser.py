from textblob import TextBlob
import math

def Detector(inputLine, fileName):

  zen = TextBlob(inputLine)  #add inputLine here
  lines = []
  with open( txt.strip(""),'r') as f:
          sym=0                      #symptoms found
          noOfSym=0                   #symtoms checked
          lines = f.readlines()         #all lines in file
          for line in lines:           #each symptom in file
              noOfSym+=1
              if (zen.find(line.strip()) != -1):
                  print(line)            #print(line , " -- ", zen.find(line.strip()))
                  sym+=1               #print symptom found
  return sym


#driver
#def main():
overallAvg =0         #final value from survey
noOfAns=0
#within loop until inputs from survey ends
# --------Analyzer code----------------
testinput = TextBlob(my days are sad and hopeless. i find everything annoying. get angry a lot. i get quite lazy. i keep trying to find hope. lost appetite. very tired.")
pvalueOfInput = 0
lines=0
txt = "depression.txt"
depressionSym =0
depressionSym += Detector(str(testinput), txt)
if( depressionSym >= 6 ):
              print("\n\n\nu may have "+ txt.strip("").rstrip(".txt"),"\n\n\n")

for sentence in testinput.sentences:
  print( sentence, "--", sentence.sentiment)                  # value for each sentence in text
  #testimonial.sentiment.polarity
 # Detector(str(sentence))                                 #     call detector()
  #avg of all sentences gives mood
  pvalueOfInput += sentence.sentiment.polarity
  lines=lines+1
  #print(lines)
  #print(pvalueOfInput)
pvalueOfInput = pvalueOfInput/lines
#print(pvalueOfInput)
if(pvalueOfInput <0):
  pvalueOfInput=pvalueOfInput*-5
elif (pvalueOfInput == 0):
  pvalueOfInput = 5
else:
  pvalueOfInput=pvalueOfInput+5
print("\n\n\nhealth score = ",pvalueOfInput)
overallAvg += pvalueOfInput
noOfAns = noOfAns+1
#when input from survey ends -exit loop -then
overallAvg = math.ceil(overallAvg/noOfAns)    #to be used for detection of possibility
