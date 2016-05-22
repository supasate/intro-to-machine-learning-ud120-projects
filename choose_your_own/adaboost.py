#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary

################################### AdaBoost ###################################
from sklearn.ensemble import AdaBoostClassifier
from time import time

print("AdaBoost")
best_accuracy = 0
best_num_estimators = -1
best_learning_rate = -1
for num_estimators in range(5,100):
    for rate in range(1, 11):
        rate = rate * 0.1
        print("n_estimators", num_estimators)
        print("learning_rate", rate)
        t0 = time()
        clf = AdaBoostClassifier(n_estimators = num_estimators, learning_rate = rate)
        clf.fit(features_train, labels_train)
        print("training time", round(time() - t0, 3), "s")

        t1 = time()
        pred = clf.predict(features_test)
        print("prediction time", round(time() - t1, 3), "s")

        from sklearn.metrics import accuracy_score
        accuracy = accuracy_score(labels_test, pred)
        print("accuracy", accuracy)
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_num_estimators = num_estimators
            best_learning_rate = rate * 0.1
print("best accuracy", best_accuracy)
print("best num_estimators", num_estimators)
print("best learning rate", best_learning_rate)
################################################################################

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
