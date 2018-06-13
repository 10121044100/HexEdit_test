from file import *

def action_create(data=None, file=None):
	if file is None:
		print data
	else:
		write_file(file, data, False)

def action_delete(data=None, file=None, start=0, end=0):
	if start > end:
		print "[-] need to exchang start and end"
		return False

	if data is not None:
		if len(data) < start:
			print "[-] data length error...."
			return False

		front = data[:start]
		back = data[end:]

		data = front + back
		if file is None:
			print data
		else:
			write_file(file, data, False)

		return True

	if file is not None:
		data = read_file(file)
		if len(data) < start:
			print "[-] data length error...."
			return False

		front = data[:start]
		back = data[end:]

		data = front + back
		write_file(file, data, True)

		return True

def action_insert(data=None, file=None, offset=0):
	if file is None:
		print "[-] error...."

		return False
	else:
		file_data = read_file(file)
		if len(file_data) < offset:
			print "[-] data length error...."
			return False

		front = file_data[:offset]
		back = file_data[offset:]

		new_data = front + data + back
		write_file(file, new_data, True)

		return True

def action_modify(data=None, file=None, offset=0):
	if file is None:
		print "[-] error...."
	else:
		file_data = read_file(file)
		if len(file_data) < offset:
			print "[-] data length error...."
			return False

		front = file_data[:offset]
		back = file_data[offset+len(data):]

		new_data = front + data + back
		write_file(file, new_data, True)

def action_search(data=None, file=None):
	if file is None:
		print "[-] error...."
	else:
		file_data = read_file(file)

		while Ture:
			tmp = file_data

			offset = file_data.find(data)
			if offset == -1:
				break

			print "[+] offset : " + hex(offset)
