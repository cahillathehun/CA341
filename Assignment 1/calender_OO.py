


week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
class Appointment(object):
	"""Appointment class is object defining the actual appointments,
	is has a day, start time and end time and is stored in the calender class,
	One is instatiated every time an appointment is added to the calender."""
	def __init__(self, day, sTime, fTime):
		self.day = day
		self.sTime = sTime
		self.fTime = fTime

	def __str__(self):
		return "Appointment on {} at {} until {}".format(self.day, self.sTime, self.fTime)


class Calender(Appointment):
	""" Calender class is an object storing a list of appointments,
	each of the methods definded beloew operate on the calender object.
	Only one of these is instatiated in the main.(could have many)"""
	def __init__(self, d=[]):
		self.d = d

	def __str__(self):			#like show() in imperative imlementation (calender_imp.py)
		if self.d:
			top = "List of booked appointments\n-----------\n"
			for i in self.d:
				for j in i:
					top += j.day + " " + j.sTime + " - " + j.fTime + "\n"

			return top.strip()
		else:
			return "No appointments booked!\n Press 'a' at the start to add an appointment \n"

	def add(self, appt):
		if not str(appt.day) in week:
			print("{} is not a valid day.\nPlease enter a valid day(Mon-Sun)".format(appt.day))
			return
		else:
			print("ADDING")
			if not int(appt.sTime) or not int(appt.fTime) in range(0,24) or int(appt.sTime) > int(appt.fTime):
				print("Please enter a valid time in the range 0-24")
				return
			else:
				if not self.d[week.index(appt.day)]:
					self.d[week.index(appt.day)].append(appt)
					print("Appointment booked for {} from {} to {}".format(appt.day, appt.sTime, appt.fTime))
					return
				else:
					for i in self.d[week.index(appt.day)]:
						if int(appt.sTime) in range(int(i.sTime),int(i.fTime)) or int(appt.fTime) in range(int(i.sTime),int(i.fTime)):
							print("Overlapping appointments, use 's' to see appointments already booked.")
							return

					self.d[week.index(appt.day)].append(appt)
					print("Appointment booked for {} from {} to {}".format(appt.day, appt.sTime, appt.fTime))
					return

	def remove(self):
		day = input("Please input a day:\n")
		if self.d[week.index(day)]:
			appt_num = 1
			for i in  self.d[week.index(day)]:
				print(appt_num, " - ", i)
				appt_num += 1
			n = int(input("Please enter the number of the appointment to remove:\n")) - 1
			del self.d[week.index(day)][n]
			print("Appointment removed!")
			return
		else:
			print("No appointments booked for this day.")
			return





def main():
	global week
	Mon = []
	Tue = []
	Wed = []
	Thu = []
	Fri = []
	Sat = []
	Sun = []
	days = [Mon, Tue, Wed, Thu, Fri, Sat, Sun]
	cal = Calender(days)
	#print(cal)
	cmd = ""
	while cmd != "q":
		cmd = str(input("Commands are 'q' to quit, 'a' to add an appointment, 'r' to remove an appointment and 's' to show appointments.\n"))
		if cmd == "a":
			day = input("Please enter the day:\n")
			sTime = input("Please enter the start time:\n")
			fTime = input("Please enter the end time:\n")
			appt = Appointment(day, sTime, fTime)
			#print(appt)
			#print(appt.day)
			cal.add(appt)
		if cmd == "r":
			cal.remove()
		if cmd == "s":
			print(cal)
	print("Quitting!")



if __name__ == "__main__":
	print("Welcome to calender!")
	main()









#15321711 - Alexander Cahill
