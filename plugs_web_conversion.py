import rhinoscriptsyntax as rs


class Node(object):
    def __init__(self, x,y,z,i,element_set):
        self.x=x
        self.y=y
        self.z=0
        self.id=i
        self.pt=[x,y,0]
        self.element_set=element_set

class Edge(object):
    def __init__(self,n0,n1,i,element_set):
        self.node0=n0
        self.node1=n1
        self.id=i
        self.element_set=element_set
    
def setCirculationGraph():
    x=rs.ObjectsByLayer("ns_nodes")
    node_li=[]
    k=0
    for i in x:
        c=rs.CircleCenterPoint(i)
        node_li.append(Node(c[0],c[1],0,k,"NCN"))
        k+=1
    x_gcn=rs.ObjectsByLayer("ns_gcn_nodes")
    for i in x_gcn:
        c=rs.CircleCenterPoint(i)
        node_li.append(Node(c[0],c[1],0,k,"GCN"))
        k+=1
    y=rs.ObjectsByLayer("ns_edges")
    edge_li=[]
    k=0
    for i in y:
        p=rs.CurveStartPoint(i)
        q=rs.CurveEndPoint(i)
        node0=None
        node1=None
        sum0,sum1=0,0
        for j in node_li:
            r=j.pt
            if(rs.Distance(r,p)<10):
                node0=j
                sum0+=1
                break
        for j in node_li:
            r=j.pt            
            if(rs.Distance(r,q)<10):
                node1=j
                sum1+=1
                break
        if(sum0>0 and sum1>0):
            edge_li.append(Edge(node0,node1,k,"road"))
        k+=1
    y_green=rs.ObjectsByLayer("ns_green_edges")
    for i in y_green:
        p=rs.CurveStartPoint(i)
        q=rs.CurveEndPoint(i)
        node0=None
        node1=None
        sum0,sum1=0,0
        for j in node_li:
            r=j.pt
            if(rs.Distance(r,p)<10):
                node0=j
                sum0+=1
                break
        for j in node_li:
            r=j.pt            
            if(rs.Distance(r,q)<10):
                node1=j
                sum1+=1
                break
        if(sum0>0 and sum1>0):
            edge_li.append(Edge(node0,node1,k,"green"))
    
    for i in edge_li:
        p=i.node0.pt
        q=i.node1.pt
        L=rs.AddLine(p,q)
        rs.MoveObject(L,[0,0,1000])
        
    return [node_li,edge_li]


def writeNodeToCsv(node_li, filename):
    f=open(filename,"w")
    for i in node_li:
        s=str(i.id)+","+str(round(i.x,2))+","+str(round(i.y,2))+","+str(0)+","+i.element_set+"\n"
        f.write(s)
    f.close()

def writeEdgeToCsv(edge_li, filename):
    f=open(filename,"w")
    s=""
    for i in edge_li:
        s=str(i.id)+","+str(i.node0.x)+","+str(i.node0.y)+","+str(0)+","+str(i.node1.x)+","+str(i.node1.y)+","+str(0)+","+i.element_set+"\n"
        f.write(s)
    f.close()


def writeParksToCsv(filename):
    x=rs.ObjectsByLayer("ns_parks")
    park_li=[]
    k=0
    for i in x:
        pts=rs.CurvePoints(i)
        area=rs.CurveArea(i)[0]/10000
        print(area)
        c=rs.CurveAreaCentroid(i)[0]
        s=str(round(area,2))+";"+str(round(c[0]/1000,2))+","+str(round(c[1]/1000,2))+","+str(round(c[2]/1000,2))+"\n"
        for j in pts:
            s+=str(round(j[0]/1000,2))+","+str(round(j[1]/1000,2))+","+str(round(j[2]/1000,2))+";"
        s+="\n"
        park_li.append(s)
        k+=1
    f=open(filename,"w")
    for i in park_li:
        f.write(i)
    f.close()

def writeBldgToCsv(filename):
    x=rs.ObjectsByLayer("ns_existing_houses")
    bldg_li=[]
    k=0
    for i in x:
        try:
            pts=rs.CurvePoints(i)
            area=rs.CurveArea(i)[0]/10000
            c=rs.CurveAreaCentroid(i)[0]
            s=str(round(area,2))+";"+str(round(c[0]/1000,2))+","+str(round(c[1]/1000,2))+","+str(round(c[2]/1000,2))+"\n"
            for j in pts:
                s+=str(round(j[0]/1000,2))+","+str(round(j[1]/1000,2))+","+str(round(j[2]/1000,2))+";"
            s+="\n"
            bldg_li.append(s)
        except:
            pass
        k+=1
    print("length of building : ",len(bldg_li))
    f=open(filename,"w")
    for i in bldg_li:
        f.write(i)
    f.close()
    
    
    


def moveObject(name):
    obj=rs.ObjectsByLayer(name)
    b=rs.ObjectsByLayer("ns_bounding_box")[0]
    
    c=rs.CurveAreaCentroid(b)[0]
    d=[-c[0],-c[1],-c[2]]
    for i in obj:
        rs.MoveObject(i,d)
    
    
###moveObject("kyojimas")#not required for now
#GRAPH=setCirculationGraph()#done
#NODE_LI=GRAPH[0]#done
#EDGE_LI=GRAPH[1]#done
#writeNodeToCsv(NODE_LI,"nodes.dat")#done
#writeEdgeToCsv(EDGE_LI,"edges.dat")#done
writeParksToCsv("parks.dat")
writeBldgToCsv("bldg.dat")