# Variables
Num_Of_Node=None
Num_Of_Link=None
MenuChoose=None
Location=[]
Degrees=None
InNodeId=None
OutNodeId=None
Node_Del_choose=None
Link_Del_choose=None
l=0
Id=0
nodes={Id:{'Location':[], 'Degrees':0}}
links={l:{'InNodeId':None, 'OutNodeId':None}}
# Functions
def MainMenu():
    print("Choose What you Want to Do or enter 0 to exit :")
    print("1)Adding Node")
    print("2)Deleting Node")
    print("3)Finding Node")
    print("4)Adding Link")
    print("5)Deleting Link")
    print("6)Finding Link")
    print("7)Show all nodes and links")

def DelMenu():
    print("Choose how to delete:")
    print("1)Deleting with Id of node")
    print("2)Deleting with Location of node")

def LinkDelMenu():
    print("Choose how to delete:")
    print("1)Deleting with Number of the link")
    print("2)Deleting with InNodeID and OutNodeID of link")

def TotalShow():
    print("All the nodes : ")
    for i in range(len(nodes)):
       print("ID = %s : "%i, nodes[i])
    print("\n")
    print("------------------------------------------")
    print("\n")
    print("All the links : ")
    for i in range(len(links)):
        print("links %s : "%i, links[i]) 
# Classes
class Graph:
    def FindingNode(self,Id):
        self.Id=Id
        if Id<len(nodes):
            print("Node With ID number %s is : "%Id,nodes[Id])
        else:
            print("Incorrect ID !!!!")
    def FindingLink(self,Id):
        self.Id=Id
        for i in range(len(links)):
            if links[i]['InNodeId']==Id or links[i]['OutNodeId']==Id:
                print("%sth links of node is"%(i+1) , links[i])
    class Node:  
        def AddingNode(self):
            global Id
            nodes[Id]={'Location':[], 'Degrees':0}
            print("enter Node Location with ID = %s"%Id)
            nodes[Id]['Location'].append(float(input("enter x = ")))
            nodes[Id]['Location'].append(float(input("enter y = ")))
            Id+=1 
        def DeletingNode(self,Id):
            self.Id=Id
            del nodes[Id]
            for i in range(len(links)):
                if links[i]['InNodeId']==Id or links[i]['OutNodeId']==Id:
                    del links[i]
                    for j in range(len(links)-i):
                        links[j+i]=links.pop(j+1+i)
                    break
            for i in range(len(nodes)-(Id)):
                nodes[Id+i]=nodes.pop(Id+1+i)

    class Link:
        def AddingLink(self,InNodeId,OutNodeId):
            global l
            self.InNodeId=InNodeId
            self.OutNodeId=OutNodeId
            links[l]={'InNodeId':InNodeId, 'OutNodeId':OutNodeId}
            nodes[InNodeId]['Degrees']+=1
            nodes[OutNodeId]['Degrees']+=1
            l+=1
        def DeletingLink(self,InNodeId,OutNodeId):
            self.InNodeId=InNodeId
            self.OutNodeId=OutNodeId
            nodes[InNodeId]['Degrees']-=1
            nodes[OutNodeId]['Degrees']-=1
            for i in range(len(links)):
                if links[i]['InNodeId']==InNodeId and links[i]['OutNodeId']==OutNodeId:
                    del links[i]
                    for j in range(len(links)-i):
                        links[j+i]=links.pop((j+1)+i)
                    break

# Main Codes
G=Graph()
NODE=G.Node()
LINK=G.Link()
while MenuChoose!=0:
  
    MainMenu()
    MenuChoose=int(input("Enter the number from above list or 0 to exit : "))
  
    if MenuChoose==1:
        Num_Of_Node=int(input("Enter the number of node you want to add : "))
        for i in range(Num_Of_Node):
            NODE.AddingNode()
  
    if MenuChoose==2:
        DelMenu()
        Node_Del_choose=int(input("enter the number from above list : "))
        if Node_Del_choose==1:  
            ID=int(input("enter the ID you want to delete its node : "))
            NODE.DeletingNode(ID)
            Id-=1
        if Node_Del_choose==2:
            Location.append(float(input("enter x : ")))
            Location.append(float(input("enter y : ")))
            for i in range(len(nodes)):
                if Location[0]==nodes[i]['Location'][0] and Location[1]==nodes[i]['Location'][1]:
                    NODE.DeletingNode(i)
                    Id-=1
                    break
            else:
                print("Ther is not such a node !!!")
  
    if MenuChoose==3:
        G.FindingNode(int(input("enter the ID of node you want to find : ")))
  
    if MenuChoose==4:
        Num_Of_Link=int(input("Enter the number of link you want to add : "))
        for i in range(Num_Of_Link):
            LINK.AddingLink(int(input("enter InNodeID of link %s : "%i)),int(input("enter OutNodeID of link %s : "%i)))
   
    if MenuChoose==5:
        LinkDelMenu()
        Link_Del_choose=int(input("enter the number from above list : "))
        if Link_Del_choose==1:  
            num=int(input("enter the ID you want to delete its link : "))
            del links[num]
            for j in range(len(links)-num):
                links[j+num]=links.pop(j+1+num)
        if Link_Del_choose==2:
            LINK.DeletingLink(int(input("enter InNodeID : ")),int(input("enter OutNodeID : ")))
   
    if MenuChoose==6:
        G.FindingLink(int(input("enter the ID of node you want to find its link(s) : ")))
  
    if MenuChoose==7:
        TotalShow()
 
print("Good Bye!!!")

