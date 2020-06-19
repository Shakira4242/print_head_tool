from printer import connect

# 	datapoints = []
# 	time = []

# initializes the robot 
class ToolHead():
	def __init__(self, url, apikey):
		self.client = connect(url, apikey)
		self.position = {"x": 0, "y":0, "z": 0}

	# Commands printerHead to go to assigned position 
	# at the x,y,z
	def move_to(self, x, y, z):
		self.client.jog(x = x,y = y, z = z)
		self.position = {"x": x, "y":y, "z": z}
		
	# returns the current position of the printer head 
	# in the form of a dictionary 
	def get_pos(self):
		return self.position

	# Commands printerHead to go to home 
	# a pre assigned x,y,z coordinate 
	def home(self): 
		self.client.home()


a = ToolHead("http://192.168.1.118:5000", "7AA24AC7430A43ABAEA065C83458270C")










