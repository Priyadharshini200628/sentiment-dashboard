# file name: app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# -----------------------------
# Sentiment Word Lists
# -----------------------------
positive_words = [
    "good", "excellent", "awesome",
    "happy", "great", "amazing",
    "love", "best", "nice"
]

negative_words = [
    "bad", "worst", "poor",
    "sad", "hate", "terrible",
    "awful", "boring"
]

# -----------------------------
# Read Reviews from File
# -----------------------------
def load_reviews():
    file_path = os.path.join(os.getcwd(), "reviews.txt")

    reviews = []

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            reviews = [line.strip() for line in f.readlines()]

    return reviews


# -----------------------------
# Sentiment Analysis Function
# -----------------------------
def analyze_sentiment(review):

    positive_count = 0
    negative_count = 0

    words = review.lower().split()

    for word in words:

        # Remove punctuation
        word = word.replace(".", "").replace(",", "").replace("!", "").replace("?", "")

        if word in positive_words:
            positive_count += 1

        elif word in negative_words:
            negative_count += 1

    if positive_count > negative_count:
        sentiment = "Positive 😊"

    elif negative_count > positive_count:
        sentiment = "Negative 😔"

    else:
        sentiment = "Neutral 😐"

    return sentiment


# -----------------------------
# API 1 : Get All Reviews
# -----------------------------
@app.route('/', methods=['GET'])
def get_reviews():

    reviews = load_reviews()

    result = []

    for review in reviews:

        sentiment = analyze_sentiment(review)

        result.append({
            "review": review,
            "sentiment": sentiment
        })

    return jsonify(result)


# -----------------------------
# API 2 : Analyze Single Review
# -----------------------------

@app.route('/analyze', methods=['GET', 'POST'])
def analyze_review():

    # For browser testing
    if request.method == 'GET':

        review = request.args.get('review', '')

        if review == '':
            return jsonify({
                "message": "Enter review in URL like /analyze?review=good product"
            })

        sentiment = analyze_sentiment(review)

        return jsonify({
            "review": review,
            "sentiment": sentiment
        })

    # For POST request
    data = request.get_json(force=True)

    review = data.get("review", "")

    sentiment = analyze_sentiment(review)

    return jsonify({
        "review": review,
        "sentiment": sentiment
    })


# -----------------------------
# API 3 : Dashboard Summary
# -----------------------------
@app.route('/dashboard', methods=['GET'])
def dashboard():

    reviews = load_reviews()

    positive = 0
    negative = 0
    neutral = 0

    for review in reviews:

        sentiment = analyze_sentiment(review)

        if "Positive" in sentiment:
            positive += 1

        elif "Negative" in sentiment:
            negative += 1

        else:
            neutral += 1

    return jsonify({
        "total_reviews": len(reviews),
        "positive_reviews": positive,
        "negative_reviews": negative,
        "neutral_reviews": neutral
    })


# -----------------------------
# Run Flask App
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)