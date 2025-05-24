from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text', '')
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return jsonify({
        'text': text,
        'sentiment': 'positive' if sentiment > 0 else 'negative' if sentiment < 0 else 'neutral'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
