from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Load words from file
with open("words.txt") as f:
    WORDS = [line.strip().lower() for line in f if len(line.strip()) == 5]

TARGET_WORD = random.choice(WORDS)

@app.route("/")
def index():
    target_word = random.choice(WORDS)  # Pick new word every page load
    return render_template("index.html", target_word=target_word)

@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    guess = data.get("guess", "").lower()
    target_word = data.get("target_word", "").lower()  # Get target word from client

    if len(guess) != 5 or guess not in WORDS:
        return jsonify({"error": "Invalid word"}), 400

    feedback = []
    target_chars = list(target_word)

    for i in range(5):
        if guess[i] == target_word[i]:
            feedback.append("green")
            target_chars[i] = None
        else:
            feedback.append(None)

    for i in range(5):
        if feedback[i] is None:
            if guess[i] in target_chars:
                feedback[i] = "yellow"
                target_chars[target_chars.index(guess[i])] = None
            else:
                feedback[i] = "gray"

    win = guess == target_word

    return jsonify({"feedback": feedback, "win": win})

if __name__ == "__main__":
    app.run(debug=True)
