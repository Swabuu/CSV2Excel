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
	with open(file, 'r') as file_object:
		# Create the new excel workbook as well as a worksheet
		workbook = xlsxwriter.Workbook(file.replace('.csv', '.xlsx'))
		worksheet = workbook.add_worksheet('Full Price List')

		# Loop over every row/line in the .CSV and generate an index
		for index, line in enumerate(file_object):

			# Split on comma
			line = line.split(SEPERATOR)

			for column in range(COLUMNS):
				worksheet.write_string(index, column, line[column])