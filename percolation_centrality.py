def percolation_centrality(G,normalized=True,weighted_edges=False): 
    """Compute the percolation centrality (ref) for nodes in G: 
    the fraction of number of shortests paths that pass through each node,
    weighted with a function of the percolation state of the node. 

    The keyword normalized (default=True) specifies whether the  
    betweenness values are normalized by b=b/(n-1)(n-2) where 
    n is the number of nodes in G. 
 
    The keyword weighted_edges (default=False) specifies whether 
    to use edge weights (otherwise weights are all assumed equal). 

    The algorithm is from 
    Ulrik Brandes, 
    A Faster Algorithm for Betweenness Centrality. 
    Journal of Mathematical Sociology 25(2):163-177, 2001. 
    http://www.inf.uni-konstanz.de/algo/publications/b-fabc-01.pdf 
 
""" 
    import heapq
    import networkx as nx
    
# first find matrix of percolation status weights. Would be much easier 
# with numpy matrix multiplication but I want it all referenced by node names
    
    percolation_status = nx.get_node_attributes(G,'percolation_state')
    
    print percolation_status    
    
    sum_status = 0.0
    for s in G:
        sum_status = sum_status + percolation_status[s]
        
    print sum_status
    
    W = dict.fromkeys(G,0.0)
    for s in G:
        W[s] = 1.0/(sum_status - percolation_status[s])
    print W
        
    percolation_weight = {}    
    for v in G:
        percolation_weight[v] = dict.fromkeys(G,0.0)
    print percolation_weight
        
    
    for v in G:
        for s in G:
            percolation_weight[v][s] = W[v] * percolation_status[s]
    
    print percolation_weight
    
    betweenness=dict.fromkeys(G,0.0) # b[v]=0 for v in G 
    for s in G: 
        S=[] 
        P={} 
        for v in G: 
            P[v]=[] 
        sigma=dict.fromkeys(G,0)    # sigma[v]=0 for v in G 
        D={} 
        sigma[s]=1 
        if not weighted_edges:  # use BFS 
            D[s]=0 
            Q=[s] 
            while Q:   # use BFS to find shortest paths 
                v=Q.pop(0)
                S.append(v) 
                for w in G.neighbors(v): 
#                for w in G.adj[v]: # speed hack, exposes internals 
                    if w not in D: 
                        Q.append(w) 
                        D[w]=D[v]+1 
                    if D[w]==D[v]+1:   # this is a shortest path, count paths 
                        sigma[w]=sigma[w]+sigma[v] 
                        P[w].append(v) # predecessors  
        else:  # use Dijkstra's algorithm for shortest paths, 
               # modified from Eppstein 
            push=heapq.heappush 
            pop=heapq.heappop 
            seen = {s:0}  
            Q=[]   # use Q as heap with (distance,node id) tuples 
            push(Q,(0,s,s)) 
            while Q:    
                (dist,pred,v)=pop(Q) 
                if v in D: 
                    continue # already searched this node. 
                sigma[v]=sigma[v]+sigma[pred] # count paths 
                S.append(v) 
                D[v] = seen[v] 
#                for w in G.adj[v]: # speed hack, exposes internals 
                for w in G.neighbors(v): 
                    vw_dist = D[v] + G.get_edge(v,w) 
                    if w not in D and (w not in seen or vw_dist < seen[w]): 
                        seen[w] = vw_dist 
                        push(Q,(vw_dist,v,w)) 
                        P[w]=[v] 
                    elif vw_dist==seen[w]:  # handle equal paths 
                        sigma[w]=sigma[w]+sigma[v] 
                        P[w].append(v) 
 
 
        delta=dict.fromkeys(G,0)  
        while S: 
            w=S.pop()
            for v in P[w]: 
                delta[v]=delta[v]+\
                          (float(sigma[v])/float(sigma[w]))*(1.0+delta[w]) 
            if w != s: 
                betweenness[w]=(betweenness[w]
                                +delta[w]*percolation_weight[w][s])
                     
    # normalize 
    if normalized: 
        order=len(betweenness) 
        if order <=2: 
            return betweenness # no normalization b=0 for all nodes 
        scale=1.0/((order-2)) 
        for v in betweenness: 
            betweenness[v] *= scale 
 
    return betweenness             