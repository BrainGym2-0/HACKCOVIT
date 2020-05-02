from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route("/java")
def java():
    return render_template("java.html")


@app.route("/dsa")
def dsa():
    return render_template("dsa.html")


@app.route("/os")
def os():
    return render_template("os.html")


if __name__ == "__main__":
    app.run(debug=True)
