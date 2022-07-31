from textblob import TextBlob
#def Detector(inputLine):

zen = TextBlob("i sad u")  #add inputLine here
lines = []
fileName = ["depression.txt", "anxiety.txt" ]
for txt in fileName:
    with open(txt,'r') as f:
        sym=0
        noOfSym=0
        lines = f.readlines()         #all lines in file
        for line in lines:           #each symptom in file
            noOfSym+=1
            if (zen.find(line.strip())
                print(line , " -- ", zen.find(line.strip()))
                sym+=1 #print symptom found
