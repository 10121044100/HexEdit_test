from EditHex.action import *
from EditHex.file import *
import sys
import getopt

def usage():
	print >>sys.stderr, "[-] hex_edit.py -[h|a [Action]] -f [file_name] -d [data] -[o [offset(n)]|r [range(0-n)]]"
	print >>sys.stderr, "                -a : Action"
	print >>sys.stderr, "                -d : Data for actions except 'delete' action"
	print >>sys.stderr, "                -f : The target file's name"
	print >>sys.stderr, "                -h : Help"
	print >>sys.stderr, "                -o : Offset for actions except 'delete' action"
	print >>sys.stderr, "                -r : Range for delete, ex) 1-100"
	sys.exit(1)

def main():
	argv = sys.argv
	if not argv:
		print >>sys.stderr, "[-] bad argument, need to check argument"
		usage()

	try:
		opts, args = getopt.getopt(argv[1:],
			"a:d:f:ho:r:",
			["action=", "data=", "file=", "help", "offset=", "range="])
	except getopt.GetoptError as err:
		print str(err)
		usage()

	action_list = ["create", "delete", "insert", "modify"]
	action_info = {}
	for flag, value in opts:
		if flag in ['-a', '--action']:
			if value.lower() not in action_list:
				print >>sys.stderr, "[-] bad action error, need to check a action argument"
				usage()
			action_info['action'] = value.lower()
		elif flag in ['-f', '--file']:
			action_info['file'] = value
		elif flag in ['-d', '--data']:
			action_info['data'] = value
		elif flag in ['-o', '--offset']:
			action_info['offset'] = int(value)
		elif flag in ['-r', '--range']:
			start, end = check_range(value)
			if start == None or end == None: usage()
			action_info['range_start'] = start
			action_info['range_end'] = end
		elif flag in ['-h', '--help']:
			print "[+] Help"
			usage()
		else:
			print >>sys.stderr, "[-] bad flag"
			usage()

	action_info = check_info(action_info)
	if not action_info: usage()
	edit_hex(action_info)

if __name__ == '__main__':
	main()

