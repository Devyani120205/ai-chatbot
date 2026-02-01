from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Uses OPENAI_API_KEY from environment variable
client = OpenAI()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=user_message
        )

        return jsonify({
            "response": response.output_text
        })

    except Exception as e:
        # IMPORTANT: log error to console
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

