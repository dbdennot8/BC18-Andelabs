def data_type(data):


	if isinstance(data, str):
		return data

	elif isinstance(data, dict):
		return data

	elif isinstance(data, bool):
		return data

	elif isinstance(data, int):
		if data < 100:
			return "less than 100"
		elif data > 100:
			return "more than 100"
		elif data == 100:
			return "equal to 100"

	elif isinstance(data, list):
		if len(data) >= 3:
			return data.pop(2)
		elif len(data) < 3:
			return "None"

	elif len(str(data)) == 0:
		return "no value"

	else:
		return "Please try again"

print 
print		

print data_type(True)
print data_type("True")
print data_type(0)
print data_type([1,2,3])
print data_type(50)
print data_type(140)
print data_type(100)

print
print
