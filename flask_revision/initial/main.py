
from flask import Flask , render_template

app= Flask(__name__) 
# app = Flask(__name__, static_folder="assests")  ##remaning static to asset
@app.route("/")
def hello_world() : 
    return render_template("index.html")
 
@app.route("/contact")
def contact_page() : 
    return render_template("contact.html")


@app.route("/about")
def about_page() : 
    return render_template("about.html")

app.run(debug=True)