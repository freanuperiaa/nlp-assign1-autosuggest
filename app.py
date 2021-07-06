from re import DEBUG
from flask import Flask, render_template, request

from language_model import language_model

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template('home.html', predicted_word = "")
    
    if request.method == "POST":
        sentence = request.form['sentence']
        words_list = sentence.split()
        predicted_text = language_model.predict(words_list)
        print(predicted_text)
        return render_template('home.html', predicted_word=predicted_text, input_text=sentence)

if __name__ == '__main__':
    app.run(debug=True)