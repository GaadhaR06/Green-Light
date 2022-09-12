import contractions
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

def verifier(text):
    text = contractions.fix(text)
    blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
    c =blob.sentiment.classification
    print(c)
    if(text.find("not")>=0):
        
        if(c=="pos"):
            return "negative"
        elif(c=="neg"):
            return "positive"
        else:
            return "neutral"
    else:
        if(c=="neg"):
            return "negative"
        elif(c=="pos"):
            return "positive"
        else:
            return "neutral"
    
