import json

class hasse:


    relation_diagram = ""

    def reach_in_two_steps(edges,u,v):
        for t1 in edges[u]:
            # print("t1 {}".format(t1))
            for t2 in edges[t1]:
                # print("t2{}".format(t2))
                if t2 == v:
                    # print ("{}->{}->{} ?= {}".format(u,t1,t2,v))
                    return True
        return False     

    def hasse(num,edges):
        # print(edges)
        res = []
        for u in range(num):
            for v in edges[u]:
                # print ("{}?{}".format(u,v))
                if (not hasse.reach_in_two_steps(edges,u,v)):
                    res.append((u,v))
        return res

    def dumpJSON(num,e):
        obj = {
            "graph": {
                "number_of_nodes": str(num),
                "names" : ["OutX"+str(i) for i in range(num)],
                "edges" : [{"from":str(u), "to":str(v)} for (u,v) in e]
            } 
        }
        return json.dumps(obj)

# dumpJSON(3,hasse(3,[[1,2],[2],[]]))
