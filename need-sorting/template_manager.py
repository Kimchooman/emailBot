import smtplib
import csv
import os

class Message:
	"""
		Description:
		- Creates an object with attributes representing various stages
		  of form completion

		Use:
		- Message(msg.txt, "^", clients.csv)

		Parameters:
		- template_file --> a text file directory with the desired email msg with 'insertion_marker's placed to denote where filler fields from the csv should go
		- insertion_marker --> a marker of type string, that denotes where a field from csv, limited to a single char length
		- filler_csv --> a csv file directory with first row respresenting the labels of proceeding data

		Attributes:
		- 
	"""
	def __init__(self, template_file, insertion_marker, filler_csv):
		
		self.template_dir = template_file
		self.insertion_marker = insertion_marker
		self.filler_csv_dir = filler_csv

		# Directory Checks for template text file
		if os.path.exists(self.template_dir):
			with open(self.template_dir, "r") as text_file:
				self.template_file = ""

				for line in text_file:
					self.template_file += line

		else:
			raise NameError("Template file {} does not exist".format(self.template_dir))
		
		# Directory Checks for filler csv file
		if os.path.exists(self.filler_csv_dir):
			with open(self.filler_csv_dir, "r") as csv_file:
				self.client_fields = []
				for row in csv.reader(csv_file):
					self.client_fields.append(row)
		else:
			raise NameError("CSV file {} does not exist".format(self.filler_csv_dir))


		# Checking if the numbers of insertions available match the fields provided in text file, and csv file respectively.
		self.insert_marker_count = 0

		for line in self.template_file:
			for char in line:
				if char == self.insertion_marker:
					self.insert_marker_count += 1
			
			# Note len(self.csv_file[0]) is subracted by 1 for a row of the clients email
		if len(self.client_fields[0])-1 != self.insert_marker_count:
			raise ValueError("Number of \"{}\" markers does not align with number of insertable fields from \"{}\"".format(self.insertion_marker, self.filler_csv_dir))
		
		# IF PROGRAM REACHED THIS POINT, AN EMAIL CAN BE PRODUCED, AND CHECKED BY USER TO ENSURE PROPER MESSAGES ARE SENT.

		self.checked_by_user = False

		self.test_msg = self.generate_single_message(1)
		
		print(self.test_msg)
		
	def generate_single_message(self, recipient_row):

		example_msg = ""

		target_info = self.client_fields[recipient_row]

		current_c = 0

		for line in self.template_file:
			for char in line:
				if char != self.insertion_marker:
					example_msg += char

				else:
					example_msg += target_info[current_c]
					current_c += 1
		
		return example_msg