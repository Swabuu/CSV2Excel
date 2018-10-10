"""
1. Import standard library OS to access the current directory
2. Import xlsxwriter to easily write excel files
"""
import os
import xlsxwriter

# Generator object of all .CSV files (in case of several products at once)
INPUT_FILES = [file for file in os.listdir() if file.endswith('.csv')]

# The number of columns as well as the seperator/delimiter
COLUMNS = 5
SEPERATOR = ','

# Re-write each .CSV file into an excel file
for file in INPUT_FILES:
	# Create a workbook and add a worksheet.
	workbook = xlsxwriter.Workbook(file.replace('.csv', '.xlsx'))
	worksheet = workbook.add_worksheet('Full Price List')
	
	# Loop over every row/line in the .CSV and generate an index
	with open(file, 'r') as file_object:
		reader = csv.reader(file_object, SETUP)
		
		# Get the header names
		header = next(reader)
		# Write the header
		[worksheet.write_string(0, index, line) for index, line in enumerate(header)]
		
		# Write the rest with offset of header
		for index, line in enumerate(reader, 1):
			[worksheet.write(index, column, line[column]) for column in range(len(header))]
