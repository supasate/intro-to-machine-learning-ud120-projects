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

poi_list = []
for name, features_dict in enron_data.items():
    if features_dict["poi"] == 1:
        poi_list.append(name)
print("number of poi", len(poi_list))

# Show name list
#print(enron_data.keys())

# Show feature list
print(enron_data["PRENTICE JAMES"].keys())

# Show total stock value of James Prentice
print(enron_data["PRENTICE JAMES"]["total_stock_value"])

# Show total number of emails from Weslet Colwell to person of interest
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

# Show the value of stock options exercised by Jeffrey Skilling
print("the value of stock options exercised by Jeffrey Skilling",
    enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

# Show total payment of Lay Kennth, Jeffrey Skilling, and Andrew Fastow
print("Total payment")
print("Lay Kennth", enron_data["LAY KENNETH L"]["total_payments"])
print("Jeffrey Skilling", enron_data["SKILLING JEFFREY K"]["total_payments"])
print("Andrew Fastow", enron_data["FASTOW ANDREW S"]["total_payments"])
