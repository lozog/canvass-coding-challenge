import csv

# key for sorting by date
def datesortkey(L):
	split = L.split('/')

	# returned in this order (2, 0, 1) because the dates are of the format MM/DD/YYYY
	return int(split[2]),int(split[0]),int(split[1]) 

with open('random_data.csv') as csvfile:
	readCSV = csv.DictReader(csvfile, delimiter=',')

	# sort by Device_ID, then by Date
	sortedlist = sorted(readCSV, key=lambda row: (row['Device_ID'], datesortkey(row['Date'])), reverse=False)

fieldnames = ['Device_ID', 'A', 'B', 'C', 'D', 'Date'] # hard-coded field names
with open('random_data_sorted.csv', 'w') as f:
	writer = csv.DictWriter(f, fieldnames=fieldnames)
	writer.writeheader()
	for row in sortedlist:
		writer.writerow(row)