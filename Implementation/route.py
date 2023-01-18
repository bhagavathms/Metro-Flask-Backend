from flask import Flask,jsonify,request
from flask_restful import Api,Resource,reqparse,abort,fields,marshal_with
from flas_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite://database.db'
db=SQLAlchemy(app)
mod=db.Model

#Returning output in the form of json
res_fields={
	'Name':fields.String
	'Interchange':{
		'Name':fields.String
	}
	'cost':fields.Integer
}

#Grenration of graph
class generate_graph(Resource):
	def add_vertex(v):
	  global graph
	  global vertices_no
	  if v in graph:
	    pass
	  else:
	    vertices_no = vertices_no + 1
	    graph[v] = []

	def add_edge(v1, v2, e):
	  global graph
	  if v1 not in graph:
	    pass
	  elif v2 not in graph:
	  	pass
	  else:
	    temp = [v2, e]
	    graph[v1].append(temp)



class find_route(Resource,generate_graph):
	@marshal_with(res_fields)
	def find_short(source,destination):
		src=mod.AllStationEntry.query.get(Sname=source)
		des=mod.AllStationEntry.query.get(Sname=destination)
		oup=dijkstra(src,des,fields'inf')
		return oup

	#check if nodes are directly connceted or not
	def hasPath(v1, v2, processed):
    if (containsEdge(v1, v2)):
        return True
    processed[v1] = True
    vtx = vtces[v1]
    nbrs = list(graph.keys())
    for nbr in nbrs:
        if (nbr not in processed):
            if (hasPath(nbr, vname2, processed)):
                return True
    return False


class DijkstraPair(Resource,generate_graph):
	#values are initiialised
    def __init__(self, vname, psf, cost):
    	cost=mod.CostOfTravel.query.get(maxst=pfs)
        self.vname = vname
        self.psf = psf
        self.cost = cost

    def __lt__(self, other):
        return other.cost - self.cost < 0

	#best route is calculated
	def dijkstra(src, des, nan):
	    val = 0
	    ans = []
	    dict=grpah{}
	    l1 = []
	    for key in vtces:
	        np = DijkstraPair(key, "", float('inf'))
	        hasPath(Vname,float('inf'),0)
	        if (key == src):
	            np.cost = 0
	            np.psf = key     
	        l1.append(np)
	        dict[key] = np
	    while (len(l1) != 0):
	        rp = l1.pop(hl1.index(min(l1)))
	        if(rp.vname == des):
	            val = rp.cost
	            break
	        l1.pop(rp.vname)
	        ans.append(rp.vname)
	        v = vtces[rp.vname]
	        for nbr in v.nbrs:
	            if (nbr not in dict):
	                continue
	            if (rp.cost + v.nbrs[nbr] < map[nbr].cost):
	                dict[nbr].cost = rp.cost + v.nbrs[nbr]
	                dict[nbr].psf = rp.psf + nbr
	    return ans




#Graph for Performing Opearions		
graph = {}
vertices_no = 0
pas=['Yellow','Blue','Red','Green','Violet','Oarnge','Pink','Magenta']

#for Yellow Line
res=mod.YellowLine.query.get(id=1)
prev=res[Sname]
for i in range(1,yellow+1):
	result=mod.YellowLine.query.get(id=i)
	curr=result[Sname]
	add_vertex(curr)
	if(i>1):
		add_edge(curr,prev,1)
		prev=result[Sname]

#for Blue Line
res=mod.BlueLine.query.get(id=1)
prev=res[Sname]
for i in range(1,blue+1):
	result=mod.BlueLine.query.get(id=i)
	curr=result[Sname]
	add_vertex(curr)
	if(i>1):
		add_edge(curr,prev,1)
		prev=result[Sname]
	if(curr='Laxmi Nagar'):
		add_edge(curr,graph['Yamuna Bank'],1)
	if(result[Inter]==pas[0]):
		add_edge(curr,graph[curr[pas[0]]],1)

#for Red Line
res=mod.RedLine.query.get(id=1)
prev=res[Sname]
for i in range(1,red+1):
	result=mod.RedLine.query.get(id=i)
	curr=result[Sname]
	add_vertex(curr)
	if(i>1):
		add_edge(curr,prev,1)
		prev=result[Sname]
	if((result[Inter1]==pas[0])||(result[Inter2]==pas[0])):
		add_edge(curr,graph[curr[pas[0]]],1)
	if((result[Inter1]==pas[1])||(result[Inter2]==pas[1])):
		add_edge(curr,graph[curr[pas[1]]],1)

