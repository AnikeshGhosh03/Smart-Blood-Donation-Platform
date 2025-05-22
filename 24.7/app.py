from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB Connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/blood_donation"
mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        donor_name = request.form.get("name")
        blood_type = request.form.get("blood_type")
        contact = request.form.get("contact")

        mongo.db.donors.insert_one({"name": donor_name, "blood_type": blood_type, "contact": contact})
        return redirect("/")

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
