class DukeOSCmd():
	name = "" #the string used to execute the command. Not defined in __init__ so can be accessed w/out making an instance
	dscp = "" #a description of the command used in the help menu

	def __init__(self):
		pass

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
	name = "example"
	dscp = "this is an example command"

	def execute(self, args):
		if args and args[0] == "self_detonate":
			return "DukeOS has self-detonated." #execute didn't finish successfully, return error message
		print "this is an example command. Here are the arguments passed: ", args
		return 0 #executed successfully