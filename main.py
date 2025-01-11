from flask import Flask, jsonify, request
from helper import predict
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        pred_label = predict(img_bytes)
        return jsonify({"label": f"{pred_label}"})

if __name__ == '__main__':
    app.run()