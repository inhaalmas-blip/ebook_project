from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

data = pd.read_csv("books.csv")

@app.route("/", methods=["GET", "POST"])
def home():
    books = []
    if request.method == "POST":
        subject = request.form["subject"].lower()
        books = data[data["subject"] == subject].to_dict(orient="records")
    return render_template("index.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)