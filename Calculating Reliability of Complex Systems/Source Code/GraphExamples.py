import networkx as nx

class node(object):
    def __init__(self,number,p):
        self.Num = number
        self.P = p
    def __repr__(self):
        return "{"+str(self.Num) +"  R=" + str(self.P) +"}"
    def __str__(self):
        return "{"+str(self.Num) +"  R=" + str(self.P)+"}"


def graph1(): # P = 0.25
    G = nx.Graph()

    #define nodes
    n1 = node(1,1)
    n2 = node("A",0.5)
    n3 = node("B",0.5)
    n4 = node(99,1)

    #map edges
    t = [(n1,n2),(n2,n3),(n3,n4)]
    G.add_edges_from(t)

    #return graph, source, target
    return G, n1, n4

def graph2(): # P = 0.68
    G = nx.DiGraph()

    #define nodes
    n1 = node(1,1)
    n2 = node("A",0.6)
    n3 = node("B",0.6)
    n4 = node("C",0.5)
    n5 = node(99,1)
    n6 = node(0,1)
    n7 = node(0,1)

    #map edges
    t = [(n1,n6),(n6,n2),(n6,n4),(n2,n3),(n3,n7),(n1,n6),(n6,n4),(n4,n7),(n7,n5)]
    G.add_edges_from(t)

    #return graph, source, target
    return G, n1, n5

def graph3(): # P = 0.99999801
    G = nx.Graph()

    #define nodes
    n1 = node(1,1)
    n2 = node(0,1)
    n3 = node("A",0.99)
    n4 = node("B",0.99)
    n5 = node(0,1)
    n6 = node("C",0.99)
    n7 = node("D",0.99)
    n8 = node(0,1)
    n9 = node(0,1)
    n10 = node(99,1)

    #map edges
    t = [(n1,n2),(n2,n3),(n2,n5),(n3,n4),(n4,n9),(n9,n10),(n5,n6),(n6,n8),(n8,n9),(n5,n7),(n7,n8)]
    G.add_edges_from(t)

    #return graph, source, target
    return G, n1, n10

def graph4(): # P = 0.999999
    G = nx.Graph()

    #define nodes
    n1 = node(1,1)
    n3 = node("A",0.99)
    n4 = node("B",0.99)
    n5 = node("C",0.99)
    n7 = node(99,1)

    #map edges
    t = [(n1,n3),(n1,n4),(n1,n5),(n5,n7),(n4,n7),(n3,n7)]
    G.add_edges_from(t)

    #return graph, source, target
    return G, n1, n7

def graph5(): #P = 0.5624994375
    G = nx.MultiDiGraph()

    #define nodes
    n1 = node(0,1)
    n2 = node("A",0.75)
    n3 = node("B",0.99)
    n4 = node("C",0.99)
    n5 = node("D",0.99)
    n6 = node("E",0.75)
    n7 = node(99,1)

    #map edges
    t = [(n1,n2),(n2,n3),(n2,n4),(n2,n5),(n3,n6),(n4,n6),(n5,n6),(n6,n7)]
    G.add_edges_from(t)

    #return graph, source, target
    return G, n1, n7

def graph6(): # P = .81243 source http://www.ecs.umass.edu/ece/koren/FaultTolerantSystems/simulator/NonSerPar/nsnpframe.html
                    #  click on help then click "non-series/parallel system"
    G = nx.DiGraph()

    #define nodes
    n0 = node(0,1)
    n1 = node(0,1)
    n2 = node("A",0.9)
    n3 = node("B",0.8)
    n4 = node("C",0.7)
    n5 = node("D",0.5)
    n6 = node("E",0.9)
    n7 = node("F",0.9)
    n8 = node(99,1)
    

    #map edges
    t = [(n0,n1),(n1,n2),(n2,n4),(n4,n6),(n6,n7),(n7,n8),(n1,n3),(n3,n6),(n2,n5),(n5,n7)]
    G.add_edges_from(t)

    #return graph, source, target
    return G, n0, n8


def graph7(): # P = 0.999988238107
    G = nx.DiGraph()

    #define nodes
    n1 = node(0,1)
    n2 = node("A",0.99)
    n3 = node("B",0.99)
    n5 = node("C",0.99)
    n6 = node("D",0.99)
    n7 = node("E",0.99)
    n8 = node("F",0.99)
    n9 = node("G",0.99)
    n11 = node(99,1)

    #map edges
    t = [(n1,n2),(n2,n3),(n3,n11),(n1,n5),(n5,n6),(n6,n7),(n7,n11),(n1,n8),(n8,n9),(n9,n11)]
    G.add_edges_from(t)

    #return graph, source, target
    return G, n1, n11

