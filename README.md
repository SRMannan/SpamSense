# SpamSense: Smart Spam Detection with NLP and Logistic Regression

SpamSense is a project focused on intelligent spam detection using Natural Language Processing (NLP) techniques combined with Logistic Regression. This application can classify messages as spam or not spam based on their content.

## Deployment Link

Visit the live deployment of SpamSense: [SpamSense Deployment](https://spamsense-51.onrender.com/)

## Features

- **NLP-based Classification**: Utilizes advanced NLP techniques to analyze and classify messages.
- **Logistic Regression Model**: Implements a Logistic Regression model trained on labeled data for accurate classification.
- **User-Friendly Interface**: Simple web interface for users to input messages and receive classification results.
- **Bootstrap Integration**: Utilizes Bootstrap for frontend development, ensuring a responsive and modern user experience.

## How It Works

SpamSense preprocesses input messages by tokenizing, removing stopwords, and applying stemming. It then converts these processed texts into numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency) representation. These vectors are fed into a Logistic Regression model trained on a labeled dataset of spam and non-spam messages. The model predicts whether a message is spam or not based on these vectors.

## Technologies Used

- **Python**: Core programming language for application logic.
- **Flask**: Web framework used for developing the application.
- **NLTK**: Natural Language Toolkit for NLP preprocessing tasks.
- **Scikit-learn**: Library used for implementing the Logistic Regression model and TF-IDF vectorization.
- **Bootstrap**: Frontend framework for developing responsive and attractive web interfaces.
- **HTML/CSS**: Frontend components for the user interface.

## Usage

1. **Accessing the Application**: Visit the [deployment link](https://spamsense-51.onrender.com/) to access the web interface.
2. **Input**: Enter a message into the provided text box.
3. **Output**: Receive instant feedback on whether the message is classified as "SPAM" or "NOT SPAM".