#for Green Line
res=mod.GreenLine.query.get(id=1)
prev=res[Sname]
for i in range(1,green+1):
	result=mod.GreenLine.query.get(id=i)
	curr=result[Sname]
	add_vertex(curr)
	if(i>1):
		add_edge(curr,prev,1)
		prev=result[Sname]
	if(curr='Satguru Ram Singh Marg'):
		add_edge(curr,graph['Ashok Park Main'],1)
		add_edge(curr,graph['Kirti Nagar'],1)
	if(result[Inter]==pas[0]):
		add_edge(curr,graph[curr[pas[0]]],1)
	if(result[Inter]==pas[1]):
		add_edge(curr,graph[curr[pas[1]]],1)
	if(result[Inter]==pas[2]):
		add_edge(curr,graph[curr[pas[2]]],1)

#for Violet Line
res=mod.VioletLine.query.get(id=1)
prev=res[Sname]
for i in range(1,violet+1):
	result=mod.VioletLine.query.get(id=i)
	curr=result[Sname]
	add_vertex(curr)
	if(i>1):
		add_edge(curr,prev,1)
		prev=result[Sname]
	if((result[Inter1]==pas[0])||(result[Inter2]==pas[0])):
		add_edge(curr,graph[curr[pas[0]]],1)
	if((result[Inter1]==pas[1])||(result[Inter2]==pas[1])):
		add_edge(curr,graph[curr[pas[1]]],1)
	if((result[Inter1]==pas[2])||(result[Inter2]==pas[2])):
		add_edge(curr,graph[curr[pas[2]]],1)
	if((result[Inter1]==pas[3])||(result[Inter2]==pas[3])):
		add_edge(curr,graph[curr[pas[3]]],1)

#for Orange Line
res=mod.OarngeLine.query.get(id=1)
prev=res[Sname]
for i in range(1,ornge+1):
	result=mod.OarngeLine.query.get(id=i)
	curr=result[Sname]
	add_vertex(curr)
	if(i>1):
		add_edge(curr,prev,1)
		prev=result[Sname]
	if(result[Inter]==pas[0]):
		add_edge(curr,graph[curr[pas[0]]],1)
	if(result[Inter]==pas[1]):
		add_edge(curr,graph[curr[pas[1]]],1)
	if(result[Inter]==pas[2]):
		add_edge(curr,graph[curr[pas[2]]],1)
	if(result[Inter]==pas[3]):
		add_edge(curr,graph[curr[pas[3]]],1)
	if(result[Inter]==pas[4]):
		add_edge(curr,graph[curr[pas[4]]],1)


#for Pink Line
res=mod.PinkLine.query.get(id=1)
prev=res[Sname]
for i in range(1,pink+1):
	result=mod.PinkLine.query.get(id=i)
	curr=result[Sname]
	add_vertex(curr)
	if(i>1):
		add_edge(curr,prev,1)
		prev=result[Sname]
	if(result[Inter]==pas[0]):
		add_edge(curr,graph[curr[pas[0]]],1)
	if(result[Inter]==pas[1]):
		add_edge(curr,graph[curr[pas[1]]],1)
	if(result[Inter]==pas[2]):
		add_edge(curr,graph[curr[pas[2]]],1)
	if(result[Inter]==pas[3]):
		add_edge(curr,graph[curr[pas[3]]],1)
	if(result[Inter]==pas[4]):
		add_edge(curr,graph[curr[pas[4]]],1)
	if(result[Inter]==pas[5]):
		add_edge(curr,graph[curr[pas[5]]],1)

#for Magenta Line
res=mod.MagentaLine.query.get(id=1)
prev=res[Sname]
for i in range(1,magenta+1):
	result=mod.MagentaLine.query.get(id=i)
	curr=result[Sname]
	add_vertex(curr)
	if(i>1):
		add_edge(curr,prev,1)
		prev=result[Sname]
	if(result[Inter]==pas[0]):
		add_edge(curr,graph[curr[pas[0]]],1)
	if(result[Inter]==pas[1]):
		add_edge(curr,graph[curr[pas[1]]],1)
	if(result[Inter]==pas[2]):
		add_edge(curr,graph[curr[pas[2]]],1)
	if(result[Inter]==pas[3]):
		add_edge(curr,graph[curr[pas[3]]],1)
	if(result[Inter]==pas[4]):
		add_edge(curr,graph[curr[pas[4]]],1)
	if(result[Inter]==pas[5]):
		add_edge(curr,graph[curr[pas[5]]],1)


#total no of stations initialised as variables
yellow=37
red=29
blue=58
green=24
violet=34
pink=38
magenta=25
orange=6

