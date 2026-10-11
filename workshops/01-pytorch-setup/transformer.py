from transformers import pipeline

# Load a pre-trained BERT model for sentiment analysis
sentiment_analysis = pipeline("sentiment-analysis")

# Prompt for user input
user_input = input("Enter a sentence or paragraph for sentiment analysis: ")

# Perform sentiment analysis
result = sentiment_analysis(user_input)

# Display the results
print("Sentiment Analysis Result:", result)