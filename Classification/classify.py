import random

import sys
sys.path.append("../")

import pickle
import numpy as np

from nltk.corpus import gutenberg
from nltk.corpus import webtext

from features_all import features_list

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn import svm

from sklearn.metrics import plot_confusion_matrix, confusion_matrix
from sklearn.metrics import f1_score, accuracy_score

import matplotlib.pyplot as plt

def make_data():
    global sentences
    global y
    other_sentences = open("./Corpus/Other/other.txt").readlines()[:100]
    y1 = len(other_sentences)
    general_sentences = open("./Corpus/General/general.txt").readlines()[:100]    
    y2 = len(general_sentences)

    sentences = [sentence for sentence in other_sentences]
    sentences += [sentence for sentence in general_sentences]

    y = [0]*y1
    y += [1]*y2

    data = [(sentence, label) for sentence, label in zip(sentences, y)]
    random.shuffle(data)

    sentences = []
    y = []
    for sentence, y_temp in data:
        sentences.append(sentence)
        y.append(y_temp)
    
    return (sentences, y)

def extract_features(sentences):
    features = []
    for sentence in sentences:
        feature_sent = []
        for feature in features_list:
            feature_sent.append(feature(sentence))
        features.append(feature_sent)
    return features

def fit_model(features, y, test_size=0.20):
    X_train, X_test, y_train, y_test = train_test_split(
        features, y, test_size=test_size, random_state=42
    )
    print("Split and Shuffled the Data")

    classify = LogisticRegression()
    classify.fit(X_train, y_train)
    
    return classify, X_test, y_test

def show_model_results(X_test, y_test):
    y_pred = classify.predict(X_test)

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\n\nF1 Score: ", round(f1_score(y_test, y_pred), 2))
    print("Accuracy: ", accuracy_score(y_test, y_pred))
    
    plot_confusion_matrix(classify, X_test, y_test)
    plt.show()

def save_model(name=""):
    pickle.dump(classify, open(f'./Classification/Models/classifier_{name}.model', 'wb'))

def load_model(name=""):
    classify = pickle.load(open(f'./Classification/Models/classifier_{name}.model', 'rb'))
    return classify

def predict(classifier, input_text):
    features = extract_features([input_text])
    return classifier.predict(features)

if __name__ == "__main__":
    sentences, y = make_data()
    print("Loaded Data")

    features = extract_features(sentences)
    print("Added features:")
    for i, feature in enumerate(features_list):
        print(f"\t{i}. {feature.__name__}")

    classify, X_test, y_test = fit_model(features, y, test_size=0.2)
    print("Fitted Model")
    
    # show_model_results(X_te`st, y_test)

    save_model("LogReg")
    print("Saved Model")

    classifier = load_model("LogReg")
    print("Loaded Model")
    print(predict(classifier, input("Enter test: ")))
