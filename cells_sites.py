import rhinoscriptsyntax as rs
import operator
import random

def genDiagSites():
    diag_li=[]
    site_li=rs.ObjectsByLayer("ns_sites")
    #site=rs.GetObject("pick site curve")
    k=0
    for site in site_li:
        crv_pts=rs.CurvePoints(site)
        crv_cen=rs.CurveAreaCentroid(site)[0]
        rs.AddTextDot(k,crv_cen)
        k+=1
        tmp_diag_li=[]
        for i in range(len(crv_pts)):
            p0=crv_pts[i]
            for j in range(len(crv_pts)):
                p1=crv_pts[j]
                d=rs.Distance(p0,p1)
                tmp_diag_li.append([p0,p1,d])
        tmp_diag_li.sort(key=operator.itemgetter(2))
        diag=tmp_diag_li[-1]
        diag_li.append(diag)
    #genCells(diag_li)
    
    
def genCells(diag_li):
    for diag in diag_li:
        p,q,norm=diag[0],diag[1],diag[2]
        u=[(q[0]-p[0])/norm, (q[1]-p[1])/norm, 0]
        s=1000
        m=[-u[1],u[0],0]
        n=[u[1],-u[0],0]
        c=[(p[0]+q[0])/2,(p[1]+q[1])/2,0]
        r=[c[0]+m[0]*s,c[1]+m[1]*s,0]
        s=[c[0]+n[0]*s,c[1]+n[1]*s,0]
        rs.AddLine(c,r)
        rs.AddLine(c,s)
        rs.AddLine(p,q)

rs.AddLayer("ns_diag")
genDiagSites()