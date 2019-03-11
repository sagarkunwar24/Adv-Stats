#! usr/bin/env python2.7
x1=[]
x2=[]
x3=[]
y=[]

import csv
with open('exam-2.csv') as csvfile:
    reader =csv.reader(csvfile)
    for row in reader:
        xy=row
        x1.append(int(xy[0]))
        x2.append(int(xy[1]))
        x3.append(int(xy[2]))
        y.append(int(xy[3]))


x=[x1,x2,x3]


print 'Define '
print 'x1=Bedrooms'
print 'x2=baths'
print 'x3=total sqft'
print
import numpy as np
import statsmodels.api as sm

def reg_m(y, x):
    x = np.array(x).T
    x = sm.add_constant(x)
    results = sm.OLS(endog=y, exog=x).fit()
    return results

print reg_m(y,x).summary()
print 'Sagar Kunwar'
print
print "PRAYFORPARISPEOPLE"
print






