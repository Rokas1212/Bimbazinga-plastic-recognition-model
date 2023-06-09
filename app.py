# Importing required libs
from flask import Flask, render_template, request, url_for
from model import predict_result
from werkzeug.utils import secure_filename
import os
# Instantiating flask app
app = Flask(__name__)


# Home route
@app.route("/")
def main():
    return render_template("index.html")


# Prediction route
@app.route('/', methods=['POST'])
def predict_image_file():
    try:
        if request.method == 'POST':
            file = request.files['file']

            pred, index, probs = predict_result(file)
            return render_template("result.html", predictions=str(pred), probs=int(probs[index]*100))
    except:
        error = "File cannot be processed."
        return render_template("result.html", err=error)


# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
