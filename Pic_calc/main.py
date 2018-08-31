# importing required modules
from sklearn.metrics import classification_report
from sklearn.externals import joblib
from sklearn import datasets
import numpy as np, cv2, imutils
import string
import os
from PIL import Image
import csv
import pandas as pd
import time
# for creating Neural Network  I am using  MLPClassifier from sklearn

from sklearn.neural_network.multilayer_perceptron import MLPClassifier

def create_data_set():
    current_path = os.getcwd()
    data_path = current_path + "/data"

    #files_in_dir = os.listdir(data_path)
    #data_set = list()
    data,labels = [],[]
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(name)
            if("exp" not in name):
                try:
                    p = str(os.path.join(root, name)).split('/')
                    label = p[-1][0]
                    img_array = imageio.imread(os.path.join(root, name))
                    #record = numpy.append(label,img_data)
                    #data_set.append(record)
                    labels.append(label)
                    data.append(img_array)
                except:
                    pass
        time.sleep(1)
    d = {"data":data,"labels":labels}
    df = pd.DataFrame(data=data_set, columns=['data', 'labels'])
    df.to_csv('data.csv')
    

def mathpart(l):
    fo = ''
    for a in l:
        if (a != '='):
            fo = fo + str(a)
    try:
        return (str(eval(fo)).strip())
    except:
        return (fo)


def train():

    #dataset = pd.read_csv("data_test.csv",names = ['data','labels'])
    #X = dataset.labels # Our Features
    #y = dataset.data # Our labels

    dataset = datasets.fetch_mldata("MNIST Original")
    features = np.array(dataset.data, 'int16') 
    labels = np.array(dataset.target, 'int')

    mlp = MLPClassifier(hidden_layer_sizes=(240), max_iter=6, verbose=True)

    # fitting our model
    mlp.fit(X, y)

    # saving our model
    joblib.dump(mlp, "model.pkl")



def test():
    model = joblib.load('model.pkl')
    img = cv2.imread('test.jpg')
    img = imutils.resize(img,width=300)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    kernel = np.ones((40, 40), np.uint8)

    # Our operations on the frame come here

    # applying blackhat thresholding
    blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

    # applying OTSU's thresholding
    ret, thresh = cv2.threshold(blackhat, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # performing erosion and dilation
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # finding countours in image
    ret, cnts, hie = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # loading our ANN model

    l = []
    for c in cnts:
        try:
            # creating a mask
            mask = np.zeros(gray.shape, dtype="uint8")

            (x, y, w, h) = cv2.boundingRect(c)

            hull = cv2.convexHull(c)
            cv2.drawContours(mask, [hull], -1, 255, -1)
            mask = cv2.bitwise_and(thresh, thresh, mask=mask)

            # Getting Region of interest
            roi = mask[y - 7:y + h + 7, x - 7:x + w + 7]
            roi = cv2.resize(roi, (28, 28))
            roi = np.array(roi)
            # reshaping roi to feed image to our model
            roi = roi.reshape(1, 784)

            # predicting
            prediction = model.predict(roi)
            l.append(int(prediction))
 
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv2.putText(img, str(int(prediction)), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 1)
            

        except Exception as e:
            print(e)
    print(l[::-1])
    cv2.putText(img,mathpart(l),(x+w, y+h), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 1)
    img = imutils.resize(img,width=500)
    cv2.imshow('Detection',img)
    cv2.imwrite('result2.jpg',img)

    #cv2.putText(frame, "Calc - " + str(mathpart(l)), (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    #time.sleep(1)
    #cv2.imshow('img', frame)

#create_data_set()
#train()
test()
