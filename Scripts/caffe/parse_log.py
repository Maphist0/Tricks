import os
import numpy as np
import matplotlib.pyplot as plt

log_filename = raw_input('Input log file\'s name >>> ')
with open(log_filename, 'r') as ifile:
	lines = ifile.readlines()

print("Total {0} lines.".format(len(lines)))

loss_titles = [
	'Total loss',		#1
	'dsn2_loss',		#2
	'dsn3_loss',		#3
	'dsn4_loss',		#4
	'dsn5_loss',		#5
	'fuse_loss',		#6
	'dsn2_loss_test',	#7
	'dsn3_loss_test',	#8
	'dsn4_loss_test',	#9
	'dsn5_loss_test',	#10
	'fuse_loss_test'	#11
]

for loss_id in range(1, 11):
	curr_iter = -10 
	iter_rounds = []
	iter_pairs = []
	update_loss = False
	for line in lines:
######################################################################################################

		#Iteration 0 (0 iter/s, 3.09583s/20 iters), loss = 6687.87
		if 'Iteration' in line and 'loss' in line:
			line = line.strip()
			iter_num = float(line.split('Iteration')[1].strip().split(' ')[0])
			loss = float(line.split('loss = ')[-1].strip())
			if loss_id == 1:
					# do nothing
					update_loss = True
				
######################################################################################################

		#Train net output #0: dsn2_loss = 37292.2 (* 1 = 37292.2 loss)
		if loss_id in [2, 3, 4, 5]:
			if 'Train net output #{0}: dsn{1}_loss'.format(loss_id-2, loss_id) in line:
				line = line.strip()
				loss = float(line.split('dsn{0}_loss = '.format(loss_id))[-1].strip().split(' ')[0])
				update_loss = True

		#Train net output #4: fuse_loss = 6828.08 (* 1 = 6828.08 loss)
		if loss_id == 6:
			if 'Train net output' in line and 'fuse_loss = ' in line:
				line = line.strip()
				loss = float(line.split('fuse_loss = ')[-1].strip().split(' ')[0])
				update_loss = True
	
######################################################################################################
				
		#Iteration 1000, Testing net (#0)
		#Test net output #0: dsn2_loss = 10299.8 (* 0.5 = 5149.92 loss)
		if loss_id in [7, 8, 9, 10]:
			if 'Iteration' in line and 'Testing net' in line:
				line = line.strip()
				iter_num = float(line.split('Iteration')[1].strip().split(' ')[0][:-1])
			if 'Test net output #{0}: dsn{1}_loss'.format(loss_id-7, loss_id-5) in line:
				line = line.strip()
				loss = float(line.split('dsn{0}_loss = '.format(loss_id-5))[-1].strip().split(' ')[0])
				update_loss = True
				
		#Test net output #4: fuse_loss = 3104.3 (* 1 = 3104.3 loss)
		if loss_id == 11:
			if 'Iteration' in line and 'Testing net' in line:
				line = line.strip()
				iter_num = float(line.split('Iteration')[1].strip().split(' ')[0][:-1])
			if 'Test net output' in line and 'fuse_loss = ' in line:
				line = line.strip()
				loss = float(line.split('fuse_loss = ')[-1].strip().split(' ')[0])
				update_loss = True
				
######################################################################################################
				
		
		if update_loss:
			update_loss = False
			if iter_num > curr_iter:
				iter_pairs.append((iter_num, loss))
				curr_iter = iter_num
			else:
				iter_rounds.append(iter_pairs)
				iter_pairs = [(iter_num, loss)]
				curr_iter = -10
				
	iter_rounds.append(iter_pairs) # last list
	f = plt.figure(figsize=(20,10))
	for i in range(len(iter_rounds)):
		it = iter_rounds[i]
		x = []
		y = []
		for pair in it:
			x.append(pair[0])
			y.append(pair[1])
		plt.subplot(1, len(iter_rounds), i+1)
		plt.plot(x, y)
		plt.title(loss_titles[loss_id-1] + " phase {0}".format(i))
	f.savefig('figure-{0}.jpg'.format(loss_id))

import time
time = time.ctime().replace(' ', '-')
os.system('mkdir {0}'.format(time))
os.system('mv figure-* {0}/'.format(time))