from re import DEBUG
from flask import Flask, render_template, request

from language_model import language_model

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)