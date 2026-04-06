
from flask import Flask , render_template

app= Flask(__name__) 

@app.route("/")
def hello_world() : 
    return "<p> Hello world </p>" 
 
@app.route("/contact")
def contact_page() : 
    return "<p>this is a contact page </p>"


@app.route("/about")
def about_page() : 
    return render_template("index.html")



app.run(debug=True)