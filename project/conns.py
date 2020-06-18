from tree import Tree
from node import Node

#main conn function is called by make_tree which is in options
#calls different conn functions to decide what needs to be done next

def conn(node):
    i = 0
    x = node.v
    found = False
    while not found and i<len(x):
        #found will remain false if the sentence at i is either a singular sentence letter
        #or the negation of one
        if len(x[i])==2:
            found = which_not(node,i)
        elif len(x[i])==3:
            found = which_bi(node,i)
        i+=1

def which_not(node,i):
    x=(node.v)[i][1]
    #if statement passes through different characteristics which certain sentence types uniquely possess
    if len(x)==2:
        nn_conn(node,i)
        return True
    elif len(x)==3:
        if x[1]=="v":
            nor_conn(node,i)
        elif x[1]=="^":
            nand_conn(node,i)
        elif x[1]=="->":
            nif_conn(node,i)
        else:
            niff_conn(node,i)
        return True
    else:
        return False

def which_bi(node,i):
    x = node.v[i]
    #same as for which_not
    if x[1]=="v":
        or_conn(node,i)
    elif x[1]=="^":
        and_conn(node,i)
    elif x[1]=="->":
        if_conn(node,i)
    else:
        iff_conn(node,i)
    return True

#for ( ¬ ( ¬ ( ...
def nn_conn(node, i):
    y = (node.v)
    x = y[i][:]
    k = 0
    while isinstance(x,list) and x[0]=="¬":
        k+=1
        print(x)
        x = x[1]
    if k%2==1:
        if isinstance(x,list):
            x = ["¬",x]
        else:
            x = x = ["¬",[x]]
    print(x)
    y[i] = x[:]
    node.vd.append(x)
        
# for ... v ...
def or_conn(node, i):
    x = node.v
    y = x[i][:]
    del x[i]
    f = x[:]
    f.append(y[0][:])
    s = x[:]
    s.append(y[2][:])
    
    node.l = Node(f)
    node.l.vd.append(y[0][:])
    node.l.p = node
    node.r = Node(s)
    node.r.vd.append(y[2][:])
    node.r.p = node

#for ¬ ( ... v ... )
def nor_conn(node, i):
    x = node.v
    y = x[i][1][:]
    del x[i]
    if isinstance(y[0],list):
        z = ["¬", y[0][:]]
    else:
        z = ["¬", [y[0][:]]]
    if isinstance(y[2],list):
        z1 = ["¬", y[2][:]]
    else:
        z1 = ["¬", [y[2][:]]]
    x.append(z)
    x.append(z1)
    node.vd.append(z)
    node.vd.append(z1)

#for ¬ ( ... ^ ... )
def nand_conn(node, i):
    x = node.v
    y = x[i][1][:]
    del x[i]
    if isinstance(y[0],list):
        z = ["¬", y[0][:]]
    else:
        z = ["¬", [y[0][:]]]
    if isinstance(y[2],list):
        z1 = ["¬", y[2][:]]
    else:
        z1 = ["¬", [y[2][:]]]
    f = x[:]
    f.append(z)
    s = x[:]
    s.append(z1)
    
    node.l = Node(f)
    node.l.vd.append(z)
    node.l.p = node
    node.r = Node(s)
    node.r.vd.append(z1)
    node.r.p = node

#for ... -> ...
def if_conn(node, i):
    x = node.v
    y = x[i][:]
    del x[i]
    f = x[:]
    if isinstance(y[0],list):
        z = ["¬", y[0][:]]
    else:
        z = ["¬", [y[0][:]]]
    f.append(z)
    s = x[:]
    s.append(y[2][:])
    
    node.l = Node(f)
    node.l.vd.append(z)
    node.l.p = node
    node.r = Node(s)
    node.r.vd.append(y[2][:])
    node.r.p = node

#for ... <-> ...
def iff_conn(node,i):
    x = node.v
    y = x[i]
    del x[i]
    f = x[:]
    f.append(y[0][:])
    f.append(y[2][:])
    s = x[:]

    if isinstance(y[0],list):
        z = ["¬", y[0][:]]
    else:
        z = ["¬", [y[0][:]]]
    if isinstance(y[2],list):
        z1 = ["¬", y[2][:]]
    else:
        z1 = ["¬", [y[2][:]]]
    s.append(z)
    s.append(z1)
    node.l = Node(f)
    node.l.vd.append(y[0][:])
    node.l.vd.append(y[2][:])
    node.l.p = node
    node.r = Node(s)
    node.r.vd.append(z)
    node.r.vd.append(z1)
    node.r.p = node

#for ... ^ ...
def and_conn(node, i):
    x = node.v
    y = x[i][:]
    del x[i]
    x.append(y[0])
    x.append(y[2])
    node.vd.append(y[0][:])
    node.vd.append(y[2][:])

#for ¬ ( ... -> ... )    
def nif_conn(node, i):
    x = node.v
    y = x[i][1][:]
    del x[i]
    x.append(y[0])
    if isinstance(y[2],list):
        z1 = ["¬", y[2][:]]
    else:
        z1 = ["¬", [y[2][:]]]
    x.append(z1)
    node.vd.append(y[0][:])
    node.vd.append(z1)

#for ¬ ( ... <-> ... )
def niff_conn(node, i):
    x = node.v
    y = x[i][1]
    del x[i]
    f = x[:]
    f.append(y[0][:])
    f.append(y[2][:])
    s = x[:]
    s.append(y[2][:])
    
    node.l = Node(f)
    node.l.vd.append(y[0][:])
    node.l.p = node
    node.r = Node(s)
    node.r.vd.append(y[2][:])
    node.r.p = node
