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
print len(enron_data) #check number of entries/people
print len(enron_data["SKILLING JEFFREY K"]) #check number of features for each person/entry

i = 0 #this is a counter.It will count the POIs in our data.
for person in enron_data:
	if enron_data[person]['poi'] == True:
		i = i+1 #counter will increase for each POI
print i


#print information on James Prentice
print enron_data["PRENTICE JAMES"]["total_stock_value"] 
#print information on Wesley Colwell
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"] 
#print information on Jeffrey K. Skilling
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"] 

#Who took home the most money?How much money did that person get?

p1 = "SKILLING JEFFREY K"
p2 = "LAY KENNETH L"
p3 = "FASTOW ANDREW S"

#the following constructs a string that contains the answer
if enron_data[p1]["total_payments"] > enron_data[p2]["total_payments"] and enron_data[p1]["total_payments"] > enron_data[p3]["total_payments"]:
	s = p1+'got'+str(enron_data[p1]["total_payments"])
elif enron_data[p2]["total_payments"] > enron_data[p3]["total_payments"]:
	s = p2+" got "+str(enron_data[p2]["total_payments"])
else:
	s = p3+" got "+str(enron_data[p3]["total_payments"])
print s

