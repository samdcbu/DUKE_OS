class DukeOSCmd():
	def __init__(self):
		self.name = "" #the string used to execute the command

	#args is a tuple of arguments e.g. if "">>> sample a b c" is typed in then args = (a, b, c)
	def execute(self, args):
		return 0 #defined by subclass. Should return != 0 if error.

#example subclass of DukeOSCmd
#would work like this:
#>>> example a bbb c
#this is an example command. Here are the arguments passed: ("a", "bbb", "c")
#>>> example self_detonate other stuff
#CommandError: command returned other than 0 (DukeOS will have handling for this.)
class SampleCmd(DukeOSCmd):
	def __init__(self):
		self.name = "example"

	def execute(self, args):
		if args and args[0] = "self_detonate":
			return "DukeOS has self-detonated." #execute didn't finish successfully, return error message
		print "this is an example command. Here are the arguments passed: ", args
		return 0 #executed successfully