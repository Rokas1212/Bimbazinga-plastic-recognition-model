from flask import Flask, render_template, request
from views import views 
import pickle

# with open(f'model/.pkl', 'rb') as f:
#     model = pickle.load(f)

app = Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/prediction', methods = ['POST'])
def predict_plastic():
    if 'image' not in request.files:
        return 'No image found', 400
    file = request.files['image']

    if file.filename == '':
        return 'No iamge found', 400
    
    if request.method == 'POST':
        file = request.files['image']
    file.save('/path/to/save/image')
    return 'File uploaded successfully', 200

if __name__ == '__main__':
    app.run(debug = True, port=8000)

