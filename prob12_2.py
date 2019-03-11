#!/usr/bin/env python2.7
# initiate a few variables
i = 0
x = []
y = []

# read csv file and store data in arrays x and y
import csv
with open('12_2.csv', 'rb') as csvfile:
   reader = csv.reader(csvfile)
   for row in reader:
       i += 1
       print i
       xy = row
       x.append(float(xy[0]))
       y.append(int(xy[1]))
       print x
       print y

print x
print y

# now use arrays x and y to run linear regression
import scipy.stats as stats

lr = stats.linregress
slope, intercept, rvalue, pvalue, stderr = lr(x,y)

# print results to screen
#print ("slope, intercept, rvalue, pvalue, stderr")
print ("slope, intercept, r-squared")
print slope
print intercept
print rvalue**2
#print pvalue
#print stderr

print ("Boom! sagar kunwar")
