from flask import Flask, json, request, render_template, redirect

app = Flask(__name__)
@app.route('/')  
#not important for now
def home_page():
    example_embed='This string is from python'
    return render_template('Index.html',embed=example_embed)

@app.route('/test', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        print("GET REQUEST")
        return render_template('questiontemplate.html')
    
    elif request.method == 'POST': 
    # POST request
        answer = request.get_json()
        print(answer)  # parse as JSON
        print(type(answer)) 
        text = json.loads(answer) #this converts the json output to a python dictionary
        print(text)
        print(type(text))
        return 'Sucesss', 500

        
if __name__ == "__main__":
    app.run(debug =True)
