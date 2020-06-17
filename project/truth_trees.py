from tree import Tree
from node import Node

from converts import convert




#makes sentences look nicer when printed in tree       
def print_sen(xs):
    sen = ""
    for x in xs:
        if isinstance(x,list):
            sen = sen + "("+print_sen(x)+")"
        else:
            sen+=x
    return sen

def print_sen_set(xss):
    i=0
    line = ""
    while i<len(xss):
        line+= print_sen(xss[i])
        if (i+1)<len(xss):
            line+=", "
        i+=1
    return line


#node done is run by make_tree
#determines whether a node should be ignored by find_next
#the reasons for this either being that a contradiction is present
#or that there are only sentence letters or negations of sentence letters left
def node_done(node):
    if node.l==None and node.r==None:
        if contradict(node.v):
            node.c = True
            node.d = True
        elif done(node.v):
            node.d = True
  

def contradict(xs):
    i = 0
    while i<len(xs):
        t = xs[i]
        if t[0]=="¬":
            s = t[1]
            j = 0
            while j<len(xs):
                if (len(s)==1):
                    if (s[0]==xs[j]):
                        return True
                if s==xs[j] or s == [xs[j]]:
                    return True
                
                j+=1
        i+=1
    if i == len(xs):
        return False

def done(xs):
    i = 0
    while i<len(xs):
        t = xs[i]
        if t[0]=="¬":
            if (not (len(t[1])==1)) or isinstance(t[1][0], list):
                return False
        elif len(t)>1:
            return False
        i+=1
    return True


#main conn function is called by make_tree
#calls diffrent conn functions to decide what needs to be done next

def conn(node):
    i = 0
    x = node.v
    found = False
    while not found and i<len(x):
        if len(x[i])==2:
            found = which_not(node,i)
        elif len(x[i])==3:
            found = which_bi(node,i)
        i+=1

def which_not(node,i):
    x=(node.v)[i][1]
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
    if x[1]=="v":
        or_conn(node,i)
    elif x[1]=="^":
        and_conn(node,i)
    elif x[1]=="->":
        if_conn(node,i)
    else:
        iff_conn(node,i)
    return True

def nn_conn(node, i):
    y = (node.v)
    x = y[i][:]
    k = 0
    while isinstance(x,list) and x[0]=="¬":
        k+=1
        x = x[1]
    if k%2==0:
        x = x[0]
    else:
        if isinstance(x[0],list):
            x = ["¬",x[0]]
        else:
            x = x = ["¬",[x[0]]]
    y[i] = x
        

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

def and_conn(node, i):
    x = node.v
    y = x[i][:]
    del x[i]
    x.append(y[0])
    x.append(y[2])
    node.vd.append(y[0][:])
    node.vd.append(y[2][:])

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
    




#function that creates the tree after sentences have been converted

def make_tree(t):
    node_done(t.root)
    d = t.root.d
    while not d:
        current = t.find_next()
        if current==None:
            d = True
        else:
            conn(current)
            node_done(current)
            
            
    
#run from options

def pick():
    d = False
    vs = []
    while not d:
        s = input("Input a sentence or type done to finish: ")
        if s=="done":
            d = True
        else:
            v = convert(s)
            if v==False:
                print("Try again")
            else:
                vs.append(v)
    return vs

