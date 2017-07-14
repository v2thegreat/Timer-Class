import threading,time

class timer(object):
	"""docstring for timer"""
	def __init__(self, seconds=0, minutes=0, hours=0, time_in_seconds = -1):

		self.Completed = False

		if time_in_seconds == -1:
			self.hours = hours
			self.minutes = minutes
			self.seconds = seconds
		
		else:
			self.time_in_seconds = time_in_seconds
			self.hours = self.time_in_seconds//(60**2)
			self.minutes = self.time_in_seconds//(60**1)
			self.seconds = self.time_in_seconds - (self.hours*(60**2) + self.minutes*(60**1))
		
		print(self)

	def start(self):
		threading.Thread(target = self.countdown,args = ()).start()

	def countdown(self):
		while True:
			time.sleep(1)
			self.seconds -= 1

			if self.seconds < 0:
				self.seconds = 59
				self.minutes -=1

				if self.minutes < 0:
					self.minutes = 59
					self.hours -= 1
			if self.seconds == 0 and self.minutes == 0 and self.seconds == 0:
			  self.Completed = True
			  break
		print(self.Completed)

	def time_remaining(get_time_in_seconds=True):
		if get_time_in_seconds:
			return self.seconds + self.minutes*60 + self.hours*(60**2)
		else:
			return ( self.seconds , self.minutes , self.hours )

	def __str__(self):
		return str(self.hours)+" "+str(self.minutes)+" "+str(self.seconds)

t = timer(time_in_seconds = 120)
t.start()