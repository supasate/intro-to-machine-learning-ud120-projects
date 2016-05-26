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
print("features list", enron_data["PRENTICE JAMES"].keys())

# Show total stock value of James Prentice
print("total stock value fo James Prentice", enron_data["PRENTICE JAMES"]["total_stock_value"])

# Show total number of emails from Weslet Colwell to person of interest
print("total number of emails from Weslet Colwell to poi", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

# Show the value of stock options exercised by Jeffrey Skilling
print("the value of stock options exercised by Jeffrey Skilling",
    enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

# Show total payment of Lay Kennth, Jeffrey Skilling, and Andrew Fastow
print("Total payment")
print("Lay Kennth", enron_data["LAY KENNETH L"]["total_payments"])
print("Jeffrey Skilling", enron_data["SKILLING JEFFREY K"]["total_payments"])
print("Andrew Fastow", enron_data["FASTOW ANDREW S"]["total_payments"])

# Show features and values to detect NaN values
num_quantified_salary = 0
num_known_email = 0
num_unknown_total_payment = 0
num_poi_with_unknown_total_payment = 0
for name, features_dict in enron_data.items():
    #print(name)
    for feature, value in features_dict.items():
        #print(feature, value)
        if feature == "salary" and value != "NaN":
            num_quantified_salary += 1
        if feature == "email_address" and value != "NaN":
            num_known_email += 1
        if feature == "total_payments" and value == "NaN":
            num_unknown_total_payment += 1
            if enron_data[name]["poi"] == 1:
                num_poi_with_unknown_total_payment += 1


# Show a number of quantified salary and known email addresses
print("number of quantified salary", num_quantified_salary)
print("number of known emails", num_known_email)

# Show a number of unknown total payments and percentage
print("number of unknown total payments", num_unknown_total_payment)
print("percentage of unknown total payments", float(num_unknown_total_payment) / len(enron_data))

# Show a number of poi with unknown total pyament and percentage
print("number of pois with unknown total payments", num_poi_with_unknown_total_payment)
print("percentage of pois with unknown total payments", float(num_poi_with_unknown_total_payment) / len(enron_data))

# Show a number of new pois with unknown total payment after adding new 10 pois
print("number of new pois", len(poi_list) + 10)
print("number of new pois with unknown total payment", num_poi_with_unknown_total_payment + 10)
print("percentage of new pois with unknown total payments", float(num_poi_with_unknown_total_payment + 10) / (len(enron_data) + 10))
