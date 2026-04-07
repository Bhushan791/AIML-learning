
from flask import Flask , render_template, request, flash,jsonify

app= Flask(__name__) 

app.secret_key = "dfghjklas647298eudghfd"
@app.route("/home")
def home_page() :
    flash("hello welcome")
    name  = "jack" 

    numbers  =   [ 1,2,4,56,123]
    return render_template("index.html", name = name, numbers =numbers)

@app.route("/about")
def about_page(): 
    flash("welcome to about page!")
    return render_template("about.html")  



## query param  
@app.route("/")
def hello_world () : 
    name = request.args.get("name") 
    print(name)
    return render_template("index2.html", name=name)



@app.route("/apitest") 
def api_test() : 
    data = {"output" : 45, "Accuracy" : 90.12}

    return jsonify(data), 200


@app.route('/api/predict', methods=['GET'])
def predict():
    value = request.args.get('value')
    
    if value is None:
        return jsonify({'error': 'Missing input'}), 400
 
    # Simulated prediction (replace with actual model call)
    result = int(value) * 2
 
    return jsonify({
        'input': value,
        'prediction': result
    }) 
##test with : /api/predict?value=7

app.run(debug=True)