
from flask import Flask , render_template, request

app= Flask(__name__) 

@app.route("/")
def home_page() :
    name  = "jack" 

    numbers  =   [ 1,2,4,56,123]
    return render_template("index.html", name = name, numbers =numbers)

@app.route("/about")
def about_page(): 
    return render_template("about.html") 
app.run(debug=True)