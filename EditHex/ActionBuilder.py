from action.create import *
from action.delete import *
from action.insert import *
from action.modify import *

class ActionBuilder(object):
	"""docstring for ActionBuilder"""
	def __init__(self, action):
		super(ActionBuilder, self).__init__()
		self.action = action

	def setaction(self, action):
		self.action = action

	def getaction(self):
		print "[+] Current action : " + self.action
		return self.action

	def build(self):
		action_list = ["create", "delete", "insert", "modify"]

		if action_info['action'] == "create":
			return CreateAction()
		elif action_info['action'] == "delete":
			return DeleteAction()
		elif action_info['action'] == "insert":
			return InsertAction()
		elif action_info['action'] == "modify":
			return ModifyAction()
		else:
			print >>sys.stderr, "[-] Error bad action, need to check a action argument"

		return None