from urllib import request, response

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin

from chat import get_response

app= Flask(__name__)
CORS(app,support_credentials=True)


@app.route('/predict', methods = ['POST'])
@cross_origin(supports_credentials=True)
def predict():
    print(request.get_json());
    text = request.get_json().get("message")
    response = get_response(text)
    message ={"responsePayload":response}
    return jsonify(message)

if __name__=="main":
    
    app.run(debug=False);
