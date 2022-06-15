# save this as app.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def dashboard():
    return ("Hello, World!", 200)

@app.route("/item/<id>/", methods=["GET", "POST"])
def item(id):
    if request.method == "GET":
        return {"status":"Success"}, 200
    if request.method == "POST":
       person = {"username": request.json["username"], "password": request.json["password"]} 
    return {"id" : id, "data":person}, 200

@app.route("/login/")
def login():
    person = {"name": request.json["name"]}
    return (person, 200)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")