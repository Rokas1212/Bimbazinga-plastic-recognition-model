# Importing required libs
from flask import Flask, render_template, request
from model import  predict_result
import os
# Instantiating flask app
app = Flask(__name__)


# Home route
@app.route("/")
def main():
    return render_template("index.html")


# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    try:
        if request.method == 'POST':
            img = request.files['file']
            predicted_label,_,predicted_prob = predict_result('C:\\Users\\matas\\OneDrive\\Stalinis kompiuteris\\4(LDPE)\\ERMA5291.jpg')
            # pred = predict_result(img)
            
            return render_template("result.html", predictions=str(predicted_label + predicted_prob))

    except:
        error = "File cannot be processed."
        return render_template("result.html", err=str(img))


# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
