from pymongo import MongoClient



def readNodeFile(filename):
    f=open(filename,"r")
    node_li=[]
    for line in f:
        i=line.split(",")[0]
        x=line.split(",")[1]
        y=line.split(",")[2]
        z=line.split(",")[3]
        t=line.split(",")[4].split("\n")[0]
        #print(i,x,y,z)
        node_li.append([i,x,y,z,t])
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
        z1=line.split(",")[6]
        t=line.split(",")[7].split("\n")[0]
        #print(i,x0,y0,z0,x1,y1,z1)
        edge_li.append([i,x0,y0,z0,x1,y1,z1,t])
    return edge_li


def writeNodesToDB(node_li):
    client, db=None, None
    if(stage=="dev"):
        client=MongoClient('mongodb://localhost:27017')
        db=client['plugs-dev']
    elif(stage=="prod"):
        client=MongoClient('mongodb://NS:plugs01@ds151078.mlab.com:51078/plugs-prod')
        db=client['plugs-prod']
    else:
        pass
    for i in node_li:
        ns_elements=db.ns_elements
        node_data={
            'element_type':'node',
            'nsId':i[0],
            'x':round(float(i[1])/1000,2),
            'y':round(float(i[2])/1000,2),
            'z':round(float(i[3])/1000,2),
            't':i[4]
            }
        result=ns_elements.insert_one(node_data)
        #print('One post: {0}'.format(result.inserted_id))



def writeEdgesToDB(edge_li):
    client, db=None, None
    if(stage=="dev"):
        client=MongoClient('mongodb://localhost:27017')
        db=client['plugs-dev']
    elif(stage=="prod"):
        client=MongoClient('mongodb://NS:plugs01@ds151078.mlab.com:51078/plugs-prod')
        db=client['plugs-prod']
    else:
        pass
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
            'z1':round(float(i[6])/1000,2),
            't':i[7]
            }
        result=ns_elements.insert_one(edge_data)
        #print('One post: {0}'.format(result.inserted_id))        

def writeParksToDB():
    if(stage=="dev"):
        client=MongoClient('mongodb://localhost:27017')
        db=client['plugs-dev']
    elif(stage=="prod"):
        client=MongoClient('mongodb://NS:plugs01@ds151078.mlab.com:51078/plugs-prod')
        db=client['plugs-prod']
    else:
        pass
    f=open("parks.dat","r")
    area_li=[]
    cen_li=[]
    pt_li=[]
    for line in f:
        data=line.split("\n")[0]
        li=data.split(";")[0]
        area=li.split(",")[0]
        area_li.append(area)            
        x=li.split(",")[1]
        y=li.split(",")[2]
        z=li.split(",")[3]        
        cen_li.append([x,y,z])
        #print(area, [x,y,z])
        pts=data.split(";")
        tmp_pts=[]
        for i in range(1, len(pts)):
            tmp_pts.append(pts[i])
        pt_li.append(tmp_pts)
    k=0
    for i in pt_li:
        ns_elements=db.ns_elements
        park_data={
            'element_type':'park',
            'area':area_li[k],
            'center':cen_li[k],
            'pts':i
        }
        result=ns_elements.insert_one(park_data)
        k+=1

def writeBldgToDB():
    client, db=None, None
    if(stage=="dev"):
        client=MongoClient('mongodb://localhost:27017')
        db=client['plugs-dev']
    elif(stage=="prod"):
        client=MongoClient('mongodb://NS:plugs01@ds151078.mlab.com:51078/plugs-prod')
        db=client['plugs-prod']
    else:
        pass
    f=open("bldg.dat","r")
    area_li=[]
    cen_li=[]    
    pt_li=[]
    for line in f:
        data=line.split("\n")[0]
        li=data.split(";")[0]
        area=li.split(",")[0]
        area_li.append(area)
        x=li.split(",")[1]
        y=li.split(",")[2]
        z=li.split(",")[3]        
        cen_li.append([x,y,z])
        pts=data.split(";")
        tmp_pts=[]
        for i in range(1,len(pts)-1):            
            tmp_pts.append(pts[i])
        pt_li.append(tmp_pts)
    k=0
    for i in pt_li:
        ns_elements=db.ns_elements
        bldg_data={
            'element_type':'bldg',
            'area':area_li[k],
            'cen':cen_li[k],
            'pts':i
        }
        result=ns_elements.insert_one(bldg_data)
        k+=1




def writeSiteToDB():
    client, db=None, None
    if(stage=="dev"):
        client=MongoClient('mongodb://localhost:27017')
        db=client['plugs-dev']
    elif(stage=="prod"):
        client=MongoClient('mongodb://NS:plugs01@ds151078.mlab.com:51078/plugs-prod')
        db=client['plugs-prod']
    else:
        pass
    f=open("site.dat","r")
    area_li=[]
    cen_li=[]    
    pt_li=[]
    for line in f:
        data=line.split("\n")[0]
        li=data.split(";")[0]
        area=li.split(",")[0]
        area_li.append(area)
        x=li.split(",")[1]
        y=li.split(",")[2]
        z=li.split(",")[3]        
        cen_li.append([x,y,z])
        pts=data.split(";")
        tmp_pts=[]
        for i in range(1,len(pts)-1):            
            tmp_pts.append(pts[i])
        pt_li.append(tmp_pts)
    k=0
    for i in pt_li:
        ns_elements=db.ns_elements
        bldg_data={
            'element_type':'site',
            'area':area_li[k],
            'cen':cen_li[k],
            'pts':i
        }
        result=ns_elements.insert_one(bldg_data)
        k+=1




#stage="dev"
stage="prod"

NODE_LI=readNodeFile("nodes.dat")
EDGE_LI=readEdgeFile("edges.dat")
writeNodesToDB(NODE_LI)
writeEdgesToDB(EDGE_LI)
writeParksToDB()
writeBldgToDB()
writeSiteToDB()

print("done: %s "%(stage))



