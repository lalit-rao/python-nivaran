from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response, initialize_chat, correct_spelling  # Import correct_spelling

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    welcome_message = initialize_chat()
    return render_template('index.html', welcome_message=welcome_message)

@app.post('/predict')
def predict():
    text = request.get_json().get("message")
    corrected_text = correct_spelling(text)  # Correct the spelling
    response = get_response(corrected_text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == '__main__':
    app.run(host= '10.55.3.203', port= 3000, debug=True)
