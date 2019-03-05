from pymongo import MongoClient



def readNodeFile(filename):
    f=open(filename,"r")
    node_li=[]
    for line in f:
        i=line.split(",")[0]
        x=line.split(",")[1]
        y=line.split(",")[2]
        z=line.split(",")[3].split("\n")[0]
        #print(i,x,y,z)
        node_li.append([i,x,y,z])
    return node_li

def readEdgeFile(filename):
    f=open(filename,"r")
    edge_li=[]
    for line in f:
        i=line.split(",")[0]
        x0=line.split(",")[1]
        y0=line.split(",")[2]
        z0=line.split(",")[3]
        x1=line.split(",")[4]
        y1=line.split(",")[5]
        z1=line.split(",")[6].split("\n")[0]
        #print(i,x0,y0,z0,x1,y1,z1)
        edge_li.append([i,x0,y0,z0,x1,y1,z1])
    return edge_li


def writeNodesToDB(node_li):
    client=MongoClient('mongodb://localhost:27017')
    db=client['plugs-dev']
    #client=MongoClient('mongodb://NS:plugs01@ds151078.mlab.com:51078/plugs-prod')
    #db=client['plugs-prod']
    for i in node_li:
        ns_elements=db.ns_elements
        node_data={
            'element_type':'node',
            'nsId':i[0],
            'x':round(float(i[1])/1000,2),
            'y':round(float(i[2])/1000,2),
            'z':round(float(i[3])/1000,2)
            }
        result=ns_elements.insert_one(node_data)
        #print('One post: {0}'.format(result.inserted_id))



def writeEdgesToDB(edge_li):
    client=MongoClient('mongodb://localhost:27017')
    db=client['plugs-dev']
    #client=MongoClient('mongodb://NS:plugs01@ds151078.mlab.com:51078/plugs-prod')
    #db=client['plugs-prod']
    for i in edge_li:
        ns_elements=db.ns_elements
        edge_data={
            'element_type':'edge',
            'nsId':i[0],
            'x0':round(float(i[1])/1000,2),
            'y0':round(float(i[2])/1000,2),
            'z0':round(float(i[3])/1000,2),
            'x1':round(float(i[4])/1000,2),
            'y1':round(float(i[5])/1000,2),
            'z1':round(float(i[6])/1000,2)
            }
        result=ns_elements.insert_one(edge_data)
        #print('One post: {0}'.format(result.inserted_id))        

NODE_LI=readNodeFile("nodes.dat")
EDGE_LI=readEdgeFile("edges.dat")
writeNodesToDB(NODE_LI)
writeEdgesToDB(EDGE_LI)

print("done")



