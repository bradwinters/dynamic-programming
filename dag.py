import numpy as np
'''
'''

def dfs_iterative(graph, start,pwts,stop):
    stack, path = [start], []
     
    wt=0
    #print("Stack is ",stack)
    #print("Path is ",path)
    
    while stack:
        vertex = stack.pop()
        if vertex in path:
            print(".",path)
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
            edgify=vertex+"_"+neighbor
            print("Edge ",vertex," ",neighbor,":",pwts[edgify])
            wt+=pwts[edgify]
            if neighbor==stop:
                print("Done",path)
                return wt, path
    return -99, path





def dfs(graph,node, visited):
    global gWts
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n,visited)
    return visited


def tupalize(pEdge):
    part1=pEdge[0]
    part2=pEdge[1]
    result=part1+"_"+part2
    return  result

def inRange(pNodes,dArray):

    aList=[]
    
    for key, value in pNodes.items():
       for jj in value:
            for mu in pNodes[jj]:
                if key == mu:
                    print("Loop detected ")
                else:
                    ikey=int(key)
                    imu=int(mu)
              
                    if dArray[ikey][imu]==-1:
                        aList.append((key,mu))
                    else:
                        print("Already computed")
    ''' 
    # make a list of pairs with matching start
    # loop thru node keys to find start of edge
    for key, value in pNodes.items():
        if pStart==key:
            for jj in value:
                aList.append((key,jj))
                print("Found key, load ",key," ",jj)
    '''
    return aList


def FindStarts(pNodes,pStart):

    aList=[]
    
    # make a list of pairs with matching start
    # loop thru node keys to find start of edge
    for key, value in pNodes.items():
        if pStart==key:
            for jj in value:
                aList.append((key,jj))
                print("FindStarts:Located key ",key," ",jj)

    return aList

def FindEnds(pNodes,Stuple):
    bList=[]
    # make a list of pairs with matching ends, which are in a list
    print("Searching for successors to ",Stuple) 
    value=pNodes[Stuple[1]]
    for jj in value:
        tuplize=(jj,Stuple[1])  # dont count reverse edge order, same edge
        if Stuple != tuplize:
            bList.append((Stuple[1],jj))

    return bList

def EdgeWt(pStart,pEnd,pwts):
    # convert edges into wts by looking them up in wts

    cpStart=str(pStart)
    cpEnd  =str(pEnd)
    tup=cpStart+"_"+cpEnd  #Create the key
    if tup in pwts:
        jj=pwts[tup]
        #print(tup," weighs ",jj[0])   maybe useful later
    else:
        #print("Edge ",tup," does not exist.")
        return -1 

    return jj 

def CreateMatrix(aDict):
    #  scan the dictionary and create rows x cols against each other
    Rows=[]
    tDgrid=[]
    Dgrid=[]
    for key, value in aDict.items():
        Rows.append(key) 
    Rows.sort()
    for i in range(len(Rows)):
        tDgrid=[]
        for j in range(len(Rows)):
           if i!=j:
               tDgrid.append(-1)
           else:
               tDgrid.append(0)
        Dgrid.append(tDgrid) 

    return Dgrid 

def updateLD(aDict,pKey,pValue):  # update a dict of lists
    
    tList=[] 
    if pKey in aDict:  # exists, extract, update list.  Replace list
       for i in aDict[pKey]:  # make a copy of the list
           tList.append(i)    # 
       if pValue in tList:
           print("Duplicate in list, ignore")
       else:
           tList.append(pValue)   # add the new value if its new
           del aDict[pKey] 
           aDict[pKey]=tList
    else:
       tList.append(pValue)  # create list, put val in it
       aDict[pKey]=tList

    return aDict 

def updateD(aDict,pKey,pValue):  # update a dict of lists
    
    if pKey in aDict:  # exists, extract, update list.  Replace list
       aDict[pKey]=int(pValue)
       print("Possible double entry of an edge in the wts dictionary")
    else:
       aDict[pKey]=int(pValue)

    return aDict 

def GraphIncident(aGraph):
    
    for key, value in aGraph.items():
        newGraph[value]=key

    print("whoa  ")
    print(newGraph)

