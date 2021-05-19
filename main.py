from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/try-now", methods=["GET"])
def try_now():
    return render_template("try_now.html")


@app.route("/analyse", methods=["GET"])
def analyse():
    # TODO: Check if user is logged in or not.
    return render_template("analyse.html")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
