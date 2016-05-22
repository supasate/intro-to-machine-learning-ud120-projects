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

############################# K-Nearest Neighbors #############################
from sklearn.neighbors import KNeighborsClassifier
from time import time

print("K-Nearest Neighbors")
best_accuracy = 0
best_n_neighbors = -1
best_weights = ""
best_algorithm = ""
best_p = -1
for n_neighbors in range(2, 10):
    for weights in ["uniform", "distance"]:
        for algorithm in ["ball_tree", "kd_tree", "brute"]:
            for p in [1, 2]:
                t0 = time()
                clf = KNeighborsClassifier(n_neighbors = n_neighbors, weights = weights, algorithm = algorithm, p = p)
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
                    best_n_neighbors = n_neighbors
                    best_weights = weights
                    best_algorithm = algorithm
                    best_p = p

print("best accuracy", best_accuracy)
print("best n_neighbors", best_n_neighbors)
print("best weights", best_weights)
print("best algorihm", best_algorithm)
print("best p", best_p)
################################################################################

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
