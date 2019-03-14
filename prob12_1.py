import scipy

x = [4,6,7,11,14,17,21]
y = [18,12,13,8,7,7,4]

scipy.mean(x)
11.428571428571429
scipy.median(x)
11.0
scipy.std(x)
5.7782138331876247
scipy.mean(y)
9.8571428571428577
scipy.median(y)
8.0
scipy.std(y)
4.3892261416392051

import scipy.stats as stats
stats.pearsonr(x,y)
(-0.92698953702675413, 0.0026589803215800443)

lr = stats.linregress
slope,intercept,rvalue,pvalue,stderr = lr(x,y)

slope
-0.70415647921760383
intercept
17.904645476772615
rsq = rvalue**2
rsq
0.85930960175707571

xval = 10
yhat = slope*xval+intercept
yhat
10.863080684596577
