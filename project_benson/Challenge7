#Challenge 7
%matplotlib inline
import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import pprint
import datetime

data1 = pd.read_csv("turnshort.csv", header=0)
data2 = 

def ex_fnn(data):
    #Check this new dictionary
    data['key'] = list(zip(data['STATION']))
    #print(list(zip(data["C/A"], data['UNIT'], data['SCP'], data['STATION'])))
    data_dict = {}

    data['datetime'] = pd.to_datetime(data.DATE + data.TIME, format='%m/%d/%Y%H:%M:%S')
    datetime_dict = {}

    for index, row in data.iterrows():
        value = row['datetime'], row['ENTRIES']
        key = row['key']

        if key in datetime_dict:
            datetime_dict[key].append(value)

        else:
            datetime_dict[key] = [value]

    return(datetime_dict)

data1 = pd.read_csv("turnshort.csv", header=0)
data2 = 
#ex

def next_fun(data):
    count_dict = {key:CountEachDay(datetime_dict[key]) for key in datetime_dict}
    #pprint.pprint(count_dict, width = 100)
    return count_dict

def run(data):
    #runs all code
    datetime_dict1 = ex_fnn(data)
    count_dict = next_fun(datetime_dict1)

    
def CountEachDay(my_list):
	dates = [row[0].date() for row in my_list]
	dates = set(dates)

    # make this a dict?
	result = []
	for date in dates:
		entries = [x[1] for x in my_list if x[0].date () == date]
		result.append((date, max(entries)-min(entries)))

	return result

count_dict = {key:CountEachDay(datetime_dict[key]) for key in datetime_dict}
#pprint.pprint(count_dict, width = 100)

def plot_turnstile(dictionary, turnstile_key):
    turnstile_data = sorted(dictionary[turnstile_key])
    
    dates = [x[0] for x in turnstile_data]
    counts = [x[1] for x in turnstile_data]

    plt.figure(figsize=(10,5))
    plt.plot(dates, counts)
    
key = ('5 AV/59 ST',)
# Demonstrate
plot_turnstile(count_dict, key)

key = ('59 ST',)
# Demonstrate
plot_turnstile(count_dict, key)



count_dict1 = run(data1)
for key in count_dict1.keys():
    # Demonstrate
    plot_turnstile(count_dict1, key)