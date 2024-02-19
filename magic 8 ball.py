import random

# List of possible responses
responses = [
    "It is certain.",
    "Outlook good.",
    "You may rely on it.",
    "Ask again later.",
    "Concentrate and ask again.",
    "Reply hazy, try again.",
    "My reply is no.",
    "My sources say no."
]

def magic_8_ball(question):
    """Generates a random Magic 8 Ball response for the given question."""
    answer_index = random.randint(0, len(responses) - 1)
    return responses[answer_index]

# API endpoint (using Flask for illustration)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/magic8ball", methods=["POST"])
def handle_magic_8_ball():
    question = request.json.get("question")
    if not question:
        return jsonify({"error": "Missing question in request body."}), 400

    answer = magic_8_ball(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
