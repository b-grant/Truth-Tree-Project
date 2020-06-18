class Node:
    def __init__(self, val):
        #left node
        self.l = None
        #right node
        self.r = None
        #parent node
        self.p = None
        #v is the list of sentences present at that node
        self.v = val
        #vd is the list of sentences that should be printed at a node
        #this prevents repetition of sentences that are being carried down a path
        self.vd = []
        #boolean for whether a path is done
        self.d = False
        #boolean for whether there is a contradiction
        self.c = False
