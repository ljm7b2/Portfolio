import networkx as nx
import matplotlib.pyplot as plt
import itertools as it
from GraphExamples import *
import copy
COUNTER = 0

def get_all_combinations(nodes):
    """return all combinations of nodes from N-N+1 to N"""
    all_combinations = []
    for num in range (len(nodes) + 1):
    #for num in range (1,len(nodes)):
        all_combinations.extend([combo for combo in it.combinations(nodes,num)])

    return all_combinations

def build_master_data_structure(all_combinations, nodes, all_paths):
    """Builds master data structure of all working and non working combinations
       If A,B,C,D,E are nodes the structure will look similar to:
       [ [["+ or -"],["A","B"],["C","D","E"]],
         [["+ or -"],["A","D"],["B","C","E"]],......]
       Where:
       [[Subtract or add to Reliability],[Broken Nodes],[Working Nodes]]
    
    """
    master = []
    #master.append([["+"],[],nodes]) #append all working

    for line in all_combinations:
        
        broken_nodes = [nde for nde in line]
       
        working_nodes = [nde for nde in nodes if nde not in broken_nodes]
        
        if will_it_break_graph_flow(broken_nodes, all_paths):
            master.append([["-"], broken_nodes, working_nodes])
        else:
            master.append([["+"], broken_nodes, working_nodes])
             
    #master.append([["-"],nodes,[]])#append all broken
    return master

def will_it_break_graph_flow(ndes,all_paths):
    """Checks to see if selected Broken nodes will break all flow in graph"""
    temp_paths, count = copy.deepcopy(all_paths), 0 

    for val in ndes:
       
        for index in range(len(temp_paths)):
            
            if val in all_paths[index]:
                temp_paths[index].append("broken")
         
    for path in temp_paths:
        
        if "broken" in path:
            count += 1

    if count >= len(temp_paths):      
        return True
    else:        
        return False


def get_reliability(master_struct, fileHandle):
    """Return the probability of the system"""
    Total_P = 0
    for line in master_struct:
        if "+" in line[0]:
            
            prob_b, formula = 1, ""
            for val in line[1]: #broken combinations
                prob_b *= (1 - val.P)
                formula += " * (1 - " + str(val.P)+ ")"

            prob_w = 1
            for val in line[2]: #working combinations
                prob_w *= val.P
                formula += " * ("+ str(val.P) + ")"

            Total_P += (prob_b * prob_w)
            formula += "  -----> = " + str(Total_P)
            
            write_formula_file(formula, fileHandle)
    return Total_P

def display_graph(G, reliability_of_system ):
    """Displays graph visual"""
    nx.draw_networkx(G,
                     node_size = 400,
                     font_size = 16,
                     width = 3.0,
                     edge_color = 'g',
                     node_color = 'c')

    plt.title("Reliability of System: " + str( reliability_of_system))

    plt.show()

def write_formula_file(formula_line, file_handle):

    formula_line = " + " + formula_line[3:]
    
    file_handle.write(formula_line)
    file_handle.write('\n\n')

####MAIN####

file_handle = open("formula.txt","w")

Graph, src, trgt = graph6()

#create a list of path sets in graph
all_paths = [[nde for nde in path if type(nde.Num) != int]
             for path in nx.all_simple_paths(Graph, source = src, target = trgt)]

nodes = [nde for nde in Graph.nodes() if type(nde.Num) != int]

combos = get_all_combinations(nodes)

master = build_master_data_structure(combos, nodes, all_paths)

reliability_of_system =  get_reliability(master, file_handle)

file_handle.close()

print "Reliability of System:", reliability_of_system

display_graph(Graph, reliability_of_system)
