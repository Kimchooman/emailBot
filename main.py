import smtplib
import csv

class send_session:
	def __init__(self, usr, passwrd, csv_name):

		self.username = usr
		self.password = passwrd

		self.msg = "Hi, this is a message from python!"

		self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		self.server.login(username, password)

		self.csv_file_name = csv_name

		with open(self.csv_file_name) as csv_file:
    		self.csv_reader = csv.reader(csv_file, delimiter=',')
	
	def send_mail(self):
	
		"""
		This for loop format assumes that the recipient email is in the first cell of each row, and additional info follows
		"""

		for recipient_row in self.csv_reader:
			for recipient in recipient_row:
				self.server.sendmail(
				"%s", 
				"%s", 
				"%s") % (self.username, recipient,self.msg)

		self.server.quit()

usr = "test_usr"

pass_ = "test_pass"

bot = send_session(usr, pass_, "test.csv")

#bot.send_mail()
