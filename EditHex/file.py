def read_file(file_name):
	fd = open(file_name, "r")
	data = fd.read()
	fd.close()

	return data

def write_file(file_name, data, isrewrite):
	if isrewrite:
		#unlink(file_name)
		pass

	with open(file_name) as fd:
		fd.write(data)