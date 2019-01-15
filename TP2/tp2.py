class Stack:
	def __init__(self):
	    self.my_list=[]

	def Last(self):
		if len(self.my_list)!=0:
			return self.my_list.pop()

	def LastWithoutPop(self):
		if len(self.my_list)!=0:
			return self.my_list[self.Size()-1]

	def First(self):
		if len(self.my_list)!=0:
			return self.my_list.pop(0)

	def AddLast(self,in_value):
		self.my_list.append(in_value)

	def AddFirst(self,in_value):
		self.my_list.insert(0,in_value)

	def GetValueInStack(self,in_key):
			return self.my_list[in_key]

	def Size(self):
		return len(self.my_list)

class Arrete:
	def __init__(self,start_noeud,end_noeud):
		self.start_noeud=start_noeud
		self.end_noeud=end_noeud

	def PrintItSelf(self):
		print "        ",self.start_noeud,"->",self.end_noeud

class Noeud:
	def __init__(self,in_value,in_list_arretes):
		self.value=in_value
		self.list_arretes=in_list_arretes

	def PrintItSelf(self):
		print "noeud:", self.value
		for arrete in self.list_arretes:
			arrete.PrintItSelf()

class Graph:

	def __init__(self):
		self.list_noeuds=Stack()

#	def DepthFirst(self,in_noeud):

	def CompCon(self,in_noeud):
		list_end_arrete_noeud=[]
		list_connexe=[]

		for i in in_noeud.list_arretes:
			list_end_arrete_noeud.append(i.end_noeud)

		for j in list_end_arrete_noeud:
			for k in self.GetNoeud(j).list_arretes:
				if k.end_noeud==in_noeud.value:
					list_connexe.append(j)

		for l in list_connexe:
			print in_noeud.value, "et",l,"connexe" 


#	def Path(self,in_noeud):

#	def Subgraph(self,list_noeud):

	def InsertNoeud(self,in_noeud):
		self.list_noeuds.AddLast(in_noeud)


	def GetNoeud(self,noeud_value):
		for i in self.list_noeuds.my_list:
			if noeud_value==i.value:
				return i

#	def GetArrete(self,noeud_value,start_noeud,end_noeud):

	def PrintItSelf(self):
		print self.list_noeuds.Size(), "noeuds dans le graphe"
		for i in range(self.list_noeuds.Size()):
			self.list_noeuds.GetValueInStack(i).PrintItSelf()

	def PrintAllConnexe(self):
		for i in range(self.list_noeuds.Size()):
			self.CompCon(self.list_noeuds.my_list[i]) 


test_graph=Graph()

test_list_arretes_1=[Arrete(1,2),Arrete(1,3),Arrete(1,4)]
test_noeud_1=Noeud(1,test_list_arretes_1)

test_list_arretes_2=[Arrete(2,5),Arrete(2,4)]
test_noeud_2=Noeud(2,test_list_arretes_2)

test_list_arretes_3=[Arrete(3,2),Arrete(3,4)]
test_noeud_3=Noeud(3,test_list_arretes_3)

test_list_arretes_4=[Arrete(4,1),Arrete(4,3)]
test_noeud_4=Noeud(4,test_list_arretes_4)

test_list_arretes_5=[]
test_noeud_5=Noeud(5,test_list_arretes_5)

test_list_arretes_6=[]
test_noeud_6=Noeud(6,test_list_arretes_6)

test_graph.InsertNoeud(test_noeud_1)
test_graph.InsertNoeud(test_noeud_2)
test_graph.InsertNoeud(test_noeud_3)
test_graph.InsertNoeud(test_noeud_4)
test_graph.InsertNoeud(test_noeud_5)
test_graph.InsertNoeud(test_noeud_6)
print test_graph.PrintItSelf()
test_graph.PrintAllConnexe()
