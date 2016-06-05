#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.cross_validation import train_test_split

feature_train, feature_test, label_train, label_test = train_test_split(features, labels, test_size = 0.3, random_state = 42)

cls = DecisionTreeClassifier()
cls.fit(feature_train, label_train)
pred = cls.predict(feature_test)
print("accuracy", accuracy_score(label_test, pred))

poi_count = int(reduce(lambda x, y: x + y, filter(lambda x: x == 1, pred), 0))

print("a number of pois in test set", poi_count)
print("a number of people in test set", len(feature_test))

print("accuracy with all 0s prediction", accuracy_score(label_test, [0] * len(feature_test)))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(label_test, pred, labels=[1,0]))

print("precision", precision_score(label_test, pred))
print("recall", recall_score(label_test, pred))
