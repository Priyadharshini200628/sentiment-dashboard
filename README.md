# sentiment-dashboard
Product Sentiment Analyzer using NLP
review = input("Enter product review: ")

positive_words = ["good", "excellent", "awesome", "happy", "great"]
negative_words = ["bad", "worst", "poor", "sad", "hate"]

positive_count = 0
negative_count = 0

words = review.lower().split()

for word in words:
    if word in positive_words:
        positive_count += 1
    elif word in negative_words:
        negative_count += 1

if positive_count > negative_count:
    print("Sentiment: Positive 😊")
elif negative_count > positive_count:
    print("Sentiment: Negative 😔")
else:
    print("Sentiment: Neutral 😐")
