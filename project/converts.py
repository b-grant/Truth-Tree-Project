#all check functions are for checking syntax of a sentence

#function that returns whether there is an equal amount of open and closed brackets
def check_bracks(x):
    i = 0
    correct = True
    bopen = 0
    while (correct and i<(len(x))):
        if (x[i]=="("):
            bopen+=1
        elif (x[i]==")"):
            if bopen==0:
                correct = False
            else:
                bopen-=1
        i+=1
    return (correct and (bopen==0))

#function that checks the syntax of any binary connectives
def check_biconn(x, i):
    biconn_list = ["v", "^", "->", "<-", "<->"]
    if (i==0 or i+1==(len(x))):
        return False
    elif (x[i-1]=="(" or x[i+1]==")" or x[i-1] in biconn_list or x[i+1] in biconn_list):
            return False

    if len(x)==3:
        return True
    elif x[i-1]==")":
        return True
    elif x[i+1]=="(":
        return True
    elif i>1 and i<(len(x)-2):
        if x[i-2]=="(" and x[i+2]==")":
            return True
    else:
        return False    

#function that checks the syntax of a negation
def check_not(x, i, b):
    if (i+1)==(len(x)):
        return False
    elif i == 0 and x[i+1]=="(":
        if (b[i+1]+1) == len(x):
            return True
        else:
            return False
    elif x[i-1]=="(" and x[i+1]=="(":
        if (b[i-1]-1) == b[i+1]:
            return True
        else:
            return False
    else:
        return False

#decided whether a connective is binary or a negation
def check_conn(x, i, b):
    if (x[i]=="¬"):
        return check_not(x,i, b)
    else:
        return check_biconn(x,i)

#checks the syntax of a variable
def check_var(x, i, con):
    if len(x[i])>1:
        print("Not a single letter variable")
        return False
    if (i==0):
        return True
    sym = ["v", "^", "¬", "->", "<-", "<->",")"]
    bsym = ["v", "^", "->", "<-", "<->", "("]
    if (i+1)<(len(x)):
        a = x[i+1]
        if (a not in sym):
            return False

    b = x[i-1]
    if (b not in bsym):
        return False
    return True

#converts a string into a usable nested list
#eg. p ^ ( p -> r ) becomes ["p",["p","<->","r"]]
def brackets(string, c, b):

    current = []
    i = c
    while i<len(string):
        if string[i]=="(":
            current.append(brackets(string, i+1, b))
            i = b[i]
        elif string[i]==")":
            return current
        else:
            current.append(string[i])
        i+=1
    return current

#find_match creates a dictionary matching
#opening bracket position to closing bracket position
#it also checks if there are too many brackets
def find_match(s):
    next_dict = {}
    bstack = []
    i=0
    while i<len(s):
        if s[i] == '(':
            bstack.append(i)
        elif s[i] == ')':
            if len(bstack) == 0:
                print("Uneven brackets")
                return False
            next_dict[bstack.pop()] = i
        i+=1

    if len(bstack) > 0:
        print("Uneven brackets")
        return False
    if 0 in next_dict:
        if next_dict[0]==(len(s)-1):
            print("Unnecessary Brackets")
            return False
    for key in next_dict:
        if next_dict[key]==(key+2) and (not s[key-1] == "¬"):
            print("Unnecessary Brackets")
            return False
        if (key+1) in next_dict:
            if ((next_dict[key])-1)==next_dict[key+1]:
                print("Double Brackets")
                return False
       
    return next_dict
            
#main convertion function
#checks the syntax of a sentence, converts it and returns it
def convert(string):
    x = string.split()
    b_dict = find_match(x)
    if b_dict==False:
        return False
    var_list = []
    conn_list = ["v", "^", "¬", "->", "<-", "<->"]
    i = 0
    valid = True
    while valid and (i<(len(x))):
        if (x[i] in conn_list):
            valid = check_conn(x,i, b_dict)
        elif (x[i]!="(" and x[i]!=")"):
            valid = check_var(x,i,conn_list)
            if (x[i] not in var_list):
                var_list.append(x[i])
        i+=1

    if not valid:
        print("Syntax Error")
        return False

    #2) convert to nested list
    x = brackets(x, 0, b_dict)
    return( x )
