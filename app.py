from flask import Flask, render_template, request
import pickle
import numpy as np
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
english_stopwords = stopwords.words('english')

import string
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

# Load the pre-trained TF-IDF vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    res = []
    for char in text:
        if char.isalnum():
            res.append(char)

    text = res[:]
    res.clear()

    # removing stopwords
    for char in text:
        if char not in english_stopwords and char not in string.punctuation:
            res.append(char)

    text = res[:]
    res.clear()

    # handling stemming
    for char in text:
        res.append(ps.stem(char))

    return " ".join(res)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            input_sms = str(request.form['floatingTextarea2'])

            # preprocess
            transformed_sms = transform_text(input_sms)

            # vectorise
            vector_sms = tfidf.transform([transformed_sms])

            # prediction
            res = model.predict(vector_sms)[0]

            if res == 1:
                prediction_text = "SPAM"
            else:
                prediction_text = "NOT SPAM"

            return render_template('home.html', prediction_text=f'The message is: {prediction_text}')

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return f"An error occurred while processing the request.{str(e)}", 501  # Return HTTP 500 status for internal server error


if __name__ == '__main__':
    app.run(debug=True)
