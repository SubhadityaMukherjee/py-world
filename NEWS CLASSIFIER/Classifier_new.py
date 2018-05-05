import csv
import os
import re

import bs4
import numpy as np
import pandas as pd
import requests
import sklearn
from nltk.corpus import stopwords
from sklearn import datasets
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder


def get_words(s):
    s = s.lower()
    s = re.sub("[^a-zA-Z]", " ", s)
    stops = set(stopwords.words("english"))
    final = ""
    for a in s.split():
        if not a in stops:
            final += str(a + " ")
    return final


def dataclass():
    current_path = os.getcwd()
    data_path = current_path + "/" + "DATASETS/all_data"

    files_in_dir = os.listdir(data_path)
    name, category, title = list(), list(), list()
    for a in files_in_dir:
        os.chdir(data_path)
        p = open(a, "r+")
        try:
            ap = p.readlines()[0].rstrip()
            name.append(a)
            category.append(a[0])
            title.append(ap)
            p.close()
        except:
            p.close()
            pass

    # Scrape
    ur = input("Enter the url of the article: ").strip()
    soup = bs4.BeautifulSoup(requests.get(ur).text, "html.parser")
    os.chdir(current_path)
    fil = open("Scraped article.txt", "wb+")
    fil.write(soup.text.encode('utf-8'))
    fil.close()

    fil_read = open("Scraped article.txt", "r", encoding='utf-8', errors='ignore').readlines()
    for a in fil_read:
        if len(a) > 3:
            edit = get_words(str(a))
            title.append(edit)
            break
    name.append("test")
    category.append(" ")
    d = {"name": name, "title": title, "category": category}

    df = pd.DataFrame(data=d, columns=['name', 'category', 'title'])
    df.to_csv('datapartition.csv')


def Training():
    # read and split into test and train
    part = pd.DataFrame.from_csv("datapartition.csv", sep=',')
    part['text'] = [get_words(s) for s in part['title']]
    vectorizer = CountVectorizer()
    x = vectorizer.fit_transform(part['text'])
    encoder = LabelEncoder()
    y = encoder.fit_transform(part['category'])
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3)
    # X_test = vectorizer.fit_transform(part['text'])
    nb = MultinomialNB()

    nb.fit(X_train, Y_train)
    # print(list(encoder.classes_))
    # print(nb.score(X_test,Y_test))
    result = nb.predict(x[-1])
    d = {'[0]': "Try this again. There seems to be an error here.", '[1]': "Business", '[2]': "Entertainment",
         '[3]': "Politics", '[4]': "Sports", '[5]': "Technology"}
    fin_result = d[str(result)]

    return "This article is of the class: " + fin_result


dataclass()

print(Training())
