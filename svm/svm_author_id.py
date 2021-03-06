#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
reduce_training_set = False

# Use 1% of training set to trading off accuracy for speed
if reduce_training_set:
    features_train = features_train[:len(features_train)/100]
    labels_train = labels_train[:len(labels_train)/100]

from sklearn.svm import SVC

#for c_val in [1, 10, 100, 1000, 10000]:
c_val = 10000
t0 = time()
cls = SVC(kernel='rbf', C=c_val )
cls.fit(features_train, labels_train)
print("training time:", round(time() - t0, 3), "s")

t1 = time()
pred = cls.predict(features_test)
print('prediction time:', round(time() - t1, 3), "s")

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(labels_test, pred)
print("c=", c_val, "accuracy=", accuracy)

for p in [10, 26, 50]:
    print("Element %d is %d" % (p, pred[p]))

pred_as_chris = reduce(lambda x, y: x + y, filter(lambda x: x == 1, pred), 0)
print("%d of test are predicted as Chris" % pred_as_chris)
#########################################################
