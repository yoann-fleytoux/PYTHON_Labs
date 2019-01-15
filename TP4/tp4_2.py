import numpy as np
import matplotlib.pyplot as plt

class Point_2:

	def __init__(self,x,y,color):
		self.x=x
		self.y=y
		self.color=color


file=open("iris.txt","r")
data=[('sepal_l','<f8'),('sepal_w','<f8'),('petal_l', '<f8'),('petal_w', '<f8'), ('classe','|S15')]
data = np.genfromtxt(file, dtype=None,delimiter=',',names=True)

print data['sepal_l'][0], data['sepal_w'][0], data['petal_l'][0], data['petal_w'][0], data['classe'][0]

#on vas afficher les differentes data
list_points_critere_1_2=[]
list_points_critere_1_3=[]
list_points_critere_1_4=[]
list_points_critere_2_3=[]
list_points_critere_2_4=[]
list_points_critere_3_4=[]

for i in range(len(data)):
	if data['classe'][i]=="Iris-versicolor":
		list_points_critere_1_2.append(Point_2(data['sepal_l'][i],data['sepal_w'][i],"r"))
	elif data['classe'][i]=="Iris-virginica":
		list_points_critere_1_2.append(Point_2(data['sepal_l'][i],data['sepal_w'][i],"b"))
	else:
		list_points_critere_1_2.append(Point_2(data['sepal_l'][i],data['sepal_w'][i],"y"))

	if data['classe'][i]=="Iris-versicolor":
		list_points_critere_1_3.append(Point_2(data['sepal_l'][i],data['petal_l'][i],"r"))
	elif data['classe'][i]=="Iris-virginica":
		list_points_critere_1_3.append(Point_2(data['sepal_l'][i],data['petal_l'][i],"b"))
	else:
		list_points_critere_1_3.append(Point_2(data['sepal_l'][i],data['petal_l'][i],"y"))

	if data['classe'][i]=="Iris-versicolor":
		list_points_critere_1_4.append(Point_2(data['sepal_l'][i],data['petal_w'][i],"r"))
	elif data['classe'][i]=="Iris-virginica":
		list_points_critere_1_4.append(Point_2(data['sepal_l'][i],data['petal_w'][i],"b"))
	else:
		list_points_critere_1_4.append(Point_2(data['sepal_l'][i],data['petal_w'][i],"y"))

	if data['classe'][i]=="Iris-versicolor":
		list_points_critere_2_3.append(Point_2(data['sepal_w'][i],data['petal_l'][i],"r"))
	elif data['classe'][i]=="Iris-virginica":
		list_points_critere_2_3.append(Point_2(data['sepal_w'][i],data['petal_l'][i],"b"))
	else:
		list_points_critere_2_3.append(Point_2(data['sepal_w'][i],data['petal_l'][i],"y"))

	if data['classe'][i]=="Iris-versicolor":
		list_points_critere_2_4.append(Point_2(data['sepal_w'][i],data['petal_w'][i],"r"))
	elif data['classe'][i]=="Iris-virginica":
		list_points_critere_2_4.append(Point_2(data['sepal_w'][i],data['petal_w'][i],"b"))
	else:
		list_points_critere_2_4.append(Point_2(data['sepal_w'][i],data['petal_w'][i],"y"))


	if data['classe'][i]=="Iris-versicolor":
		list_points_critere_3_4.append(Point_2(data['petal_l'][i],data['petal_w'][i],"r"))
	elif data['classe'][i]=="Iris-virginica":
		list_points_critere_3_4.append(Point_2(data['petal_l'][i],data['petal_w'][i],"b"))
	else:
		list_points_critere_3_4.append(Point_2(data['petal_l'][i],data['petal_w'][i],"y"))

print "critere 1 et 2"
for p in list_points_critere_1_2:
	plt.plot(p.x ,p.y ,p.color+"o")
plt.show()

print "critere 1 et 3"
plt.clf()
for p in list_points_critere_1_3:
	plt.plot(p.x ,p.y ,p.color+"o")
plt.show()

print "critere 1 et 4"
plt.clf()
for p in list_points_critere_1_4:
	plt.plot(p.x ,p.y ,p.color+"o")
plt.show()

print "critere 2 et 3"
plt.clf()
for p in list_points_critere_2_3:
	plt.plot(p.x ,p.y ,p.color+"o")
plt.show()

print "critere 2 et 4"
plt.clf()
for p in list_points_critere_2_4:
	plt.plot(p.x ,p.y ,p.color+"o")
plt.show()

print "critere 3 et 4"
plt.clf()
for p in list_points_critere_3_4:
	plt.plot(p.x ,p.y ,p.color+"o")
plt.show()

print "conclusion: les criteres interressant sont: tout sauf le 1_2"
