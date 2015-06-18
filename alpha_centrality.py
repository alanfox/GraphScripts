def alpha_centrality(G,alpha = 1.0, evalue = 'percolation_state'): 
    """Compute the alpha centrality (ref) for nodes in G: 

    alpha centrality is a generalisation of eigenvector centrality allowing
    for use of an external source of importance (default is percolation state).
    The factor alpha determines the relative weight given to internal network
    compared to external.
    
    Basically
    
    x = inverse((I - alpha * transpose(A)) * e
    
    Test with examples from: Bonacich and Lloyd
    >>>import networkx as nx
    >>>G = nx.DiGraph()
    >>>G.add_edges_from([('a','b'),('b','c'),('c','d'),('d','a'),('e','a')])
    >>>percolation_state = {}
    >>>percolation_state['a'] = 1.0
    >>>percolation_state['b'] = 1.0
    >>>percolation_state['c'] = 1.0
    >>>percolation_state['d'] = 1.0
    >>>percolation_state['e'] = 1.0
    >>>for node in G.nodes():
    >>>   G.node[node]['percolation_state'] = percolation_state[node]
    >>>alpha_centrality(G,0.5)
    {'a': matrix([[ 2.53333333]]),
     'b': matrix([[ 2.26666667]]),
     'c': matrix([[ 2.13333333]]),
     'd': matrix([[ 2.06666667]]),
     'e': matrix([[ 1.]])}    
    
    Potential problems with singular matrices    
    
    From:     Eigenvector-like measures of centrality for asymmetric relations
    Phillip Bonacich, , Paulette Lloyd
    doi:10.1016/S0378-8733(01)00038-7

    """ 

    import networkx as nx
    import numpy as np
    
# first find vector e of external importance. Put in a np matrix for later
# matrix multiplication. Ordered by node order (for s in G returns the same
# order as G.nodes() and also same as adjacency_matrix(G))
    
    e_dict = nx.get_node_attributes(G,evalue)
    
    e = []
    for s in G:
        e.append(e_dict[s])
    em = np.matrix(e)
    emt = np.transpose(em)
    
# get attribute matrix
    
    A = nx.adjacency_matrix(G, weight = None)
    
# get identity matrix of same dimension
    
    I = np.matrix(np.identity(len(nx.nodes(G))))  
    
 # construct matrix for alpha centrality calculation   
    
    B = I - alpha*np.transpose(A)
    
# inverse (possible problem with singular matrix)
    
    C = np.linalg.inv(B)
    
# complete alpha centrality calculation
    
    D = C*emt

# get back into a dictionary to return
    alpha_cent = {}
    i = 0
    for s in G:
        alpha_cent[s] = float(D[i,0])
        i = i + 1

    return alpha_cent          