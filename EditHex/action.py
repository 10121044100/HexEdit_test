import re
import sys

def check_range(range):
	match = re.match("^(\d+)-(\d+)$", range)
	if match:
		start = int(match.group(1))
		end = int(match.group(2))
	else:
		print >>sys.stderr, "[-] bad range data"
		return None, None

	if start > end:
		tmp = start
		start = end
		end = tmp

	return start, end

def check_info(action_info):
	try:
		if not action_info['action']:
			print >>sys.stderr, "[-] bad argument(action)"
			return None

		if not action_info['data']:
			print >>sys.stderr, "[-] bad argument(data)"
			return None
		
		if not action_info['file']:
			print >>sys.stderr, "[-] bad argument(file)"
			return None
		elif action_info['file']:
			# check path
			pass

		if not action_info['range'] and not action_info['offset']:
			print >>sys.stderr, "[-] bad arguments(range or offset)"
			return None

	except:
		print >>sys.stderr, "[-] arguments exception"
		return None

	return action_info

def edit_hex(action_info):
	print "[+] debug data"
	print action_info

	if action_info['action'] == "create":
		pass
	elif action_info['action'] == "delete":
		pass
	elif action_info['action'] == "insert":
		pass
	elif action_info['action'] == "modify":
		pass
	else:
		print >>sys.stderr, "[-] bad action error, need to check a action argument"