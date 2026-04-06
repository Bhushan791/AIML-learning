
from flask import Flask , render_template, request

app= Flask(__name__) 

@app.route("/", methods=["GET","POST"])
def home_page() : 
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"] 
        print(f"The email is {email} and password is {password}") 
        ##save it to the database now  
        return "<b> you are now logged in!</b>" 
    ##return again to same page after login
    return render_template("index.html")
 

app.run(debug=True)