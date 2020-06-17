class Tree:
    def __init__(self):
        self.root = None
        
    def getRoot(self):
        return self.root
    
    def setRoot(self, node):
        self.root = node
        self.root.vd = node.v[:]
    
    #find_next finds to next free node to be decomposed
    #uses a depth search
    def find_next(self):
        if(self.root != None):
            return self._find_next(self.root)
        else:
            return None

    def _find_next(self, node):
        if node==self.root and node.d==True:
            return None
        elif node.l == None and node.r == None:
            return node
        elif (node.l).d:
            if (node.r).d:
                node.d = True
                if node.p == None:
                    return None
                return self._find_next(node.p)
            else:
                return self._find_next(node.r)
        else:
            return self._find_next(node.l ) 

    def print_tree(self):
        if(self.root != None and self.root.l != None):
            (self._print_tree(self.root,"",False))
        elif(self.root != None):
            (self._print_tree(self.root,"",True))

    #makes sentences look nicer when printed in tree       
    def print_sen(self,xs):
        sen = ""
        for x in xs:
            if isinstance(x,list):
                sen = sen + "("+self.print_sen(x)+")"
            else:
                sen+=x
        return sen

    def print_sen_set(self,xss):
        i=0
        line = ""
        while i<len(xss):
            line+= self.print_sen(xss[i])
            if (i+1)<len(xss):
                line+=", "
            i+=1
        return line

    def _print_tree(self,node, prefix, end):
        ending = ""
        if node.c:
            ending = "   x"
        print(prefix, "`- " if end else "|- ", self.print_sen_set(node.vd), ending, sep="")
        prefix += "   " if end else "|  "
        if not end:
            self._print_tree(node.l,prefix,((node.l.l==None)and(node.l.r==None)))
            self._print_tree(node.r,prefix, ((node.r.l==None)and(node.r.r==None)))

    #has to be done with separate function from printing to stop python
    #being lazy and not printing the full tree
    def contradicted(self):
        if(self.root != None):
            return (self._contradicted(self.root))

    def _contradicted(self,node):
        if not ((node.l==None)and(node.r==None)):
            s = self._contradicted(node.l)
            s = s and self._contradicted(node.r)
            return s
        elif node.c:
            return True
        return False
