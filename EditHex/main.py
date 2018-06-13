from action import *
import sys
import getopt

ACTIONS = ["create", "delete", "insert", "modify", "search"]

########################
#        usage         #
########################
def usage():
	print >>sys.stderr, "[-] hex_edit.py -[h] [-a Action] [-f file_name] [-d data] [-F] [-D] [-o offset(n)]"
	sys.exit(0)

########################
#    for store info    #
########################
def parse_range(range):
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

#########################
#    Action Interface   #
#########################
def do_action(action_info):
	print "[+] debug data"
	print action_info

	if action_info['action'] == "create":
		action_create(action_info['data'], action_info['file'])
	elif action_info['action'] == "delete":
		action_delete(action_info['data'], action_info['file'], action_info['start'], action_info['end'])
	elif action_info['action'] == "insert":
		action_insert(action_info['data'], action_info['file'], action_info['offset'])
	elif action_info['action'] == "modify":
		action_modify(action_info['data'], action_info['file'], action_info['offset'])
	elif action_info['action'] == "search":
		action_search(action_info['data'], action_info['file'])
	else:
		global ACTIONS
		print >>sys.stderr, "[-] Bad Action"
		print >>sys.stderr, ACTIONS

#########################
#        main           #
#########################
def edit_hex(argv=None):
	if argv is None:
		argv = sys.argv

	try:
		opts, args = getopt.getopt(argv[1:],
			"a:Dd:Ff:hOo:",
			["action=", "data=", "file=", "help", "offset="])
	except getopt.GetoptError as err:
		print str(err)
		usage()

	global ACTIONS
	action_info = {}
	for opt, value in opts:
		if opt in ['-a', '--action']:
			if value.lower() not in ACTIONS:
				print >>sys.stderr, "[-] Error bad action"
				print >>sys.stderr, ACTIONS
				usage()
			action_info['action'] = value.lower()
		elif opt in ['-F']:
			action_info['file'] = None
		elif opt in ['-f', '--file']:
			action_info['file'] = value
		elif opt in ['-D']:
			action_info['data'] = None
		elif opt in ['-d', '--data']:
			action_info['data'] = value
		elif opt in ['-O']:
			action_info['data'] = None
		elif opt in ['-o', '--offset']:
			if value.fine('-') == -1:
				action_info['offset'] = int(value)
			else:
				start, end = parse_range(value)
				if start == None or end == None: usage()
				action_info['range_start'] = start
				action_info['range_end'] = end
		elif opt in ['-h', '--help']:
			print "[+] Help"
			usage()
		else:
			print >>sys.stderr, "[-] bad opt"
			usage()

	do_action(action_info)

if __name__ == '__main__':
	edit_hex()

