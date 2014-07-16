
import time
import random
import os.path
import pkgutil
import cmdClass
import commands

import sys
noreply = ''

#function to load in all "commands"
def load_commands(cmd_pack_name):
	cmd_pack = sys.modules[cmd_pack_name]
	cmds = []
	for _, cmdMod, _ in pkgutil.iter_modules([os.path.dirname(cmd_pack.__file__)]):
		cmdMod = cmd_pack_name + "." + cmdMod
		__import__(cmdMod)
		cmds += sys.modules[cmdMod].commands() #returns all commands that the module defines
	return cmds #

def get_command(name, cmdList):
	for cmd in cmdList:
		if name.lower().startswith(cmd.name.lower() + " ") or name.lower() == cmd.name.lower():
			return cmd
	return UnknownCmd()

class UnknownCmd(cmdClass.DukeOSCmd):
	def execute(self, args):
		print 'processing'
		time.sleep(10)
		print('compiling result')
		time.sleep(10)
		print 'outputing result'
		time.sleep(10)
		print 'result = dirt'
		return 0

class HelpCmd(cmdClass.DukeOSCmd):
	name = "help"
	dscp = "brings up the help menu"

	def __init__(self, cmdList):
		self.cmdList = cmdList

	def execute(self, args):
		print "Welcome to the debut of DUKEOS, here are some helpful commands"

		for cmd in self.cmdList:
			print cmd.name + ": " + cmd.dscp

def logo():
#The DukeOS logo
	print '  _____  _    _ _  ________    ____   _____ '
	print ' |  __ \| |  | | |/ /  ____|  / __ \ / ____|'
	print ' | |  | | |  | | \' /| |__    | |  | | (___  '
	print ' | |  | | |  | |  < |  __|   | |  | |\___ \ '
	print ' | |__| | |__| | . \| |____  | |__| |____)|'
	print ' |_____/ \____/|_|\_\______|  \____/|_____/ '
	print '                                            '
	print '           Type help for help               '


class DukeOS():
	def __init__(self):
		self.cmds = load_commands("commands")
		self.cmds.append(HelpCmd(self.cmds))

	def mainLoop(self):
		logo()
		while True:
			command = raw_input('>>> ')
			command = command.lower()
			#DukeOS help menu

			cmdObj = get_command(command, self.cmds)
			x = cmdObj.execute(command.split()[1:])

			if x == "exit":
				print "DUKE OS has been quit by command.  We will delete system_32 on our way out if thats OK. " + cmdObj.name
				raw_input("Do you want us to delete system_32?: ")
				print "Deleting system_32..."
			
				
				sys.exit()

OS = DukeOS()
OS.mainLoop()