#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print("number of people", len(enron_data))
print("number of features", len(enron_data["SKILLING JEFFREY K"]))

num_person_of_interest = 0
for name, features_dict in enron_data.items():
    if features_dict["poi"] == 1:
        num_person_of_interest += 1
print("number of poi", num_person_of_interest)

# Show name list
#print(enron_data.keys())

# Show total stock value of James Prentice
print(enron_data["PRENTICE JAMES"]["total_stock_value"])
