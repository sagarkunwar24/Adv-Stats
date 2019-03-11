#!/usr/bin/env python2.7
# initiate a few variables
i = 0
Id=[]
Gdp= []
Fertrate= []

# read csv file and store data in arrays x and y
import csv
with open('emea.csv','rb') as csvfile:
   reader = csv.reader(csvfile)
   for row in reader:
       i += 1
       #print i
       emea = row
       Id.append(int(emea[0]))
       Gdp.append(float(emea[1]))
       Fertrate.append(float(emea[2]))
       #print x
       #print y

print ("Id")
print Id
print ("Gdp")
print Gdp
print ("Fertility rate")
print Fertrate

# now use arrays x and y to run linear regression
import scipy.stats as stats

lr = stats.linregress
slope, intercept, rvalue, pvalue, stderr,= lr(Gdp,Fertrate)

# print results to screen
print 'slope',slope
print 'intercept',intercept
print 'rvalue',rvalue
print 'pvalue',pvalue
print 'stand error',stderr

print 'Y=',slope,'*X+',intercept

print (" sagar kunwar")
print
