from flask import Flask, render_template, request, make_response, redirect, url_for
import requests
from datetime import datetime, timedelta

app = Flask(__name__)
api_url = "http://127.0.0.1:5000/api/"


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/try-now", methods=["GET"])
def try_now():
    if request.cookies != None:
        if request.cookies.get("x-access-token", False):
            return redirect(url_for("analyse"))
    return render_template("try_now.html")


@app.route("/analyse", methods=["GET"])
def analyse():
    if request.cookies != None:
        if request.cookies.get("x-access-token", False):
            return render_template("analyse.html")
    return redirect(url_for("try_now"))


@app.route("/api/signin", methods=["POST"])
def signin():
    payload = request.form
    response = requests.post(api_url + "signin", payload)
    print(response.json())
    if response.status_code == 200 and response.json()["status"] == "success":
        token = response.cookies["x-access-token"]
        response = make_response(response.json(), 200)
        response.set_cookie(
            "x-access-token", token, httponly=True, samesite="Strict", secure=True, expires = datetime.utcnow() + timedelta(minutes=30) 
        )
        return response
    return response.json()


@app.route("/api/signup", methods=["POST"])
def signup():
    payload = request.form
    response = requests.post(api_url + "signup", payload)
    if response.status_code == 200 and response.json()["status"] == "success":
        return response.json()
    return response.json()


@app.route("/api/predict", methods=["POST"])
def predict():
    # TODO: handle all the possible responses
    image = {"predict_img": request.files["predict_img"].stream.read()}
    response = requests.post(api_url + "predict", files=image, cookies=request.cookies)
    if response.json()["message"] == "Prediction complete":
        return response.json()
    return response.json()

@app.route("/logout", methods=["POST"])
def logout():
    response = make_response()
    response.set_cookie(
        "x-access-token", '', httponly=True, samesite="Strict", secure=True, expires = 0
    )
    return response, 200

if __name__ == "__main__":
    app.run(port=8080, debug=True)
