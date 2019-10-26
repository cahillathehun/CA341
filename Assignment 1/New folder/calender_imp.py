

"""
implenting the appointments using lists and tuples.
days is a list of all days in the week.
each of the days in the week is a list of tuples.
each of the tuples in a day contains the start time of the appointment @ pos 0 and the end time @ pos 1.

as a result of this times cannot be changed unless they are removed and the desired edited time is added

the time works off the 24 hr clock.

eg an appointment booked for 5pm until 7 pm on a Friday
   an appointment booked for 3am until 4 am on a Tuesday
   and an appointment booked for 10am until 1pm on a Tuesday

Tue = [(3,4),(10,13)]
Fri = [(17,19)]

"""

Mon = []
Tue = []
Wed = []
Thu = []
Fri = []
Sat = []
Sun = []
days = [Mon, Tue, Wed, Thu, Fri, Sat, Sun]
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]	#just using this for str representation of the days due to bugginess
															#only used in show()

def add_appt():
	#Function for adding appointments to the calender
	while True:
		print("Please enter a day:")
		day = input()
		if not day in days:																#checks if day entered is valid
			print("please enter a valid day(Mon-Sun)")
		else:
			print("Please enter the start time(0-24):")
			start = input()
			print("Please enter the end time(0-24):")
			end = input()
			if not start in range(0,24) or not end in range(0,24) or end < start:		#checks if times are valid
				print("Please enter a valid time in range (0-24)")
			else:
				if not day:
					day.append(tuple((start,end)))										#adds the appointment
					print("Appointment booked!")
					print("press enter to continue")
					break
				else:
					for i in day:
						#print(i)
						if start in range(i[0],i[1]) or end in range(i[0],i[1]):		#checks appointment does not overlap with another appointment
							print("Overlapping appointments")
							break

					day.append(tuple((start,end)))
					print("Appointment booked!")
					print("press enter to continue")
					break
			break

def remove_appt():
	#Function for removing appointments
	while True:
		print("enter the day of the appointment to be removed.")
		day = input()
		if not day in days:																#checks if day entered is valid
			print("please enter a valid day(Mon-Sun)")
		elif not day:
			print("No appointments on this day.")
		else:
			print("Choose the number of the appointment to remove:")
			for i in day:
				print(i)
			n = input()
			day.pop(n-1)																#removes the appointment
			print("Appointment removed!")
			print("Press enter to continue.")
			break

def show():
	#Function for displaying all booked appointments
	i = 0
	j = 0
	while i < len(days):
		if not days[i]:	#checks if a day has an appointment pythonically
			i+=1
		else:
			while j < len(days[i]):
				print "Appointment booked on", week[i], "from", days[i][j][0], "until", days[i][j][1], "."
				j+=1
			j = 0
			i+=1
	print("Press enter to continue.")

def main():
	#main
	cmd = ""

	while cmd != "q":
		print "Commands are: 'q'to quit, 'a' to add an appointment, 's' to show appointments and 'r' to remove an appointment."
		cmd = raw_input()	#using raw_input() because of python 2.7
		if str(cmd) == "a":
			add_appt()
		elif str(cmd) == "s":
			show()
		elif str(cmd) == "r":
			remove_appt()
		else:
			print "Valid commands are: 'q' to quit, 'a' to add an appointment, 's' to show appointments and 'r' to remove an appointment"
		cmd = raw_input()


if __name__ == "__main__":
	print("Welcome to the calender!")
	main()
