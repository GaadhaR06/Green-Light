from flask import Flask, json, request, render_template
from Analyzer import Analyse

app = Flask(__name__)
@app.route('/')  
#not important for now
def home_page():
    return render_template('HOME.html')

health = {"depression" :0 , "anxiety" :0, "PTSD" :0, 'd':0, 'a':0, 'p':0}

@app.route('/question1', methods=['GET', 'POST'])
def testfn1():
    # GET request
    if request.method == 'GET':
        return render_template('question1.html')
    
    elif request.method == 'POST': 
    # POST request
        answer = request.get_json()
        print(answer)  # parse as JSON string 
        health["depression"] += Analyse(answer,"depression.txt")
        health['d'] += 1
        health["anxiety"] += Analyse(answer,"Anxiety.txt")
        health['a'] += 1
        health["PTSD"] += Analyse(answer,"ptsd.txt")
        health['p'] += 1
        #print(health) 
        # text = json.loads(answer) #this converts the json output to a python dictionary
        return 'Sucesss', 200

@app.route('/question2a', methods=['GET', 'POST'])
def testfn2a():
    # GET request
    if request.method == 'GET':
        return render_template('question2a.html')
    
    elif request.method == 'POST': 
    # POST request
        answer = request.get_json()
        print(answer)  # parse as JSON
        health["depression"] += Analyse(answer,"depression.txt")
        health['d'] += 1
        health["anxiety"] += Analyse(answer,"Anxiety.txt")
        health['a'] += 1
        health["PTSD"] += Analyse(answer,"ptsd.txt")
        health['p'] += 1
        #text = json.loads(answer) #this converts the json output to a python dictionary
        # print(text)
        # print(type(text))
        return 'Sucesss', 200

@app.route('/question2b', methods=['GET', 'POST'])
def testfn2b():
    # GET request
    if request.method == 'GET':
        return render_template('question2b.html')
    
    elif request.method == 'POST': 
    # POST request
        answer = request.get_json()
        print(answer)  # parse as JSON
        health["depression"] += Analyse(answer,"depression.txt")
        health['d'] += 1
        health["anxiety"] += Analyse(answer,"Anxiety.txt")
        health['a'] += 1
        health["PTSD"] += Analyse(answer,"ptsd.txt")
        health['p'] += 1
        return 'Sucesss', 200

@app.route('/question3', methods=['GET', 'POST'])
def testfn3():
    # GET request
    if request.method == 'GET':
        return render_template('question3.html')
    
    elif request.method == 'POST': 
    # POST request
        answer = request.get_json()
        print(answer)  # parse as JSON
        if(answer == "Poor" or answer == "Over-Eating"):
            health["depression"] += -0.1
            health['d'] += 1
            health["anxiety"] += -0.1
            health['a'] += 1
            health["PTSD"] += -0.1
            health['p'] += 1
        if(answer == "None"):
            health["depression"] += 0.7
            health['d'] += 1
            health["anxiety"] += 0.7
            health['a'] += 1
            health["PTSD"] += 0.7
            health['p'] += 1
        return 'Sucesss', 200

@app.route('/question4', methods=['GET', 'POST'])
def testfn4():
    # GET request
    if request.method == 'GET':
        return render_template('question4.html')
    
    elif request.method == 'POST': 
    # POST request
        answer = request.get_json()
        print(answer)  # parse as JSON
        health["depression"] += Analyse(answer,"depression.txt")
        health['d'] += 1
        health["anxiety"] += Analyse(answer,"Anxiety.txt")
        health['a'] += 1
        health["PTSD"] += Analyse(answer,"ptsd.txt")
        health['p'] += 1
        return 'Sucesss', 200