def printNumpy(Centers):  # prints floats to 3 dec places
    sizeD=len(Centers)
    for i in range(sizeD):
        for j in range(sizeD):
             print(Centers[i][j],end=' ')
        print()

def print2D(Centers,pleaves):  # prints floats to 3 dec places

    row_niceCenters=[] 
    niceCenters=[] 

    for rleaf in pleaves:
        ridx=int(rleaf)
        for cleaf in pleaves:
            #row_niceCenters.append(Centers[leaf])
            cidx=int(cleaf)
            #print(ridx,end=' ')
            print('{:1d}'.format(Centers[ridx][cidx]),end=' ')
        print()

    ''' 
    for row in row_niceCenters:
       for element in row:
           print("%d" % (element),end=" ")
       print()
    ''' 

def ParseU(astring):
    facter=astring.count('_') 
    return facter

def readData():
    '''
    Open hardcoded file, parse data anticipataed but may change
    Load just data into a numpy array, 
    '''
    #f = open('ld.dat', 'r')   #Smaller dataset 
    f = open('dag1.txt', 'r')   #Smaller dataset 
    cnt=0
    dataCnt=0
    clist=[] # list 
    nodeDict={} # dict 
    wtDict={} # dict 
    print("Loading data . . .")
    # K is used to grab the first K lines as clusters, don't consider them
    # Data at this time, that may not be correct
    for line in f:
        xx=line.rstrip() # get rid of cr
        if cnt==0:       # known line to contain only K and M
           n=int(xx)   # n leaves
           ##Use n, to Dim numpy array to build, delete row 0 later 
           #npDataArr = np.zeros(n, dtype=np.float)
        elif cnt==1:
           m=int(xx)
        elif cnt > 1:
           ##Parse data, put rows in list, list appended to a numpy array
           # Rows will be as 0->4:11 where node 0 points to a node 4 with wt 11 
           row=xx.split("->")
          
           pNode=row[0]   # parent node, a dictionary
           ttNode=row[1].split(':')  # temp target node  
           tNode=ttNode[0]   # target node  
           eWt=ttNode[1]   #  weight of the edge 
           # load
           updateLD(nodeDict,pNode,tNode)
           edge=pNode+"_"+tNode
           updateD(wtDict,edge,eWt)
        else:
           print("Something is wrong, bail")

        cnt+=1
    #close(f)

    ### remove phoney line 0 that established shape.  Find a better way later
    #npDataArr=np.delete(npDataArr, 0, 0)
    print("Read ",cnt," Datapoints") 
    return n,m, nodeDict, wtDict 

def FindX(nGrid):

    sizeD=len(nGrid)
    for i in range(sizeD):
        for j in range(sizeD):
             if nGrid[i][j]==-1:
                return str(i), str(j)
    return -99, -99 

def ezGrid(nGrid,pwts):

    sizeD=len(nGrid)
    for i in range(sizeD):
        for j in range(sizeD):
             if j!=i:
                 nGrid[i][j]=EdgeWt(i,j,pwts)
             else:
                 nGrid[i][j]=0
                 

    return nGrid

gWts=[]
    
def main():
   
    startNode, endNode, nodes, wts = readData() #load Data and Params from file
    print("Start node is ",startNode)
    print("End node is ",endNode)
    print("Nodes array is ",nodes)
    print("Wts array is ",wts)

    exit()


 
    Grid=CreateMatrix(nodes)
    # make it numpy
    npGrid=np.array(Grid)

    #  put known wts into the grid from the wts dict.   0 in the diagonal
    aNewGrid=ezGrid(npGrid,wts)
    leaves=[]
    for key, value in nodes.items():
        if len(value) == 1:
            leaves.append(key)
    #St=input("Start node")
    #En=input("End node")
    xxx=0

    for i in range(sz):
        for j in range(sz):
            print("********************")
            score, path = dfs_iterative(nodes, str(i),wts,str(j))
            print("Path for ",i," ",j," Score is ",score)
            print("********************")

    print("*****Finally ******")
    
if __name__ == "__main__":
    main()

