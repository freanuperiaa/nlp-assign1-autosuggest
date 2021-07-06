from re import DEBUG
from flask import Flask, render_template, request

from language_model import language_model

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template('home.html')
    
    if request.method == "POST":
        print(request.form)
        sentence = request.form['sentence']
        print(sentence)
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)