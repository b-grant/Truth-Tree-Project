class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.p = None
        #v is the list of sentences present at that node
        self.v = val
        #vd is the list of sentences that should be printed at a node
        #this prevents repetition of sentences that are being carried down a path
        self.vd = []
        self.d = False
        self.c = False
