import numpy as np



import matplotlib.pyplot as plt
import random

class Point:

	def __init__(self,x,y):
		self.x=x
		self.y=y

class Point_2:

	def __init__(self,x,y,color):
		self.x=x
		self.y=y
		self.color=color

class Droite:

	def __init__(self,m,b,c):
		self.m=m
		self.b=b
		self.center=c

class Cloud:
	#la premiere question, creer un nuage de point qui vas du point d'origine + ou moins le scale et x et en y
	def __init__(self,starting_point, n_number_of_points,scale):
		#random.random()
   		#Return the next random floating point number in the range [0.0, 1.0).
   		self.data_x=[]
   		self.data_y=[]
   		for i in range(n_number_of_points):
   			self.data_x.append(starting_point.x + random.random()*scale - random.random()*scale)
   			self.data_y.append(starting_point.y +random.random()*scale - random.random()*scale)
   		self.center=self.GetCenterCloud()

   	def New(self,data_x,data_y):
		#random.random()
   		#Return the next random floating point number in the range [0.0, 1.0).
   		self.data_x=data_x
   		self.data_y=data_y
   		self.center=self.GetCenterCloud()

   	#la question 4 concretement
	def AddToPlt(self,mediatrice_1_2,mediatrice_1_3,mediatrice_2_3,color1,color2,color3,sign):
		plot_opt1=color1
		plot_opt1+=sign
		plot_opt2=color2
		plot_opt2+=sign
		plot_opt3=color3
		plot_opt3+=sign

		for i in range(len(self.data_x)):
			#r,b,y
			#1,2,3

				vector_MP_1_2=[self.data_x[i]-mediatrice_1_2.center.x,self.data_y[i]-mediatrice_1_2.center.y]
				vector_w_1_2=[-mediatrice_1_2.center.x,mediatrice_1_2.center.y-mediatrice_1_2.b]
				p_scalaire_1_2=np.vdot(vector_MP_1_2,vector_w_1_2)

				vector_MP_1_3=[self.data_x[i]-mediatrice_1_3.center.x,self.data_y[i]-mediatrice_1_3.center.y]
				vector_w_1_3=[-mediatrice_1_3.center.x,mediatrice_1_3.center.y-mediatrice_1_3.b]
				p_scalaire_1_3=np.vdot(vector_MP_1_3,vector_w_1_3)

				vector_MP_2_3=[self.data_x[i]-mediatrice_2_3.center.x,self.data_y[i]-mediatrice_2_3.center.y]
				vector_w_2_3=[-mediatrice_2_3.center.x,mediatrice_2_3.center.y-mediatrice_2_3.b]
				p_scalaire_2_3=np.vdot(vector_MP_2_3,vector_w_2_3)

				#on compare les bleus et jaune (2 et 3)
				if p_scalaire_2_3 > 0:
					if p_scalaire_1_3 > 0:
						plt.plot(self.data_x[i] ,self.data_y[i] ,plot_opt3)
					else:
						plt.plot(self.data_x[i] ,self.data_y[i] ,plot_opt1)
				else:
					if p_scalaire_1_2 > 0:
						plt.plot(self.data_x[i] ,self.data_y[i] ,plot_opt1)
					else:
						plt.plot(self.data_x[i] ,self.data_y[i] ,plot_opt2)

		#on rajoute le centre
		plt.plot(self.center.x,self.center.y,"ko")


	#calcul le centre d'un groupe q2
	def GetCenterCloud(self):
		avg_x=0
		avg_y=0

		for i in self.data_x:
			avg_x= avg_x+i
		avg_x=avg_x/float(len(self.data_x))

		for i in self.data_y:
			avg_y= avg_y+i
		avg_y=avg_y/float(len(self.data_y))

		return Point(avg_x,avg_y)