def one():
    print("Example 1: contradiction with multiple paths")
    s = "r ^ ( ¬ ( p ) )"
    s1 = "p v ( ¬ ( q ) )"
    s2 = "( ¬ ( p ) ) -> q"
    l = convert(s)
    l1 = convert(s1)
    l2 = convert(s2)
    n = Node([l,l1,l2])
    t = Tree()
    t.setRoot(n)
    make_tree(t)
    print("\n\n\n")
    t.print_tree()
    contr = t.contradicted()
    print("Contradiction variable is", str(contr))
    print("\n\n")

    input("Press Enter to continue")

    print("\nExample 2: contradiction with one path")
    s = "p ^ ( ¬ ( p ) )"
    l = convert(s)
    n = Node([l])
    t = Tree()
    t.setRoot(n)
    make_tree(t)
    print("\n\n\n")
    t.print_tree()
    contr = t.contradicted()
    print("Contradiction variable is", str(contr))
    print("Therefore, satisfiability variable is", str(not contr))
    print("\n\n")

    input("Press Enter to continue")

    print("\nExample 3: satisfiable with no paths closed")
    s = "p v q"
    s1 = "( ¬ ( p ) ) -> r"
    s2 = "r ^ p"
    l = convert(s)
    l1 = convert(s1)
    l2 = convert(s2)
    n = Node([l,l1,l2])
    t = Tree()
    t.setRoot(n)
    make_tree(t)
    print("\n\n\n")
    t.print_tree()
    contr = t.contradicted()
    print("Contradiction variable is", str(contr))
    print("Therefore, satisfiability variable is", str(not contr))
    print("\n\n")

    input("Press Enter to continue")

    print("\nExample 4: satisfiable with some paths closed")
    s = "( ¬ ( p ) ) v q"
    s1 = "( ¬ ( ¬ ( p ) ) ) -> r"
    s2 = "r <-> p"
    l = convert(s)
    l1 = convert(s1)
    l2 = convert(s2)
    n = Node([l,l1,l2])
    t = Tree()
    t.setRoot(n)
    make_tree(t)
    print("\n\n\n")
    t.print_tree()
    contr = t.contradicted()
    print("Contradiction variable is", str(contr))
    print("Therefore, satisfiability variable is", str(not contr))
    print("\n\n")

    input("Press Enter to continue")

    print("\nExample 5: Tautology process for tautology")
    s = "( ¬ ( p ) ) v p"
    print("Original sentence is",s)
    l = convert(s)
    l = ["¬", l]
    n = Node([l])
    t = Tree()
    t.setRoot(n)
    make_tree(t)
    print("\n\n\n")
    t.print_tree()
    contr = t.contradicted()
    print("Contradiction variable for negated sentence is", str(contr))
    print("Therefore, tautologous variable for original sentence is", str(contr))
    print("\n\n")

    input("Press Enter to continue")

    print("\nExample 6: Tautology process for satisfiable sentence")
    s = "( ( ¬ ( p ) ) <-> q ) -> ( p ^ ( ¬ ( p ) ) )"
    print("Original sentence is",s)
    l = convert(s)
    l = ["¬", l]
    n = Node([l])
    t = Tree()
    t.setRoot(n)
    make_tree(t)
    print("\n\n\n")
    t.print_tree()
    contr = t.contradicted()
    print("Contradiction variable for negated sentence is", str(contr))
    print("Therefore, tautologous variable for original sentence is", str(contr))
    print("\n\n")

    input("Press Enter to continue")

    print("\nExample 7: Tautology process for contradiction")
    s = "p ^ ( ¬ ( p ) )"
    print("Original sentence is",s)
    l = convert(s)
    l = ["¬", l]
    n = Node([l])
    t = Tree()
    t.setRoot(n)
    make_tree(t)
    print("\n\n\n")
    t.print_tree()
    contr = t.contradicted()
    print("Contradiction variable for negated sentence is", str(contr))
    print("Therefore, tautologous variable for original sentence is", str(contr))
    print("\n\n")

    input("Press Enter to continue")

    print("\nExample 8: Extreme tautology process for tautology")
    s = "p v ( p v ( p v ( p v ( ( ¬ ( p ) ) v ( p v p ) ) ) ) )"
    print("Original sentence is",s)
    l = convert(s)
    l = ["¬", l]
    n = Node([l])
    t = Tree()
    t.setRoot(n)
    make_tree(t)
    print("\n\n\n")
    t.print_tree()
    contr = t.contradicted()
    print("Contradiction variable for negated sentence is", str(contr))
    print("Therefore, tautologous variable for original sentence is", str(contr))
    print("\n\n")


    input("Press Enter to continue")

    print("\n* Testing for incorrect inputs * \n")
    w = "("
    print(w)
    convert(w)
    w = ")"
    print(w)
    convert(w)
    w = "^"
    print(w)
    convert(w)
    w = "¬"
    print(w)
    convert(w)
    w = "p ¬ ( )"
    print(w)
    convert(w)
    w = ") ("
    print(w)
    convert(w)
    w = "¬ p"
    print(w)
    convert(w)
    w = "¬ ¬"
    print(w)
    convert(w)
    w = "( p ^ q )"
    print(w)
    convert(w)
    w = "( ¬ ( ( p ^ q ) ) ) v r"
    print(w)
    convert(w)
    w = "p v q v r"
    print(w)
    convert(w)
    w = "p1"
    print(w)
    convert(w)
    w = "p v ( ¬ ( p1 ) )"
    print(w)
    convert(w)

    print("\n\n")  
    

def two():
    vs = pick()
    if len(vs)>0:
        r = Node(vs)
        t = Tree()
        t.setRoot(r)
        make_tree(t)
        print("\n\n\n")
        t.print_tree()
        contr = t.contradicted()
        if contr:
            print("This is not satisfiable")
        else:
            print("This is satisfiable")
    else:
        print("An empty set has no tree")
    print("\n\n\n\n")

def three():
    vs = pick()
    if len(vs)> 0:
        r = Node(vs)
        t = Tree()
        t.setRoot(r)
        make_tree(t)
        print("\n\n\n")
        t.print_tree()
        contr = t.contradicted()
        if contr:
            print("This is a contradiction")
        else:
            print("This is not a contradiction")
    else:
        print("An empty set has no tree")
    print("\n\n\n\n")

def four():
    d = False
    vs = []
    while not d:
        s = input("Input a sentence: ")
        
        v = convert(s)
        if v==False:
           print("Try again")
        else:
            vs=v
            d = True
            
    if len(vs)>0:
        r = Node([["¬",vs]])
        t = Tree()
        t.setRoot(r)
        make_tree(t)
        print("\n\n\n")
        t.print_tree()
        contr = t.contradicted()
        if contr:
            print("This is a tautology")
        else:
            print("This is not a tautology")
    else:
        print("An empty set has no tree")
    print("\n\n\n\n")




        


            



