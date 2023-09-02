from textblob import TextBlob

class Sentiment:
    def __init__(self, text, threshold):
        self.text = text
        self.polarity = self.get_polarity()
        self.threshold = threshold
        self.emoji = self.get_emoji()

    def get_polarity(self):
        blob = TextBlob(self.text)
        polarity = blob.sentiment.polarity
        return polarity

    def get_emoji(self):
        if self.polarity > self.threshold:
            return '😀'
        elif self.polarity < -self.threshold:
            return '😞'
        else:
            return '👍'


