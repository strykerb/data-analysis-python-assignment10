import numpy as np

import matplotlib

import matplotlib.pyplot as plt

import pymongo

from pymongo import MongoClient

x = np.linspace(0,10,11)

y = x**2

print(x)


print(y)

figure, axis = plt.subplots(1, 1)

axis.plot(x, y)

figure.savefig("x_squared.svg")

db = MongoClient("mongodb://mongo0.scitecha.com,mongo1.scitecha.com,mongo2.mrocha.org/mrocha?replicaSet=rs0").mrocha 

user_data = list(db.users.find({}, {"profile.Robux": 1})) # This is the query requesting the Robux data from the users collection

robux = [user["profile"]["Robux"] for user in user_data]

figure, axis = plt.subplots(1, 1) # This create a figure with 1 axis

axis.hist(robux, bins=10) # This draws a histogream with 10 bins


figure.savefig('robux_histogram.svg')