from portfolio.models import *
import csv
with open('Facebook.csv') as f:
	reader = csv.reader(f,delimiter=',')
	for row in reader:
		newnumber = ''
		for o in row[1]:
			if o != ',':
				newnumber+=o
		Facebook.objects.create(x=row[0][0:10],y=float(newnumber))



