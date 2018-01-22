#print(__doc__)

# Import the necessary modules and libraries
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import unicodecsv as csv
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from matplotlib.offsetbox import AnchoredText



X_arr =[]
Y_arr = []
Y_test_arr = []
X_test = []

with open('input_train.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar=' ')
     for row in spamreader:
	row1 =  (row[:1]) if (len(row)> 1) else row
	a = row[0].split("%")
	b = row[1].replace(u'\xa0', ' ').split(' ')
	c = row[2].replace(u'\xa0', ' ').split(' ')
	if(b[0]== '' or b[0]== ''):
		 b[0]=999
	if(a[0]== 'N/A' or a[0]== ''):
		 a[0]=0
	X_arr.append( [int(a[0]),float(c[0])])
	
with open('label_train.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
     for row in spamreader:
	b = row[1].split(',')
	b1 =row[3].split(',')
	a= float(str(b[0]))
	a1= float(str(b1[0]))
	Y_arr.append( [float(a),float(a1)])


with open('label_test.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
     for row in spamreader:
	b = row[1].split(',')
	b1 =row[3].split(',')
	a= float(str(b[0]))
	a1= float(str(b1[0]))
	Y_test_arr.append( [float(a),float(a1)])

with open('input_test.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar=' ')
     for row in spamreader:
	a = row[5].split("%")
	b = row[1].replace(u'\xa0', ' ').split(' ')
	c = row[7].replace(u'\xa0', ' ').split(' ')
	X_test.append( [int(a[0]),float(b[0])])

		


# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=2,criterion="friedman_mse",splitter="best",min_samples_split=0.50)
regr_2 = DecisionTreeRegressor(max_depth=5,criterion="friedman_mse",splitter="best",min_samples_split=0.75)
regr_3 = DecisionTreeRegressor(max_depth=12,criterion="friedman_mse",splitter="best",min_samples_split=0.75)


regr_1.fit(X_arr, Y_arr)
regr_2.fit(X_arr, Y_arr)
regr_3.fit(X_arr, Y_arr)

print X_arr[0]  #show how feature are stored, check the order must correspond to Y_arr
print Y_arr[0]  #show how feature are stored, check the order must correspond to X_arr


# Predict
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
y_3 = regr_3.predict(X_test)

print "MSE for Max_depth=2: "
mse1 = mean_squared_error(Y_test_arr, y_1, multioutput='uniform_average')
print "MSE for Max_depth=5: "
mse2 = mean_squared_error(Y_test_arr, y_2, multioutput='uniform_average')
print "MSE for Max_depth=5: "
mse3 =  mean_squared_error(Y_test_arr, y_3, multioutput='uniform_average')
print "R2 for Max_depth=2: "
R2_1 =  r2_score(Y_test_arr, y_1)  
print "R2 for Max_depth=5: "
R2_2 =  r2_score(Y_test_arr, y_2)
print "R2 for Max_depth=12: "  
R2_3 = r2_score(Y_test_arr, y_3) 

# Plot the results
fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.95)
fig.subplots_adjust(bottom=0.05)
fig.subplots_adjust(left=0.05)
fig.subplots_adjust(right=0.95)


ax.text(50, 45, ''.join(['MSE for (Max_depth=2) : ',str(mse1)]), style='italic',
        bbox={'facecolor':'red', 'alpha':0.1, 'pad':10})
ax.text(50, 40, ''.join(['MSE for (Max_depth=5) : ',str(mse2)]), style='italic',
        bbox={'facecolor':'red', 'alpha':0.1, 'pad':10})
ax.text(50, 35, ''.join(['MSE for (Max_depth=12) : ',str(mse3)]), style='italic',
        bbox={'facecolor':'red', 'alpha':0.1, 'pad':10})
ax.text(25, 45, ''.join(['R2 for (Max_depth=2) : ',str(R2_1)]), style='italic',
        bbox={'facecolor':'red', 'alpha':0.1, 'pad':10})
ax.text(25, 40, ''.join(['R2 for (Max_depth=5) : ',str(R2_2)]), style='italic',
        bbox={'facecolor':'red', 'alpha':0.1, 'pad':10})
ax.text(25, 35, ''.join(['R2 for (Max_depth=12) : ',str(R2_3)]), style='italic',
        bbox={'facecolor':'red', 'alpha':0.1, 'pad':10})
  

plt.scatter(X_arr,Y_arr, s=20, edgecolor="black",
            c="darkorange", label="data")
plt.plot(X_test, y_1, color="cornflowerblue",label="max_depth=2", linewidth=2)
plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.plot(X_test, y_3, color="red", label="max_depth=12", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()

