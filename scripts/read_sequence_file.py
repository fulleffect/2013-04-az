import sys
import screed

filename = sys.argv[1]
#sequences = {}
counter = 0 

for record in screed.open(filename):
	counter += 1
	sequence = record['sequence']
	print sequence
	if counter > 10:
		break

#	if count >9:
#		break
#	count += 1

print record

#for line in filename:
#	line_list = line.strip().split(',')
#	seq = line_list[1]
#	data = line_list[1:]
#	sequences[atgc]=data
#print seq

#for record in screed.open(filename):
#	sequences[]=data
#	if count >9:
#		break
#	count += 1
#	print record

