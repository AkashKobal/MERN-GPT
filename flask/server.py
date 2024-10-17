import openai
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = "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"
openai.api_key = API_KEY

@app.route('/chatBot', methods=['POST', 'GET'])
def postData():
    if request.method == 'GET':
        return jsonify({"message": "ChatBot endpoint is working"})
    
    text = request.json.get('text')
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": text
                }
            ]
        )
        # Return the content of the response
        return jsonify({"response": response.choices[0].message['content']})
    except openai.error.OpenAIError as e:
        # Return an error message with a 400 status code
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)