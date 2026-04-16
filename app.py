from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def email_check():

    if request.method == "POST":

        email = request.form["email"]

        if "@" in email:
            return "Email to‘g‘ri"
        else:
            return "Email noto‘g‘ri"

    return render_template("index.html")

app.run(debug=True)
