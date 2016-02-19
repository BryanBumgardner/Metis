import csv
import dateutil.parser
from datetime import *
from collections import defaultdict

# data = defaultdict(list)
reader = csv.reader(open('turnshort.csv'), delimiter=',')
next(reader, None)

data['key'] = zip(data["C/A"], data['UNIT'], data['SCP'], data['STATION'])

for index, row in data.iterrows():
	value = row['datetime'], row['ENTRIES']
	key = row['key']

	if key in datetime_dict:
		datetime_dict[key].append(value)

	else:
		datetime_dict[key] = [value]

def days(my_list):
	dates = [row[0].date() for row in my_list]
	dates = set(dates)

	result = []
	for date in dates:
		entries = [x[1] for x in my_list if x[0].date () == date]
		result.append((date, max(entries)-min(entries)))

	return result

count_dict = {ket:day(datetime_dict[key]) for key in datetime_dict}
pprint.pprint(count_dict, width = 100)