from textblob import TextBlob
import math

overallAvg =0         #final value from survey
noOfAns=0
#within loop until inputs from survey ends
# --------Analyzer code----------------
testinput = TextBlob(" --input text --")
valueOfInput = 0
lines=0
for sentence in testinput.sentences:
  print( sentence, "--", sentence.sentiment)                  # value for each sentence in text
  #testimonial.sentiment.polarity
  Detector(sentence)
  #avg of all sentences gives mood
  valueOfInput += sentence.sentiment
  lines=lines+1
valueOfInput = ceil(valueOfInput/lines)
overallAvg += valueOfInput
#when input from survey ends -exit loop -then
overallAvg = ceil(overallAvg/noOfAns)    #to be used for detection of possibility