def graph8(): # P = 0.9582606 source http://d577289.u36.websitesource.net/articles/ReliabilityEng-Part12.pdf
    G = nx.DiGraph()

    #define nodes
    n1 = node(0,1)
    n2 = node("A",0.8) #a
    n3 = node("B",0.9) #b
    n5 = node("C",0.75) #c
    n6 = node("D",0.85) #d
    n7 = node("E",0.92) #e
    n8 = node("F",0.99) #f
    n9 = node(99,1)

    #map edges
    t = [(n1,n2),(n2,n3),(n3,n8),(n8,n9),(n1,n5),(n5,n7),(n7,n8),(n1,n6),(n6,n7),(n7,n8)]
    G.add_edges_from(t)

    #return graph, source, target
    return G, n1, n9


def graph9(): # P = 0.6876576 source http://www.ecs.umass.edu/ece/koren/FaultTolerantSystems/simulator/NonSerPar/nsnpframe.html
              # click help series parallel system
    G = nx.DiGraph()

    #define nodes
    n1 = node(0,1)
    n2 = node("A",0.9) #a
    n3 = node("B",0.8) # b
    n4 = node("C",0.7) # c
    n5 = node("D",0.9) # h
    n6 = node("E",0.8) # d
    n7 = node("F",0.9) # e
    n8 = node("G",0.5) # f
    n9 = node("H",0.6) # g
    n10 = node(99,1)

    #map edges
    t = [(n1,n2),(n2,n3),(n3,n4),(n4,n5),(n5,n10),(n3,n6),(n6,n5),(n1,n7),(n7,n8),(n8,n9),(n9,n5)]
    G.add_edges_from(t)

    #return graph, source, target
    return G, n1, n10 
        
    
def graph10(): # P = 0.9582606 http://d577289.u36.websitesource.net/articles/ReliabilityEng-Part12.pdf
              # example 4
    G = nx.DiGraph()

    #define nodes
    n1 = node(0,1)
    n2 = node("A",0.8) #a
    n3 = node("B",0.9) # b
    n4 = node("C",0.75) # c
    n5 = node("D",0.85) # d
    n6 = node("E",0.92) # e
    n7 = node("F",0.99) # f
    n8 = node(99,1)

    #map edges
    t = [(n1,n2),(n1,n4),(n1,n5),(n2,n3),(n3,n7),(n7,n8),
         (n4,n6),(n6,n7),(n5,n6)]
    G.add_edges_from(t)

    #return graph, source, target
    return G, n1, n7 


def graph11(): #P = 0.99797
              
    G = nx.DiGraph()

    #define nodes
    n1 = node(1,1)
    n2 = node("A",0.95) #a
    n3 = node("B",0.98) # c
    n4 = node("C",0.95) # b1
    n5 = node("D",0.95) # b2
    n6 = node("F",0.9) # d
    n7 = node("E",0.81) # e1
    #n8 = node(8,0.9) # e2
    n9 = node(99,1)

    #map edges
    t = [(n1,n2),(n2,n4),(n4,n9),(n2,n5),(n5,n9),
         (n1,n3),(n3,n6),(n6,n9),
         (n3,n7),(n7,n9)]
    G.add_edges_from(t)

    #return graph, source, target
    return G, n1, n9

def graph12(): #P = 0.94369
              
    G = nx.DiGraph()

    #define nodes
    n1 = node(1,1)
    n2 = node("A",0.25) 
    n3 = node("B",0.3) 
    n4 = node("C",0.35) 
    n5 = node("D",0.4) 
    n6 = node("E",0.45) 
    n7 = node("F",0.5) 
    n9 = node(99,1)

    #map edges
    t = [(n1,n2),(n1,n3),(n1,n4),(n1,n5),(n1,n6),(n1,n7),
         (n2,n9),(n3,n9),(n4,n9),(n5,n9),(n6,n9),(n7,n9)]
    G.add_edges_from(t)

    #return graph, source, target
    return G, n1, n9


def graph13(): 
              
    G = nx.DiGraph()

    #define nodes
    nSource = node(0,1)
    a = node("A",0.99)
    b = node("B", 0.25)
    c = node("C",0.25)
    d = node("D", 0.25)
    e = node("E",0.25)
    f = node("F", 0.25)
    g = node("G",0.99)
    h = node("H", 0.25)
    i = node("I",0.25)
    j = node("J", 0.25)
    k = node("K",0.25)
    l = node("L", 0.25)
    m = node("M",0.99)
    n = node("N", 0.25)
    o = node("O",0.25)
    p = node("P", 0.25)
    q = node("Q",0.25)
    r = node("R", 0.25)
    s = node("S",0.99)
    nTarget = node(99, 1)
    

    #map edges
    t = [(nSource, a),(a,b), (b,g),(a,c),(c,g),(a,d),(d,g),(a,e),(e,g),(a,f),(f,g),
         (g,h),(h,m),(g,i),(i,m),(g,j),(j,m),(g,k),(k,m),(g,l),(l,m),
         (m,n),(n,s),(m,o),(o,s),(m,p),(p,s),(m,q),(q,s),(m,r),(r,s),
         (b,h),(h,n),(f,l),(l,r),(s,nTarget)]
    G.add_edges_from(t)

    #return graph, source, target
    return G, nSource, nTarget 