@app.route('/question5', methods=['GET', 'POST'])
def testfn5():
    # GET request
    if request.method == 'GET':
        return render_template('question5.html')
    
    elif request.method == 'POST': 
    # POST request
        answer = request.get_json()
        print(answer)  # parse as JSON
        health["depression"] += Analyse(answer,"depression.txt")
        health['d'] += 1
        health["anxiety"] += Analyse(answer,"Anxiety.txt")
        health['a'] += 1
        health["PTSD"] += Analyse(answer,"ptsd.txt")
        health['p'] += 1
        return 'Sucesss', 200

@app.route('/question6', methods=['GET', 'POST'])
def testfn6():
    # GET request
    if request.method == 'GET':
        return render_template('question6.html')
    
    elif request.method == 'POST': 
    # POST request
        answer = request.get_json()
        print(answer)  # parse as JSON
        if(answer == "Poor"):
            health["depression"] += -0.1
            health['d'] += 1
            health["anxiety"] += -0.1
            health['a'] += 1
            health["PTSD"] += -0.1
            health['p'] += 1
        elif(answer == "Moderate"):
            health["depression"] += 0.1
            health['d'] += 1
            health["anxiety"] +=0.1
            health['a'] += 1
            health["PTSD"] += 0.1
            health['p'] += 1
        elif(answer == "Good"):
            health["depression"] += 0.8
            health['d'] += 1
            health["anxiety"] +=0.8
            health['a'] += 1
            health["PTSD"] += 0.8
            health['p'] += 1
        return 'Sucesss', 200

@app.route('/question7', methods=['GET', 'POST'])
def testfn7():
    # GET request
    if request.method == 'GET':
        return render_template('question7.html')
    
    elif request.method == 'POST': 
    # POST request
        answer = request.get_json()
        print(answer)  # parse as JSON
        health["depression"] += Analyse(answer,"depression.txt")
        health['d'] += 1
    return 'Sucesss', 200

@app.route('/question8', methods=['GET', 'POST'])
def testfn8():
    # GET request
    if request.method == 'GET':
        return render_template('question8.html')
    
    elif request.method == 'POST': 
    # POST request
        answer = request.get_json()
        print(answer)  # parse as JSON
        health["depression"] += Analyse(answer,"depression.txt")
        health['d'] += 1
    return 'Sucesss', 200

@app.route('/question9', methods=['GET', 'POST'])
def testfn9():
    # GET request
    if request.method == 'GET':
        return render_template('question9.html')
    
    elif request.method == 'POST': 
    # POST request
        answer = request.get_json()
        print(answer)  # parse as JSON
        if(answer == "Not at all interested"):
            health["depression"] += -0.5
        elif(answer == "Moderately interested"):
            health["depression"] += 0
            health['d'] += 1
        elif(answer == "Interested"):
            health["depression"] += 0.3
            health['d'] += 1
        elif(answer == "Really interested"):
            health["depression"] += 0.8
            health['d'] += 1
    return 'Sucesss', 200

@app.route('/question10', methods=['GET', 'POST'])
def testfn10():
    # GET request
    if request.method == 'GET':
        return render_template('question10.html')
    
    elif request.method == 'POST': 
    # POST request
        answer = request.get_json()
        print(answer)  # parse as JSON
        if(answer == "Very low"):
            health["depression"] += 1
        elif(answer == "Low"):
            health["depression"] += 0.5
            health['d'] += 1
        elif(answer == "Moderate"):
            health["depression"] += 0
            health['d'] += 1
        elif(answer == "High"):
            health["depression"] += -0.5
            health['d'] += 1
        elif(answer == "Very high"):
            health["depression"] += -1
            health['d'] += 1
    return 'Sucesss', 200       

#no ques 11

@app.route('/question12', methods=['GET', 'POST'])
def testfn12():
    # GET request
    if request.method == 'GET':
        return render_template('question12.html')
    
    elif request.method == 'POST': 
    # POST request
        answer = request.get_json()
        print(answer)  # parse as JSON
        health["depression"] += Analyse(answer,"depression.txt")
        health['d'] += 1
    return 'Sucesss', 200

        
if __name__ == "__main__":
    app.run(debug =True)

 



 
