def topologicalSort(jobs, deps):
  graph = Graph(jobs)
  for job, dep in deps:
    graph.addDep(job, dep)
  return traverse(graph)

def traverse(graph):
  order = []
  free = []
  for node in graph.nodes:
    if node.num == 0:
      free.append(node)
  while len(free):
    node = free.pop()
    order.append(node.job)
    clear(node, free)
  bad = any(node.num for node in graph.nodes)
  return [] if bad else order

def clear(node, free):
  while len(node.deps):
    dep = node.deps.pop()
    dep.num -= 1
    if dep.num == 0:
      free.append(dep)
    

class Graph:
  def __init__(self, jobs):
    self.nodes = []
    self.graph = {}
    for job in jobs:
      self.addNode(job)
      
  def addNode(self, job):
    self.graph[job] = Node(job)
    self.nodes.append(self.graph[job])
    
  def addDep(self, job, dep):
    node = self.getNode(job)
    depNode = self.getNode(dep)
    node.deps.append(depNode)
    depNode.num += 1
    
  def getNode(self, job):
    if job not in self.graph:
      self.addNode(job)
    return self.graph[job]
  
class Node:
  def __init__(self, job):
    self.job = job
    self.deps = []
    self.num = 0