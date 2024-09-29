from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
Analyser = SentimentIntensityAnalyzer()
def analyze(text):
    try:
        sentiment = Analyser.polarity_scores(text)

        if sentiment["compound"] >= 0.05:
            print("\nPositive")
        elif sentiment["compound"] <= -0.05:
            print("\nNegative")
        else:
            print("\nNeutral")
    except Exception as e:
        print(e)

Text = input("Please enter a Text\n")
analyze(Text)
