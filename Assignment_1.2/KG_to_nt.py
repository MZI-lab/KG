from rdflib import Graph
g = Graph()
g.parse('./full_KG_final.ttl', format='ttl')
g.serialize('./full_KG_final.nt', format='nt')