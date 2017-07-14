import threading,time

cdef class timer:

	cdef int hours , minutes , seconds , time_in_seconds
	cdef object Completed

	def __init__(self, int seconds = 0, int minutes = 0, int hours = 0 , int time_in_seconds = -1 ):

		if time_in_seconds == -1:
			self.hours = hours
			self.minutes = minutes
			self.seconds = seconds

		else:
			self.time_in_seconds = time_in_seconds

	def start(self):
		threading.Thread(target = self.countdown , args = ()).start()

	def countdown(self):
		while True:
			time.sleep(1)
			self.seconds -=1

			if self.seconds < 0:
				self.seconds = 59
				self.minutes -=1
				if self.minutes <0:
					self.minutes = 59
					self.hours -=1
			if self.seconds == 0 and self.minutes == 0 and self.seconds == 0:
				self.Completed = True
				break
		print(self.Completed)

	def __str__(self):
		return str(self.hours)+" "+str(self.minutes)+" "+str(self.seconds)

if __name__ == '__main__':
	t = timer ( time_in_seconds = 120 )
	t.countdown()