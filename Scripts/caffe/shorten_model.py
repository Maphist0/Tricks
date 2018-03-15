with open('ResNet-50-deploy.prototxt', 'r') as ifile:
	lines = ifile.readlines()

level = 0
with open('ResNet-50-shorten.prototxt', 'w') as ofile:
	for line in lines:
		if '{' in line:
			level += 1
		elif '}' in line:
			level -= 1
		else:
			pass
		if level == 0:
			if line.strip():
				ofile.write(line)
		else:
			ofile.write(line.strip() + ' ')
