import numpy as np
import math


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
	def AddToPlt(self,mediatrice,color1,color2,sign):
		plot_opt1=color1
		plot_opt1+=sign
		plot_opt2=color2
		plot_opt2+=sign

		for i in range(len(self.data_x)):

				vector_MP=[self.data_x[i]-mediatrice.center.x,self.data_y[i]-mediatrice.center.y]
				vector_w=[-mediatrice.center.x,mediatrice.center.y-mediatrice.b]
				p_scalaire=np.vdot(vector_MP,vector_w)
				if p_scalaire > 0:
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
		self.cloud_1=None 
		self.cloud_2=None
		self.mediatrice=None
		self.cloud_3=Cloud(Point(0,0),1,0)

	def AddPoints(self,n_number_of_points):
		data_x=[]
		data_y=[]
		for i in range(n_number_of_points):
			data_x.append(random.random()*10-random.random()*10)
			data_y.append(random.random()*10-random.random()*10)
		#ugly but on a hurry
		self.cloud_3.New(data_x,data_y)



	def DefCloud_1(self,starting_point, n_number_of_points,scale):
		self.cloud_1=Cloud(starting_point, n_number_of_points,scale)

	def DefCloud_2(self,starting_point, n_number_of_points,scale):
		self.cloud_2=Cloud(starting_point, n_number_of_points,scale)

	def DefMediatrice(self):
		self.mediatrice=self.ComputeMediatrice(self.cloud_1.center,self.cloud_2.center)

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
		self.cloud_1.AddToPlt(self.mediatrice,"r","b","o")
		self.cloud_2.AddToPlt(self.mediatrice,"r","b","o")
		if not self.cloud_3 == None: 
			self.cloud_3.AddToPlt(self.mediatrice,"r","b","x")
		
		x_min,x_max=plt.xlim()
		y_min,y_max=plt.ylim()
		plt.plot([x_min,x_max], [int(self.mediatrice.m*x_min+self.mediatrice.b),int(self.mediatrice.m*x_max+self.mediatrice.b)],"g-")

		plt.xlim(x_min,x_max)
		plt.ylim(y_min,y_max)
		plt.show()


starting_point_cloud_1=Point(-1,-1)
starting_point_cloud_2=Point(1,1)

my_app = Application()

my_app.DefCloud_1(starting_point_cloud_1,50,0.5)

my_app.DefCloud_2(starting_point_cloud_2,50,0.5)
#creer la mediatrice (pas vraiment le temps de faire des tests)
my_app.DefMediatrice()

my_app.AddPoints(50)

my_app.PrintItSelf()