class Application:

	def __init__(self):
		self.unsorted_cloud=None
		self.cloud_1=Cloud(Point(0,0),1,0) 
		self.cloud_2=Cloud(Point(0,0),1,0)
		self.mediatrice_1_2=None
		self.mediatrice_1_3=None
		self.mediatrice_2_3=None
		self.cloud_3=Cloud(Point(0,0),1,0)#les nouveaux points, c'est moche mais jai pas le temps
		self.cloud_4=Cloud(Point(0,0),1,0)

	def AddPoints(self,n_number_of_points):
		data_x=[]
		data_y=[]
		for i in range(n_number_of_points):
			data_x.append(3+random.random()*4)
			data_y.append(random.random()*3)
		#ugly but on a hurry
		self.cloud_4.New(data_x,data_y)


	def AddData_1(self,data_x,data_y):
		self.cloud_1.New(data_x,data_y)

	def AddData_2(self,data_x,data_y):
		self.cloud_2.New(data_x,data_y)

	def AddData_3(self,data_x,data_y):
		self.cloud_3.New(data_x,data_y)

	def DefCloud_1(self,starting_point, n_number_of_points,scale):
		self.cloud_1=Cloud(starting_point, n_number_of_points,scale)

	def DefCloud_2(self,starting_point, n_number_of_points,scale):
		self.cloud_2=Cloud(starting_point, n_number_of_points,scale)

	def DefMediatrice(self):
		self.mediatrice_1_2=self.ComputeMediatrice(self.cloud_1.center,self.cloud_2.center)
		self.mediatrice_1_3=self.ComputeMediatrice(self.cloud_1.center,self.cloud_3.center)
		self.mediatrice_2_3=self.ComputeMediatrice(self.cloud_2.center,self.cloud_3.center)

	def ComputeLine(self,p_1,p_2):
		#calcul du coeficient directeur de la droite
		m=(p_2.y - p_1.y) / float(p_2.x - p_1.x)
		#calcul de la valeur en ordonee a l'origine
		b=p_1.y - m * p_1.x
		return m,b

	def ComputeMediatrice(self,p_1,p_2):
		if not self.cloud_1 == None and not self.cloud_2 == None:
			#on calcul l'equation de la droite reliant les deux centres
			m,b = self.ComputeLine(p_1,p_2)
			#on a la droite reliant les deux points
			#on calcul le centre de la droite
			x_c=(p_1.x + p_2.x)/2
			y_c=m*x_c+b
			#on cherche le coeficient directeur de la mediatrice
			m_mediatrice=-1/m
			#on cherche l'ordonnee a l'origine
			b_mediatrice=y_c-m_mediatrice*x_c
			return Droite(m_mediatrice,b_mediatrice,Point(x_c,y_c))

	#la question 5 concretement
	def PrintItSelf(self):
		plt.clf()
		self.cloud_1.AddToPlt(self.mediatrice_1_2,self.mediatrice_1_3,self.mediatrice_2_3,"r","b","y","o")
		self.cloud_2.AddToPlt(self.mediatrice_1_2,self.mediatrice_1_3,self.mediatrice_2_3,"r","b","y","o")
		self.cloud_3.AddToPlt(self.mediatrice_1_2,self.mediatrice_1_3,self.mediatrice_2_3,"r","b","y","o")
		self.cloud_4.AddToPlt(self.mediatrice_1_2,self.mediatrice_1_3,self.mediatrice_2_3,"r","b","y","x")

		x_min,x_max=plt.xlim()
		y_min,y_max=plt.ylim()

		#plt.plot([x_min,x_max], [int(self.mediatrice_1_2.m*x_min+self.mediatrice_1_2.b),int(self.mediatrice_1_2.m*x_max+self.mediatrice_1_2.b)],"g-")
		#plt.plot([x_min,x_max], [int(self.mediatrice_1_3.m*x_min+self.mediatrice_1_3.b),int(self.mediatrice_1_3.m*x_max+self.mediatrice_1_3.b)],"g-")
		#plt.plot([x_min,x_max], [int(self.mediatrice_2_3.m*x_min+self.mediatrice_2_3.b),int(self.mediatrice_2_3.m*x_max+self.mediatrice_2_3.b)],"g-")
	
		plt.xlim(x_min,x_max)
		plt.ylim(y_min,y_max)
		plt.show()


file=open("iris.txt","r")
data=[('sepal_l','<f8'),('sepal_w','<f8'),('petal_l', '<f8'),('petal_w', '<f8'), ('classe','|S15')]
data = np.genfromtxt(file, dtype=None,delimiter=',',names=True)

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

#exemple avec la liste 1_4 mais ca marche avec le reste
my_app=Application()
data_x_r=[]
data_y_r=[]

data_x_b=[]
data_y_b=[]

data_x_y=[]
data_y_y=[]


#les couleurs sont pas vraiment coherente
for p in list_points_critere_1_4:
	if(p.color=="r"):
		data_x_r.append(p.x)
		data_y_r.append(p.y)
	if(p.color=="b"):
		data_x_b.append(p.x)
		data_y_b.append(p.y)
	if(p.color=="y"):
		data_x_y.append(p.x)
		data_y_y.append(p.y)

my_app.AddData_1(data_x_r,data_y_r)
my_app.AddData_2(data_x_b,data_y_b)
my_app.AddData_3(data_x_y,data_y_y)
my_app.DefMediatrice()
my_app.AddPoints(100)

my_app.PrintItSelf()